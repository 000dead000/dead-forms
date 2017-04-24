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

    def make_dualselect(self):
        field = Field(
            'field_dual_select_1',
            css_class="dual-listbox"
        )

        return {
            'description': "Dual Listbox",
            'field': field,
        }

    def make_toggle(self):
        field = Field(
            'field_boolean_1',
            css_class="toggle-checkbox"
        )

        return {
            'description': "Toggle checkbpx",
            'field': field,
        }

    def make_layout(self):
        fields = [
            self.make_chosen_select(),
            self.make_bs_file(),
            self.make_dualselect(),
            self.make_toggle(),
        ]

        for field in fields:
            self.wrap_tr(field)
