# -*- coding: utf-8 -*-

from crispy_forms.layout import Div

from dead_base.layouts import date_picker_layout


def date_week_picker_layout(d1, d2):
    date_1 = Div(date_picker_layout(d1), css_class="date-week-picker")
    date_2 = Div(date_picker_layout(d2), css_class="date-week-picker")

    return [
        date_1,
        date_2,
    ]
