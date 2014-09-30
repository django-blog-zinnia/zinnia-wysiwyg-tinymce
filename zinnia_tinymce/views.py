"""
Views for filebrowser in TinyMCE
"""
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from zinnia_tinymce.models import FileModel


class StaffMemberRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(StaffMemberRequiredMixin, self).dispatch(*args, **kwargs)


class FileBrowserView(StaffMemberRequiredMixin,
                      CreateView):
    model = FileModel
    fields = ['uploaded_file']
    success_url = '.'
    upload_tab_active = False
    limit = 20

    def get_context_data(self, **kwargs):
        context = super(FileBrowserView, self).get_context_data(**kwargs)
        if self.object:
            context['uploaded_file'] = self.object
        file_type = self.kwargs['file_type']
        context['file_type'] = file_type
        context['upload_tab_active'] = self.upload_tab_active
        context['files'] = FileModel.objects.filter(
            file_type=file_type)[:self.limit]
        return context

    def post(self, request, *args, **kwargs):
        self.upload_tab_active = False
        return super(FileBrowserView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.file_type = self.kwargs['file_type']
        self.object = form.save()
        return super(FileBrowserView, self).form_valid(form)


class RemoveFileView(StaffMemberRequiredMixin,
                     RedirectView):
    permanent = False
    pattern_name = 'tinymce-filebrowser'

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs['pk']
        file_type = self.kwargs['file_type']

        f = get_object_or_404(FileModel, pk=pk)
        f.delete()

        return super(RemoveFileView, self).get_redirect_url(
            file_type=file_type)
