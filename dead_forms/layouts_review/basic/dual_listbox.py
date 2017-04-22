from crispy_forms.layout import Field


def dual_listbox_layout(field_name):
    field = Field(
        field_name,
        css_class="dual-listbox"
    )

    return field
