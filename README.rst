Mapomatic provides for easy management of map points on a Google Map.  

Installation
------------
#) Install GeoDjango.  Please follow the instructions to `install GeoDjango for your platform: <https://docs.djangoproject.com/en/1.3/ref/contrib/gis/install/>`_.

#) Install django-mapomatic
::

	pip install -e git+git://github.com/sbnoemi/django-mapomatic.git#egg=django-mapomatic

Or::

	git clone git://github.com/sbnoemi/django-mapomatic.git
	cd django-mapomatic
	python setup.py

#) Add 'django.contrib.gis' and 'mapomatic' to your INSTALLED_APPS setting.

Requirements
------------
* GeoDjango