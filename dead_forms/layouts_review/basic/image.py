# -*- coding: utf-8 -*-

from crispy_forms.layout import Field

from ..base import panel_layout


def image_layout(field_name, extensions='["png", "jpg", "jpeg", "gif"]', max_file_size=200, min_height=227, min_width=227, max_height=227, max_width=227):
    field = Field(
        field_name,
        css_class="file widget-with-bootstrap-fileinput",
        data_preview_file_type="image",
        data_allowed_file_extensions=extensions,
        data_max_file_size=max_file_size,
        data_min_image_height=min_height,
        data_min_image_width=min_width,
        data_max_image_height=max_height,
        data_max_image_width=max_width,
        data_language="es",
        data_show_upload="false",
        data_browse_class="btn btn-default",
        data_browse_label=u"Imágen",
        data_browse_icon="<span class='glyphicon glyphicon-picture'></span>",
        data_remove_from_preview_on_error="true"
    )

    return panel_layout(field)
