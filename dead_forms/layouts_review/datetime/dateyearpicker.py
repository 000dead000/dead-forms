from crispy_forms.layout import Field


def date_year_picker_layout(field_name, css_class=""):
    field = Field(
        field_name,
        template="dead-layouts/date-year-picker.html",
        css_class=css_class
    )

    return field
