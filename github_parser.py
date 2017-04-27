import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import django
django.setup()
from bs4 import BeautifulSoup

import json
import requests

def parse_github_url(url):
    """
    soup = BeautifulSoup(htmlstring)
    soup.findAll('div', style="width=300px;")
    """
    """
    for div in soup.findAll('div', attrs={'class':'image'}):
        print div.find('a')['href']
        print div.find('a').contents[0]
        print div.find('img')['src']
    """

    final_results = {
        "schedule": {
            "name": "",
            "scope": "public"
        },
        "events": []
    }

    rawhtml = requests.get("https://raw.githubusercontent.com/emeth-/the-flow/master/mary_perpetual_virginity.md")
    soup = BeautifulSoup(rawhtml.text)

    for schedule_data in soup.findAll('h1'):
        final_results['schedule']['name'] = schedule_data.string
        break

    return {
        "schedule": {
            "name": "Did Jesus have brothers born of Mary?",
            "scope": "public"
        },
        "events": [
            {
              "when": {
                "period": "year",
                "startDate": "0145",
                "endDate": "0145",
                "relative": "145 A.D."
              },
              "name": "Protoevangelium of James: No",
              "description": "Part of New Testament Apocrypha. \
            \
            While it does not explicitly assert Mary's perpetual virginity after the birth of Jesus, it does identify the brothers and sisters of Christ to be Joseph's children from a marriage previous to his union with Mary. <a href='https://books.google.com/books?id=dsZzsAtggnUC&lpg=PP1&dq=L.%20Gambero%2C%20Mary%20and%20the%20Fathers%20of%20the%20Church&pg=PA35#v=onepage&q&f=false'>Mary and the Fathers of the Church: The Blessed Virgin Mary in Patristic Thought, pg. 35-41</a>\
            \
            There's an excellent article here that summarizes this document and its impact <a href='http://www.hippieheretic.com/2015/12/did-mary-remain-perpetual-virgin.html'>here</a>.\
            ",
              "icon": "https://upload.wikimedia.org/wikipedia/commons/4/49/Codex_Tchacos_p33.jpg",
              "resources": [
                "https://en.wikipedia.org/wiki/Gospel_of_James",
                "https://upload.wikimedia.org/wikipedia/commons/4/49/Codex_Tchacos_p33.jpg"
              ],
              "customFieldData": {"opinion": "no"},
            }
        ]
    }

github_data = parse_github_url("https://raw.githubusercontent.com/emeth-/the-flow/master/mary_perpetual_virginity.md")
