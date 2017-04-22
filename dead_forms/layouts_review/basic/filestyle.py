# -*- coding: utf-8 -*-

from crispy_forms.layout import Field

from ..base import panel_layout


def filestyle_layout(field_name):
    field = Field(
        field_name,
        css_class="bs-file",
        data_buttonText="Archivo"
    )

    return panel_layout(field)
