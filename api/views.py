from django.http import HttpResponse
import datetime
import json
from api.models import Widget
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

def json_custom_parser(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)



def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")

def load_widget(request):
    return TemplateResponse(request, 'load_widget.html', context={
        "users": []
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