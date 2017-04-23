# -*- coding: utf-8 -*-

from dead_forms.mixins import BaseFormMixin
from dead_forms.forms.tests import BasicNormalForm
from dead_forms.layouts.tests import BasicNormalLayout


class TestsBasicNormalCBV(BaseFormMixin):
    template_name = "dead-forms/tests/basic/normal.html"
    form_class = BasicNormalForm

    def get_context_data(self, **kwargs):
        context = super(TestsBasicNormalCBV, self).get_context_data(**kwargs)

        context['form_layout'] = BasicNormalLayout()
        context['tests_tab'] = 'basic'
        context['tests_subtab'] = 'normal'

        return context

TestsBasicNormal = TestsBasicNormalCBV.as_view()
