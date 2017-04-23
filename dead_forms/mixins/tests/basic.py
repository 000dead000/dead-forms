# -*- coding: utf-8 -*-

from django.views.generic import FormView

from dead_forms.forms.tests.basic import BasicForm
from dead_forms.mixins import AddMessageMixin
from dead_forms.mixins import AddRequestToFormMixin

from dead_forms.layouts.tests import BasicLayout


class TestsBasicMixin(AddMessageMixin, AddRequestToFormMixin, FormView):
    form_class = BasicForm

    def get_context_data(self, **kwargs):
        context = super(TestsBasicMixin, self).get_context_data(**kwargs)

        context['tests_tab'] = 'basic'
        context['form_layout'] = BasicLayout()

        return context
