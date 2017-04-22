# -*- coding: utf-8 -*-

from crispy_forms.layout import Div


def panel_layout(element, extra_css_class=""):

    return Div(
        Div(
            element,
            css_class="panel-body"
        ),
        css_class="panel panel-default {}".format(extra_css_class)
    )
