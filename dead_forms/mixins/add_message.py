# -*- coding: utf-8 -*-

from django.contrib import messages


class AddMessageMixin(object):
    def add_success_message(self):
        msg = u"Operación realizada exitosamente"
        messages.add_message(
            self.request,
            messages.SUCCESS,
            msg
        )

    def add_error_message(self):
        msg = u"La información diligenciada en el formulario, requiere algunas correcciones"
        messages.add_message(
            self.request,
            messages.ERROR,
            msg
        )

    def form_valid(self, form):
        self.add_success_message()

        return super(AddMessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        self.add_error_message()

        return super(AddMessageMixin, self).form_invalid(form)

    def formset_valid(self, form):
        self.add_success_message()

        return super(AddMessageMixin, self).formset_valid(form)

    def formset_invalid(self, form):
        self.add_error_message()

        return super(AddMessageMixin, self).formset_invalid(form)

    def forms_valid(self, form, inlines):
        self.add_success_message()

        return super(AddMessageMixin, self).forms_valid(form, inlines)

    def forms_invalid(self, form, inlines):
        self.add_error_message()

        return super(AddMessageMixin, self).forms_invalid(form, inlines)
