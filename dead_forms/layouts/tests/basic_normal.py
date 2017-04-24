# -*- coding: utf-8 -*-

from crispy_forms.layout import Div
from crispy_forms.layout import Field

from dead_forms.layouts.basic import chosen_select_layout
from .base import BaseTestLayout


class BasicNormalLayout(BaseTestLayout):
    @staticmethod
    def make_chosen_select():
        field_1 = chosen_select_layout("field_chosen_select_1")
        field_2 = chosen_select_layout("field_chosen_select_2")
        field_3 = chosen_select_layout("field_chosen_select_3")
        field_4 = chosen_select_layout("field_chosen_select_4", hint_text=True)
        description = "Chosen Select"

        field = Div(
            field_1,
            field_2,
            field_3,
            field_4,
        )

        return {
            'description': description,
            'field': field,
        }

    def make_bs_file(self):
        field = Field(
            'field_bsfile',
            css_class="bs-file"
        )

        return {
            'description': "BS File",
            'field': field,
        }

    def make_layout(self):
        fields = [
            self.make_chosen_select(),
            self.make_bs_file(),
        ]

        for field in fields:
            self.wrap_tr(field)
