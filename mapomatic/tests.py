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