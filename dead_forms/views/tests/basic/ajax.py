# -*- coding: utf-8 -*-

import time

from django.template.loader import render_to_string

from dead_common.mixins import AjaxResponseMixin
from dead_common.mixins import JSONResponseMixin
from dead_common.mixins import EnsureCSRFMixin

from dead_forms.mixins import BaseFormMixin


class TestsBasicAJAXCBV(EnsureCSRFMixin, JSONResponseMixin, AjaxResponseMixin, BaseFormMixin):
    template_name = "dead-forms/tests/basic/ajax.html"

    def get_context_data(self, **kwargs):
        context = super(TestsBasicAJAXCBV, self).get_context_data(**kwargs)

        context['tests_subtab'] = 'ajax'

        return context

    def get_ajax(self, request, *args, **kwargs):
        template_file = "dead-forms/tests/basic/table/main.html"
        params = {}

        html = render_to_string(
            template_name=template_file,
            context=params,
            request=request
        )

        data = {
            'html': html,
        }

        return self.render_to_json_response(data)

TestsBasicAJAX = TestsBasicAJAXCBV.as_view()
