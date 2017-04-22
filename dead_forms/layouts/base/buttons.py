# -*- coding: utf-8 -*-

from crispy_forms.layout import Div
from crispy_forms.layout import HTML


def buttons_layout(buttons, align_class="text-right"):
    html = """
    <div class="btn-group" role="group" aria-label="...">
          <button type="button" class="btn btn-default">Left</button>
          <button type="button" class="btn btn-default">Middle</button>
          <button type="button" class="btn btn-default">Right</button>
    """

    for button in buttons:
        options = {
            "class": "btn-default",
            "text": "Enviar",
            "type": "button",
            "name": "",
            "id": "",
            "icon": "",
        }

        options.update(button)

        html += u"""
        <button name='{}' id='{}' class='btn {}' type='{}'>{}{}</button>
        """.format(
            options.get("name"),
            options.get("id"),
            options.get("class"),
            options.get("type"),
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
