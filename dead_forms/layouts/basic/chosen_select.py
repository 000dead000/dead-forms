# -*- coding: utf-8 -*-

from crispy_forms.layout import Field


def chosen_select_layout(field_name, css_class="", id=""):
    css_class = u"chosen-select {}".format(
        css_class
    )

    return Field(
        field_name,
        css_class=css_class,
        id=id
    )
