# -*- coding: utf-8 -*-

from crispy_forms.layout import Field

from ..base import panel_layout


def xlsx_layout(field_name, extensions='["xlsx"]', max_file_size=2048):
    field = Field(
        field_name,
        css_class="file widget-with-bootstrap-fileinput",
        data_preview_file_type="object",
        data_allowed_file_extensions=extensions,
        data_max_file_size=max_file_size,
        data_language="es",
        data_show_upload="false",
        data_browse_class="btn btn-default",
        data_browse_label=u"Archivo",
        data_browse_icon="<i class='fa fa-file-excel-o text-success'></i>",
        data_remove_from_preview_on_error="true"
    )

    return panel_layout(field)
