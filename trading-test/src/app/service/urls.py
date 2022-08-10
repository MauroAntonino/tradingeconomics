from django.urls import path
from app.infra.http.authorize_connection.views import GetSite
urlpatterns: list = [
    path('v1/get_site', GetSite.as_view(), name='pie-chart')
]
