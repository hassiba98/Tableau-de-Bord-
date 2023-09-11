
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from myapp.models import Fish, CSVImport
from myapp.views import remove_duplicates_from_csv
from django.urls import path, reverse
from django.utils.html import format_html
from django.core.files import File
from django.shortcuts import get_object_or_404

admin.site.register(Fish)


class CSVImportAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_file', 'download_cleaned_file_link')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('download/<int:csvimport_id>/', self.admin_site.admin_view(self.download_cleaned_file),
                 name='download_cleaned_file'),
        ]
        return custom_urls + urls

    def download_cleaned_file_link(self, obj):
        if obj.cleaned_file:
            return format_html('<a href="{}">Télécharger le fichier clean</a>',
                               reverse('admin:download_cleaned_file', args=[obj.pk]))
        return "Aucun fichier clean disponible"

    download_cleaned_file_link.short_description = 'Fichier Clean'

    def download_cleaned_file(self, request, csvimport_id):
        csvimport = get_object_or_404(CSVImport, id=csvimport_id)
        if csvimport.cleaned_file:
            with open(csvimport.cleaned_file.path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{csvimport.cleaned_file.name}"'
                return response
        return redirect('admin:index')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # À ce stade, obj.uploaded_file contient le fichier CSV que l'utilisateur vient d'importer.
        # Vous pouvez maintenant appeler votre fonction pour nettoyer ce CSV et enregistrer le résultat dans obj.cleaned_file.
        input_path = obj.uploaded_file.path
        csv_buffer = remove_duplicates_from_csv(input_path, 'english_name')
        cleaned_filename = f"cleaned_{obj.uploaded_file.name}"
        obj.cleaned_file.save(cleaned_filename, File(csv_buffer))
        obj.save()


admin.site.register(CSVImport, CSVImportAdmin)
