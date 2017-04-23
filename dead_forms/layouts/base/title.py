# -*- coding: utf-8 -*-

from crispy_forms.layout import HTML


def title_layout(title, markup="h3", css_class=""):
    return HTML(
        u"""
        <{} class="{}">{}</{}>
        """.format(
            markup,
            css_class,
            title,
            markup
        )
    )