# -*- coding: utf-8 -*-

from crispy_forms.layout import HTML
from crispy_forms.layout import Div

from dead_forms.layouts import BaseLayout
from dead_forms.layouts.base import buttons_layout
from dead_forms.layouts.base import panel_layout
from dead_forms.layouts.base import row_layout
from dead_forms.layouts.base import rule_layout
from dead_forms.layouts.base import subtitle_layout
from dead_forms.layouts.base import title_layout


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

    @staticmethod
    def create_panels():
        description = "Panels"

        panels = Div(
            panel_layout(
                content=HTML("<b>Panel 1</b>")
            ),
            panel_layout(
                content=buttons_layout([
                    {
                        "text": "Boton de prueba",
                    },
                ])
            ),
            panel_layout(
                header=HTML("Un panel mas"),
                content=buttons_layout([
                    {
                        "text": "Boton de prueba",
                    },
                ]),
                footer=HTML("Con pie de pagina")
            ),

            panel_layout(
                header=HTML("Un panel mas"),
                content=HTML(u"""lorem ipsum <b>xyz</b> abc"""),
                footer=HTML("Con pie de pagina"),
                style="info"
            ),
        )

        return {
            "description": description,
            "field": panels,
        }

    @staticmethod
    def create_rows():
        description = "Rows"

        rows = Div(
            HTML("<b>Fila 1</b>"),
            row_layout(
              elements=[
                  {
                      "content": HTML("Columna 1"),
                  },
                  {
                      "content": HTML("Columna 2"),
                  }
              ]
            ),
            HTML("<br>"),
            HTML("<b>Fila 2</b>"),
            row_layout(
                elements=[
                    {
                        "content": HTML("Columna 1"),
                        "size": 3,
                    },
                    {
                        "content": HTML("Columna 2"),
                        "size": 9,
                    }
                ]
            ),
        )

        return {
            "description": description,
            "field": rows,
        }

    @staticmethod
    def create_rule():
        description = "Rule"

        rules = Div(
            HTML("Hola"),
            rule_layout(),
            HTML("Hola"),
        )

        return {
            "description": description,
            "field": rules,
        }

    @staticmethod
    def create_subtitle():
        description = "Subtitle"

        subtitles = Div(
            subtitle_layout("Hola mundo!"),
        )

        return {
            "description": description,
            "field": subtitles,
        }

    @staticmethod
    def create_title():
        description = "Title"

        titles = Div(
            title_layout("Hola mundo!"),
        )

        return {
            "description": description,
            "field": titles,
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
            self.create_panels(),
            self.create_rows(),
            self.create_rule(),
            self.create_subtitle(),
            self.create_title(),
        ]

        for field in fields:
            self.wrap_tr(field)

    def __init__(self, *args, **kwargs):
        super(BasicToolsLayout, self).__init__(*args, **kwargs)
        self.make_layout()
