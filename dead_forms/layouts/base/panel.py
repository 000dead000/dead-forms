# -*- coding: utf-8 -*-

from crispy_forms.layout import Div
from crispy_forms.layout import HTML


def panel_layout(header=None, content=None,  footer=None, style="default", extra_css_class=""):
    components = []

    if header:
        components.append(
            Div(
                header,
                css_class="panel-heading"
            )
        )

    if content:
        components.append(
            Div(
                content,
                css_class="panel-body"
            )
        )

    if footer:
        components.append(
            Div(
                footer,
                css_class="panel-footer"
            )
        )

    return Div(
        *components,
        css_class="panel panel-{} {}".format(
            style,
            extra_css_class
        )
    )
