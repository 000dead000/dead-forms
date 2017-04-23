# -*- coding: utf-8 -*-

from crispy_forms.layout import Div
from crispy_forms.layout import HTML


def buttons_layout(buttons, align_class="text-right"):
    html = """
    <div class="btn-group" role="group" aria-label="...">
    """

    for button in buttons:
        options = {
            "class": "",
            "style": "default",
            "text": "Enviar",
            "type": "button",
            "name": "",
            "id": "",
            "icon": "",
            "href": "",
            "is_button": True,
            "extra_attrs": None
        }

        options.update(button)

        extra_attrs = ""
        if options.get("extra_attrs"):
            for k, v in options.get("extra_attrs").items():
                if extra_attrs != "":
                    extra_attrs += " "

                extra_attrs += u"{}={}".format(
                    k,
                    v
                )

        if options.get("is_button"):
            html += u"""
            <button name='{}' id='{}' class='btn {} btn-{}' type='{}' {}>{}{}</button>
            """.format(
                options.get("name"),
                options.get("id"),
                options.get("class"),
                options.get("style"),
                options.get("type"),
                extra_attrs,
                options.get("icon"),
                options.get("text") if options.get("icon") == "" else " {}".format(options.get("text")),
            )
        else:
            html += u"""
            <a href={} id='{}' class='btn {} btn-{}' {}>{}{}</a>
            """.format(
                options.get("href"),
                options.get("id"),
                options.get("class"),
                options.get("style"),
                extra_attrs,
                options.get("icon"),
                options.get("text") if options.get("icon") == "" else " {}".format(options.get("text")),
            )

    html += """
    </div>
    """

    return Div(
        HTML(html),
        css_class=align_class
    )
