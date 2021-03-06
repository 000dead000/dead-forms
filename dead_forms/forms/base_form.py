# -*- coding: utf-8 -*-

from django import forms


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        return super(BaseForm, self).__init__(*args, **kwargs)
