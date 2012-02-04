from django.utils import unittest
from django.template import Template, loader, Context


class TemplateTestCase(unittest.TestCase):
    def setUp(self):
        pass

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