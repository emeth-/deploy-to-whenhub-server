import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import django
django.setup()

import json
import requests

def append_access_token(url):
    return url + "?access_token="+hackathon.settings.WHENHUB_ACCESS_TOKEN

def parse_github_url(url):
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
