# -*- coding: utf-8 -*-

from dead_forms.mixins import BaseFormMixin


class TestsBasicNormalCBV(BaseFormMixin):
    template_name = "dead-forms/tests/basic/normal.html"

    def get_context_data(self, **kwargs):
        context = super(TestsBasicNormalCBV, self).get_context_data(**kwargs)

        context['tests_subtab'] = 'normal'

        return context

TestsBasicNormal = TestsBasicNormalCBV.as_view()
