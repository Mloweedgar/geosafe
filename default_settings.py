# coding=utf-8

import os
from ast import literal_eval
from django.utils.translation import ugettext_lazy as _

_LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

# Opt-in to use layerfile direct disk access for InaSAFE Headless Celery
# workers instead of Http
USE_LAYER_FILE_ACCESS = literal_eval(os.environ.get(
    'USE_LAYER_FILE_ACCESS', 'True'))


# Location of local layer file that can be accessed by InaSAFE worker directly
# This path will be accessed by InaSAFE Celery Worker
#
# For example, if celery workers need to fetch layers from GeoSAFE with name
# vector_layer.shp, since this file is located in media folders in:
# /usr/src/app/geonode/uploaded/layers/vector_layer.shp
# GeoSAFE then tries to find its relative path from
# INASAFE_LAYER_DIRECTORY_BASE_PATH, which is vector_layer.shp. Then it
# appended the relative path to INASAFE_LAYER_DIRECTORY:
# /home/geosafe/layers/vector_layer.shp . Then this is the path that will be
# accessed by InaSAFE Headless Celery Worker
INASAFE_LAYER_DIRECTORY = os.environ.get(
    'INASAFE_LAYER_DIRECTORY', '/home/geosafe/media/')
INASAFE_LAYER_DIRECTORY_BASE_PATH = os.environ.get(
    'INASAFE_LAYER_DIRECTORY_BASE_PATH', '/usr/src/app/geonode/qgis_layer/')

# Location of InaSAFE Impact Layer output that can be accessed by
# GeoSAFE.
# This path will be accessed by GeoSAFE
GEOSAFE_IMPACT_OUTPUT_DIRECTORY = os.environ.get(
    'GEOSAFE_IMPACT_OUTPUT_DIRECTORY', '/home/geosafe/impact_layers/')


# Location of InaSAFE Impact Layer output base url
# This base url will be set as root path for GEOSAFE_IMPACT_OUTPUT_DIRECTORY
# Impact output path will be extracted from relative path from this base url
# then appended to GEOSAFE_IMPACT_OUTPUT_DIRECTORY.
#
# For example, if InaSAFE output path taken from analysis results coming from
# celery worker is: http://inasafe-output/output/20170519/temp_analysis.zip
# Then file path which will be accessed by GeoSAFE is:
# /home/geosafe/impact_layers/20170519/temp_analysis.zip
INASAFE_IMPACT_BASE_URL = os.environ.get(
    'INASAFE_IMPACT_BASE_URL', '/output/')


# Opt-in to use layerfile http access for InaSAFE Headless Celery
# workers instead of disk access
USE_LAYER_HTTP_ACCESS = literal_eval(os.environ.get(
    'USE_LAYER_HTTP_ACCESS', 'False'))


# This base url is needed for InaSAFE worker to be able to find Geonode to
# fetch layers
GEONODE_BASE_URL = 'http://localhost:8000/'


# Analysis Run Time Limit (in seconds)
# Task will exit if exceeded this hard limit
INASAFE_ANALYSIS_RUN_TIME_LIMIT = literal_eval(os.environ.get(
    'INASAFE_ANALYSIS_RUN_TIME_LIMIT', '600'))


# Analysis area limit (in meter squares)
# Create analysis will display warning if analysis extent
# exceeded this limit. User will be able to continue analysis
# with warning that analysis will might take a long time.
INASAFE_ANALYSIS_AREA_LIMIT = literal_eval(os.environ.get(
    'INASAFE_ANALYSIS_AREA_LIMIT', '1000000000'))


# QGIS report template settings
LOCALIZED_QGIS_REPORT_TEMPLATE = {
    # Below is a sample dict of locale to custom template
    # We will uncomment this when we have a custom template file
    # 'en': os.path.join(
    #     _LOCAL_ROOT, 'templates/geosafe/qgis_templates/en/map-report.qpt')
}

# InaSAFE Headless Settings modifier
INASAFE_SETTINGS_PATH = os.environ.get('INASAFE_SETTINGS_PATH', '')
MINIMUM_NEEDS_LOCALE_MAPPING_PATH = os.environ.get(
    'MINIMUM_NEEDS_LOCALE_MAPPING_PATH', '')

# Context layers. The order of the layers that we want to show
# in the map report.
REPORT_LAYER_ORDER = [
    # From top to bottom
    '@aggregation',
    '@impact',
    '@hazard',
    '@exposure',
    '@basemap'
]

# Hazard settings.
# Do not forget to add also the icon when adding new hazard.
HAZARD_DEFINITION = {
    'key': 'hazard',
    'name': _('hazard'),
    'categories': ['flood', 'tsunami', 'earthquake', 'volcano',
                   'volcanic_ash', 'cyclone'],
    'list_titles': [
        _('Select a flood layer'),
        _('Select a tsunami layer'),
        _('Select an earthquake layer'),
        _('Select a volcano layer'),
        _('Select a volcanic ash layer'),
        _('Select a cyclone layer'),
    ]
}

# Exposure settings.
# Do not forget to add also the icon when adding new exposure.
EXPOSURE_DEFINITION = {
    'key': 'exposure',
    'name': _('exposure'),
    'categories': [
        'population',
        'road',
        'structure',
        'land_cover',
    ],
    'list_titles': [
        _('Select a population layer'),
        _('Select a roads layer'),
        _('Select a structure layer'),
        _('Select a landcover layer'),
    ]
}

# Aggregation settings
AGGREGATION_DEFINITION = {
    'key': 'aggregation',
    'name': _('aggregation'),
    'list_title': _('Select an aggregation layer')
}

# The basemap
# Default Korona basemap doesn't load, so we uses OSM
REPORT_DEFAULT_BASEMAP = 'http://tile.openstreetmap.org/{z}/{x}/{y}.png'
