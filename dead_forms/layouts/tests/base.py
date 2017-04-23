# -*- coding: utf-8 -*-

from crispy_forms.layout import HTML

from dead_forms.layouts import BaseLayout


class BaseTestLayout(BaseLayout):
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

    def __init__(self, *args, **kwargs):
        super(BaseTestLayout, self).__init__(*args, **kwargs)
        self.make_layout()
