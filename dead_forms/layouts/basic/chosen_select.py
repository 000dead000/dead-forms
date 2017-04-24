# -*- coding: utf-8 -*-

from dead_common import utilities

from crispy_forms.layout import Field


def chosen_select_layout(field_name, css_class="", hint_text=False, id=None):
    if not id:
        id = utilities.generate_key()

    css_class = u"chosen-select {} {}".format(
        css_class,
        "chosen-select-hint-text" if hint_text else ""
    )

    return Field(
        field_name,
        css_class=css_class,
        id=id
    )
