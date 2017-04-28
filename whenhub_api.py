import hackathon.settings

import requests

def create_widget(github_data):

    print "***schedule data", github_data['schedule']
    resp = requests.post("https://api.whenhub.com/api/users/me/schedules?access_token="+hackathon.settings.WHENHUB_ACCESS_TOKEN, json=github_data['schedule'])
    schedule_data = resp.json()

    print "***schedule response", schedule_data

    for event_data in github_data['events']:
        resp = requests.post("https://api.whenhub.com/api/schedules/"+schedule_data['id']+"/events?access_token="+hackathon.settings.WHENHUB_ACCESS_TOKEN, json=event_data)
        #event_data = resp.json()

    return schedule_data['id']
    #return "https://studio.whenhub.com/schedules/"+schedule_data['id']
