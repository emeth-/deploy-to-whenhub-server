import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import django
django.setup()

import json
import requests
import github_parser

def append_access_token(url):
    return url + "&access_token="+hackathon.settings.WHENHUB_ACCESS_TOKEN

resp = requests.get(append_access_token("https://api.whenhub.com/api/users/me/schedules/59015f6ec5cc3e2f1c6d7150?filter[include][events]=media&filter[include]=media"))
schedule_data = resp.json()
print json.dumps(schedule_data, indent=4)
