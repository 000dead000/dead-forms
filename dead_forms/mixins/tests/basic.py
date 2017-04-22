# -*- coding: utf-8 -*-

from django.views.generic import FormView

from dar_forms.forms.tests.basic import BasicForm
from dar_forms.mixins import AddMessageMixin
from dar_forms.mixins import AddRequestToFormMixin

from dar_forms.layouts.tests import BasicLayout


class TestsBasicMixin(AddMessageMixin, AddRequestToFormMixin, FormView):
    form_class = BasicForm

    def get_context_data(self, **kwargs):
        context = super(TestsBasicMixin, self).get_context_data(**kwargs)

        context['tests_tab'] = 'basic'
        context['form_layout'] = BasicLayout()

        return context
