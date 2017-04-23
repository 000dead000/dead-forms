# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import TestsHome

from .views import TestsBasicNormal
from .views import TestsBasicAJAX

urlpatterns = [
    # home
    url(
        r'^$',
        TestsHome,
        name='tests-home'
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