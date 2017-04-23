# -*- coding: utf-8 -*-

from crispy_forms.layout import Div
from crispy_forms.layout import HTML

from dead_common import utilities


def row_layout(elements, extra_css_class="", id=None):
    if not id:
        id = utilities.generate_key()

    try:
        default_col_size = int(12 / len(elements))
    except:
        default_col_size = 12

    cols = []

    for element in elements:
        size = element.get("size", default_col_size)
        content = element.get("content", HTML(""))
        col_css = element.get("css", "")
        col_id = element.get("id", utilities.generate_key())

        row_css_class = "col-xs-12 col-md-{} {}".format(size, col_css)

        cols.append(Div(
            content,
            css_class=row_css_class,
            id=col_id
        ))

    return Div(
        *cols,
        css_class="row {}".format(extra_css_class),
        id=id
    )
