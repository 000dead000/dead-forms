# -*- coding: utf-8 -*-

from dead_forms.layouts import BaseLayout
from dead_forms.layouts.basic import chosen_select_layout


class BasicLayout(BaseLayout):
    @staticmethod
    def make_chosen_select():
        field = chosen_select_layout("dar_forms_tests_chosen_select")
        return field

    def make_layout(self):
        # Chosen select
        self.layout.fields.append(
            self.make_chosen_select()
        )

    def __init__(self, *args, **kwargs):
        super(BasicLayout, self).__init__(*args, **kwargs)
        self.make_layout()
