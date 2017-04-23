# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views.tests import TestsHome
from .views.tests.basic import TestsBasicTools
from .views.tests.basic import TestsBasicNormal
from .views.tests.basic import TestsBasicAJAX

urlpatterns = [
    # home
    url(
        r'^$',
        TestsHome,
        name='tests-home'
    ),

    # Basic
    url(
        r'^tests/basic/tools$',
        TestsBasicTools,
        name='tests-basic-tools'
    ),

    url(
        r'^tests/basic/normal$',
        TestsBasicNormal,
        name='tests-basic-normal'
    ),

    url(
        r'^tests/basic/ajax$',
        TestsBasicAJAX,
        name='tests-basic-ajax'
    ),
]