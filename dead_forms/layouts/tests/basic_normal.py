# -*- coding: utf-8 -*-

from crispy_forms.layout import Div

from dead_forms.layouts.basic import chosen_select_layout
from .base import BaseTestLayout


class BasicNormalLayout(BaseTestLayout):
    @staticmethod
    def make_chosen_select():
        field_1 = chosen_select_layout("field_chosen_select_1")
        field_2 = chosen_select_layout("field_chosen_select_2")
        description = "Chosen Select"

        field = Div(
            field_1,
            field_2
        )

        return {
            'description': description,
            'field': field,
        }

    def make_layout(self):
        fields = [
            self.make_chosen_select(),
        ]

        for field in fields:
            self.wrap_tr(field)
