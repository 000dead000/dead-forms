# -*- coding: utf-8 -*-

from crispy_forms.helper import FormHelper
from crispy_forms.helper import Layout


class BaseLayout(FormHelper):
    def __init__(self, *args, **kwargs):
        super(BaseLayout, self).__init__(*args, **kwargs)

        self.form_tag = False
        self.disable_csrf = True

        self.layout = Layout()
