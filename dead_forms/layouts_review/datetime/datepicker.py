from crispy_forms.layout import Field


def date_picker_layout(field_name, css_class="", with_icon=True, attrs={}):
    if with_icon:
        field = Field(
            field_name,
            template="dead-layouts/datepicker.html",
            css_class=css_class,
            **attrs
        )
    else:
        field = Field(
            field_name,
            template="dead-layouts/datepicker-noicon.html",
            css_class=css_class,
            **attrs
        )

    return field
