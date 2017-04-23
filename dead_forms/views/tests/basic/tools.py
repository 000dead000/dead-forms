# -*- coding: utf-8 -*-

from dead_forms.mixins import BaseFormMixin

from dead_forms.forms.tests import BasicToolsForm
from dead_forms.layouts.tests import BasicToolsLayout


class TestsBasicToolsCBV(BaseFormMixin):
    template_name = "dead-forms/tests/basic/tools.html"
    form_class = BasicToolsForm

    def get_context_data(self, **kwargs):
        context = super(TestsBasicToolsCBV, self).get_context_data(**kwargs)

        context['tests_tab'] = 'basic'
        context['tests_subtab'] = 'tools'
        context['form_layout'] = BasicToolsLayout()

        return context

TestsBasicTools = TestsBasicToolsCBV.as_view()
