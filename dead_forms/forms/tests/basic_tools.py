# -*- coding: utf-8 -*-

from django import forms

from dead_forms.forms import BaseForm


class BasicToolsForm(BaseForm):
    field_1 = forms.CharField(
        label="Field 1"
    )
