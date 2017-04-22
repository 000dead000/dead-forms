# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import TestsHome

from .views import TestsBasicNormal
from .views import TestsBasicAJAX

urlpatterns = [
    url(
        r'^tests$',
        TestsHome,
        name='tests'
    ),

    # Basic
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