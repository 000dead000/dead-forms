# -*- coding: utf-8 -*-

from dead_forms.mixins.tests import BaseFormMixin


class TestsBasicToolsCBV(BaseFormMixin):
    template_name = "dead-forms/tests/basic/tools.html"

    def get_context_data(self, **kwargs):
        context = super(TestsBasicToolsCBV, self).get_context_data(**kwargs)

        context['tests_subtab'] = 'tools'

        return context

TestsBasicTools = TestsBasicToolsCBV.as_view()
