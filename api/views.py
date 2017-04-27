from django.http import HttpResponse
import datetime
import json
from api.models import Widget
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
import github_parser
import whenhub_api

def json_custom_parser(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)



def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")

def load_widget(request):
    refer = request.META.get('HTTP_REFERER')
    if not refer:
        return TemplateResponse(request, 'error.html', context={
            "error": "Referred not detected."
        })

    #TODO make it work if it's the readme. This assumes it's not the readme.

    #refer = https://github.com/emeth-/the-flow/blob/master/mary_perpetual_virginity.md
    refer = refer.replace('/blob', '')
    refer = refer.replace('github.com', 'raw.githubusercontent.com')
    #refer = https://raw.githubusercontent.com/emeth-/the-flow/master/mary_perpetual_virginity.md

    github_data = github_parser.parse_github_url(refer)
    schedule_id = whenhub_api.create_widget(github_data)

    return TemplateResponse(request, 'horizontal_timeline.html', context={
        "schedule_id": schedule_id
    })

def create_widget(request):
    """
    request.POST Input:
        mode = ["vertical", "horizontal"]
        referrel_url = "https://github.com/emeth-/the-flow/blob/master/mary_perpetual_virginity.md"
    """
    #Fish.objects.filter(id=fish_id).delete()
    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)