# -*- coding: utf-8 -*-

from crispy_forms.layout import HTML

from dead_forms.layouts import BaseLayout
from dead_forms.layouts.base import buttons_layout


class BasicToolsLayout(BaseLayout):
    @staticmethod
    def create_field_1():
        field = "field_1"

        return {
            "description": "Field 1",
            "field": field,
        }

    @staticmethod
    def create_buttons():
        description = "Buttons"

        buttons = buttons_layout([
            {
                "text": "Boton 1",
            },
            {
                "text": "Boton 2",
                "style": "success",
            },
            {
                "text": "Boton 3",
                "style": "warning",
                "icon": """<i class="fa fa-clock-o" aria-hidden="true"></i>""",
            },
            {
                "text": "Google",
                "style": "info",
                "is_button": False,
                "href": "http://www.google.com",
                "extra_attrs": {
                    "target": "_blank",
                }
            },
        ])

        return {
            "description": description,
            "field": buttons,
        }

    def wrap_tr(self, field):
        description = field.get("description")
        example = field.get("field")

        self.layout.fields.append(HTML("<tr>"))
        self.layout.fields.append(HTML("<td>"))
        self.layout.fields.append(HTML(description))
        self.layout.fields.append(HTML("</td>"))
        self.layout.fields.append(HTML("<td>"))
        self.layout.fields.append(example)
        self.layout.fields.append(HTML("</td>"))
        self.layout.fields.append(HTML("</tr>"))

    def make_layout(self):
        fields = [
            # self.create_field_1(),
            self.create_buttons(),
        ]

        for field in fields:
            self.wrap_tr(field)

    def __init__(self, *args, **kwargs):
        super(BasicToolsLayout, self).__init__(*args, **kwargs)
        self.make_layout()
