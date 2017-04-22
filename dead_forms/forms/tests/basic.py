# -*- coding: utf-8 -*-

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH

from .. import BaseForm

DUMMY_OPTIONS = []
for i in range(100):
    DUMMY_OPTIONS.append([
        i+1,
        u"Opción {}".format(i+1),
    ])


class BasicForm(BaseForm):
    dar_forms_tests_chosen_select = forms.ChoiceField(
        label="Opciones",
        choices=BLANK_CHOICE_DASH + list(DUMMY_OPTIONS),
        initial=""
    )
