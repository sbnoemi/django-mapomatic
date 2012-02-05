Mapomatic provides for easy management of map points on a Google Map.  

Installation
------------
1) Install GeoDjango.  Please follow the instructions to `install GeoDjango for your platform: <https://docs.djangoproject.com/en/1.3/ref/contrib/gis/install/>`_.

2) Install django-mapomatic
::

	pip install -e git+git://github.com/sbnoemi/django-mapomatic.git#egg=django-mapomatic

Or::

	git clone git://github.com/sbnoemi/django-mapomatic.git
	cd django-mapomatic
	python setup.py

3) Add 'django.contrib.gis' and 'mapomatic' to your INSTALLED_APPS setting.

Requirements
------------
* GeoDjango