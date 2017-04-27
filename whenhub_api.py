import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import django
django.setup()

import json
import requests
import github_parser

def append_access_token(url):
    return url + "?access_token="+hackathon.settings.WHENHUB_ACCESS_TOKEN

github_data = github_parser.parse_github_url("https://raw.githubusercontent.com/emeth-/the-flow/master/mary_perpetual_virginity.md")

resp = requests.post(append_access_token("https://api.whenhub.com/api/users/me/schedules"), json=github_data['schedule'])
schedule_data = resp.json()
#schedule_data = {"name":"we","scope":"private","viewCode":"3RkhC","id":"59014bafc5cc3e2f1c6d7130","userId":"5901073da40c0e472ccfd50d","createdAt":"2017-04-27T01:38:55.000Z","updatedAt":"2017-04-27T01:38:55.000Z","updatedBy":"5901073da40c0e472ccfd50d"}

whenhub_url = "https://studio.whenhub.com/schedules/"+schedule_data['id']

for event in github_data['events']:
    resp = requests.post(append_access_token("https://api.whenhub.com/api/schedules/"+schedule_data['id']+"/events"), json=event)
    print "****", resp.text
    event_data = resp.json()

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
