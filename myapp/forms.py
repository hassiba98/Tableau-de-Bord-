from django import forms

from myapp.models import CSVImport


class CSVImportForm(forms.ModelForm):
    class Meta:
        model = CSVImport
        fields = ['uploaded_file']
