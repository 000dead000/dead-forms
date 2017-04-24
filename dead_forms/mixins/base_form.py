# -*- coding: utf-8 -*-

from django.views.generic import FormView

from .add_message import AddMessageMixin
from .add_request_to_form import AddRequestToFormMixin


class BaseFormMixin(AddMessageMixin, AddRequestToFormMixin, FormView):
    pass