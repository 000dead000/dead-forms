# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from dead_common.mixins import AjaxResponseMixin
from dead_common.mixins import JSONResponseMixin
from dead_common.mixins import EnsureCSRFMixin
from dead_forms.forms.tests import BasicNormalForm
from dead_forms.layouts.tests import BasicNormalLayout
from dead_common import utilities


class TestsBasicAJAXCBV(EnsureCSRFMixin, JSONResponseMixin, AjaxResponseMixin, TemplateView):
    template_name = "dead-forms/tests/basic/ajax.html"

    def get_context_data(self, **kwargs):
        context = super(TestsBasicAJAXCBV, self).get_context_data(**kwargs)

        context['tests_tab'] = 'basic'
        context['tests_subtab'] = 'ajax'

        return context

    def get_ajax(self, request, *args, **kwargs):
        template_file = "dead-forms/tests/basic/form.html"
        form = BasicNormalForm()
        layout = BasicNormalLayout()

        params = {
            "form": form,
            "form_layout": layout
        }

        html = utilities.render_template_to_string(
            template_file=template_file,
            params=params,
            request=request
        )

        data = {
            'html': html,
        }

        return self.render_to_json_response(data)

TestsBasicAJAX = TestsBasicAJAXCBV.as_view()
