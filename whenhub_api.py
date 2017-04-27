import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import django
django.setup()

import json
import requests
import github_parser

github_data = github_parser.parse_github_url("https://raw.githubusercontent.com/emeth-/the-flow/master/mary_perpetual_virginity.md")

resp = requests.post("https://api.whenhub.com/api/users/me/schedules?access_token="+hackathon.settings.WHENHUB_ACCESS_TOKEN, json=github_data['schedule'])
schedule_data = resp.json()

whenhub_url = "https://studio.whenhub.com/schedules/"+schedule_data['id']

for event_data in github_data['events']:
    resp = requests.post("https://api.whenhub.com/api/schedules/"+schedule_data['id']+"/events?access_token="+hackathon.settings.WHENHUB_ACCESS_TOKEN, json=event_data)
    #event_data = resp.json()

print "whenhub_url", whenhub_url

#https://api.whenhub.com/api/schedules/<schedule_id>/events

#print json.dumps(resp.json(), indent=4)

"""
--The plan--

input = mode (vertical, horizontal)
- api call to create schedule
- create events one by one
- redirect user to widget
- add to local WIDGETS table
- environment variable with api key

"""
