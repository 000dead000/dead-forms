# -*- coding: utf-8 -*-

from dead_common.mixins import AjaxResponseMixin
from dead_common.mixins import JSONResponseMixin
from dead_common.mixins import EnsureCSRFMixin

from .base_form import BaseFormMixin


class BaseAJAXFormMixin(EnsureCSRFMixin, JSONResponseMixin, AjaxResponseMixin, BaseFormMixin):
    pass
