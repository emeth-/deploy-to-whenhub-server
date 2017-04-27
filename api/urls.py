from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^load_widget$', "api.views.load_widget"),
    url(r'^render_widget$', "api.views.render_widget"),
    url(r'^create_whenhub$', "api.views.create_whenhub"),

    url(r'^$', "api.views.load_frontend")
)
