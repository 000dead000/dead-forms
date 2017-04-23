# -*- coding: utf-8 -*-

from django.views.generic import FormView

from dead_forms.mixins import AddMessageMixin
from dead_forms.mixins import AddRequestToFormMixin


class BaseFormMixin(AddMessageMixin, AddRequestToFormMixin, FormView):
    pass