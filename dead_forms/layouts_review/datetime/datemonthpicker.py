from crispy_forms.layout import Field


def date_month_picker_layout(field_name, css_class=""):
    field = Field(
        field_name,
        template="dead-layouts/date-month-picker.html",
        css_class=css_class
    )

    return field
