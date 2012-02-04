from django.http import HttpResponse
from django.shortcuts import render_to_response
from mapomatic.models import MapPoint

def index(request):
    map_points = MapPoint.objects.all()
    return render_to_response('mapomatic/map.html', {'map_points': map_points,})