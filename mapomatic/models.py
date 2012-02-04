from django.contrib.gis.db import models


class MapPoint(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.location.x, self.location.y)