# -*- coding: utf-8 -*-

from django import forms


class BaseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        return super(BaseModelForm, self).__init__(*args, **kwargs)

    @property
    def is_update(self):
        return self.instance.pk

    @property
    def is_create(self):
        return not self.is_update
