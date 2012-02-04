from django.utils import unittest
from django.template import Template, loader, Context
from mapomatic.models import MapPoint

class TemplateTestCase(unittest.TestCase):
    def setUp(self):
        MapPoint.objects.create(name='NYC', location='POINT(-73.9869510 40.7560540)')
        MapPoint.objects.create(name='Atlantic City', location='POINT(-74.422474 39.369341)')

    def test_map_html(self):
        """Test that mapomatic/map.html extends base.html and outputs a div 
        with ID "map" """
        t = loader.get_template('mapomatic/map.html')
        c = Context({})
        str = t.render(c)
        self.assertTrue(u'<div id="map">' in str)
        
    def test_base_html(self):
        """ Test that base.html pulls in the Google Maps and jQuery scripts, and 
        our custom JS.  This needs to change when we move our JS to an external file."""
        t = loader.get_template('base.html')
        c = Context({})
        str = t.render(c)
        self.assertTrue(u'http://maps.google.com/maps/api/js' in str)
        self.assertTrue(u'http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js' in str)
        self.assertTrue(u"map = new google.maps.Map(document.getElementById('map')" in str)
        
    def test_map_point_js_output(self):
        """ Test that our javascript is outputting the map_points array definition in 
        javascript correctly."""
        t = loader.get_template('base.html')
        c = Context({'map_points': MapPoint.objects.all()})
        str = t.render(c)
        self.assertRegexpMatches(str, r'map_points\.push\(\{\s*id:\s*\d+\s*,\s+name:\s*"NYC"\s*,\s+'
                                        + r'lat:\s*40\.756054\s*,\s+lng:\s*-73\.986951\s*\}\);')
        