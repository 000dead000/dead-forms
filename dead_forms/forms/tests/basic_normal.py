# -*- coding: utf-8 -*-

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH

from .. import BaseForm
from .base import DUMMY_OPTIONS


class BasicNormalForm(BaseForm):
    field_chosen_select_1 = forms.ChoiceField(
        label="Opciones 1",
        choices=BLANK_CHOICE_DASH + list(DUMMY_OPTIONS),
        initial="",
        help_text=" ",
        required=False
    )

    field_chosen_select_2 = forms.ChoiceField(
        label="Opciones 2",
        choices=BLANK_CHOICE_DASH + list(DUMMY_OPTIONS),
        initial="",
        help_text=" ",
        required=False
    )

    field_chosen_select_3 = forms.MultipleChoiceField(
        label="Opciones 3",
        choices=DUMMY_OPTIONS,
        initial="",
        help_text=" ",
        required=False
    )

    field_chosen_select_4 = forms.ChoiceField(
        label="Opciones 4 (hint_text=True)",
        choices=BLANK_CHOICE_DASH + list(DUMMY_OPTIONS),
        initial="",
        help_text=" ",
        required=False
    )

    field_bsfile = forms.FileField(
        label="BS File 1",
        required=False
    )

    field_dual_select_1 = forms.MultipleChoiceField(
        label="Dual list box",
        choices=DUMMY_OPTIONS,
        initial="",
        required=False
    )

    field_boolean_1 = forms.BooleanField(
        label="¿Acepta envio de correos electrónicos?",
        required=False
    )
