"""
Views for filebrowser in TinyMCE
"""
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.contrib.admin.views.decorators import staff_member_required

from zinnia.models import Entry

from zinnia_tinymce.models import FileModel


class StaffMemberRequiredMixin(object):

    @method_decorator(staff_member_required)
    @method_decorator(cache_control(max_age=0))
    def dispatch(self, *args, **kwargs):
        return super(StaffMemberRequiredMixin, self).dispatch(*args, **kwargs)


class EntryLinksView(StaffMemberRequiredMixin,
                     ListView):
    model = Entry
    template_name = 'zinnia_tinymce/entry_links.js'
    content_type = 'application/javascript'


class ImageLinksView(StaffMemberRequiredMixin,
                     ListView):
    template_name = 'zinnia_tinymce/image_links.js'
    content_type = 'application/javascript'

    def get_queryset(self):
        return FileModel.objects.filter(file_type='image')


class FileLinksView(StaffMemberRequiredMixin,
                    ListView):
    template_name = 'zinnia_tinymce/file_links.js'
    content_type = 'application/javascript'

    def get_queryset(self):
        return FileModel.objects.filter(file_type='file')


class FileBrowserCallBackView(StaffMemberRequiredMixin,
                              TemplateView):
    template_name = 'zinnia_tinymce/filebrowser.js'
    content_type = 'application/javascript'


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
