import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import django
django.setup()
from bs4 import BeautifulSoup

import json
import requests

def expand_year(year):
    year = str(year)
    while len(year) < 4:
        year = "0"+year
    return year

def parse_github_url(url):
    final_results = {
        "schedule": {
            "calendar": {
                "calendarType": "absolute"
            },
            "name": "",
            "scope": "public",
        },
        "events": []
    }

    rawhtml = requests.get(url)
    soup = BeautifulSoup(rawhtml.text)

    for schedule_data in soup.findAll('h1'):
        final_results['schedule']['name'] = schedule_data.string
        break

    for detail_block in soup.findAll('details'):
        for summary_block in detail_block.findAll('summary'):
            if '|' in summary_block.text:
                #valid block!
                summary_block_text_pieces = summary_block.text.split('|')
                #summary_block_html_pieces = str(summary_block).split('|')
                year = summary_block_text_pieces[0].strip().split(' ')[0].strip().replace('~', '')
                expanded_year = expand_year(year)
                full_summary_clause = summary_block_text_pieces[1].strip()
                #who = full_summary_clause.split(':')[0].strip()
                opinion = full_summary_clause.split(':')[1].strip().split(',')[0].strip()
                full_description = ""
                for detail_block in detail_block.findAll('blockquote'):
                    full_description = str(detail_block)

                final_results['events'].append({
                    "when": {
                      "period": "year",
                      "startDate": expanded_year,
                      "endDate": None,
                    },
                    "name": full_summary_clause,
              "description": full_description,
              "customFieldData": {"opinion": opinion},
            })


    return final_results

github_data = parse_github_url("https://raw.githubusercontent.com/emeth-/the-flow/master/mary_perpetual_virginity.md")
