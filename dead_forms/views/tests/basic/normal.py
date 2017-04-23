# -*- coding: utf-8 -*-

from dead_forms.mixins import BaseFormMixin
from dead_forms.forms.tests import BasicToolsForm


class TestsBasicNormalCBV(BaseFormMixin):
    template_name = "dead-forms/tests/basic/normal.html"
    form_class = BasicToolsForm

    def get_context_data(self, **kwargs):
        context = super(TestsBasicNormalCBV, self).get_context_data(**kwargs)

        context['tests_subtab'] = 'normal'

        return context

TestsBasicNormal = TestsBasicNormalCBV.as_view()
