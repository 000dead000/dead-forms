from crispy_forms.layout import Field


def datetime_picker_layout(field_name, css_class=""):
    field = Field(
        field_name,
        template="dead-layouts/datetimepicker.html",
        css_class=css_class
    )

    return field
