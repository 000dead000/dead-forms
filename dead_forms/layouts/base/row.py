# -*- coding: utf-8 -*-

from crispy_forms.layout import Div


def row_layout_fixed(elements, size, extra_css_class="", id=""):
    row_css_class = "col-xs-12 col-md-{}".format(size)
    cols = []

    for element in elements:
        cols.append(Div(
            element,
            css_class=row_css_class
        ))

    return Div(
        *cols,
        css_class="row {}".format(extra_css_class),
        id=id
    )


def row_layout_flexible(elements, sizes, extra_css_class="", id=""):
    cols = []

    idx = -1
    for element in elements:
        idx += 1
        size = sizes[idx]
        row_css_class = "col-xs-12 col-md-{}".format(size)

        cols.append(Div(
            element,
            css_class=row_css_class
        ))

    return Div(
        *cols,
        css_class="row {}".format(extra_css_class),
        id=id
    )
