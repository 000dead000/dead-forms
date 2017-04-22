# -*- coding: utf-8 -*-

from crispy_forms.layout import HTML


def subtitle_layout(subtitle, markup="h4", css_class=""):
    return HTML(
        u"""
        <{} class="{}">{}</{}>
        """.format(
            markup,
            css_class,
            subtitle,
            markup
        )
    )