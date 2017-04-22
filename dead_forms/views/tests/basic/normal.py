# -*- coding: utf-8 -*-

from dar_forms.mixins.tests import TestsBasicMixin


class TestsBasicNormalCBV(TestsBasicMixin):
    template_name = "dar-forms/tests/basic/normal.html"

    def get_context_data(self, **kwargs):
        context = super(TestsBasicNormalCBV, self).get_context_data(**kwargs)

        context['tests_subtab'] = 'normal'

        return context

TestsBasicNormal = TestsBasicNormalCBV.as_view()