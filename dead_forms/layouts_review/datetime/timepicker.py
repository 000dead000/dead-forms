from crispy_forms.layout import Field


def time_picker_layout(field_name, css_class=""):
    field = Field(
        field_name,
        template="dead-layouts/timepicker.html",
        css_class=css_class
    )

    return field
