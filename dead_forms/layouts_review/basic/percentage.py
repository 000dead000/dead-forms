from crispy_forms.bootstrap import AppendedText


def percentage_layout(field_name, css_class=""):
    field = AppendedText(
        field_name,
        "%",
        css_class=css_class
    )

    return field
