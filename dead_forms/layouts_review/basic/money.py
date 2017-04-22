from crispy_forms.bootstrap import PrependedText


def money_layout(field_name, css_class=""):
    field = PrependedText(
        field_name,
        "$",
        css_class=css_class
    )

    return field
