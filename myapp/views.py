from django.shortcuts import render
from django.http import HttpResponse
from .forms import CSVImportForm
import pandas as pd
import io

from .models import Fish

# Create
def create_fish(data):
    fish = Fish(**data)
    fish.save()
    return fish

# Read
def get_all_fishes():
    return Fish.objects.all()

def get_fish_by_species_code(code):
    return Fish.objects.get(species_code=code)

# Update
def update_fish_by_species_code(code, updated_data):
    fish = Fish.objects.get(species_code=code)
    for key, value in updated_data.items():
        setattr(fish, key, value)
    fish.save()
    return fish

# Delete
def delete_fish_by_species_code(code):
    fish = Fish.objects.get(species_code=code)
    fish.delete()




def remove_duplicates_from_csv(input_csv_path, column_name):
    # Lire le fichier CSV
    data = pd.read_csv(input_csv_path)

    # Supprimer les doublons
    data_clean = data.drop_duplicates(subset=column_name, keep='first')

    # Créez un objet en mémoire pour stocker le CSV
    csv_buffer = io.BytesIO()
    data_clean.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)  # Pour s'assurer que le fichier est lu depuis le début
    return csv_buffer



def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            # Exécuter le script de nettoyage
            input_path = form.instance.uploaded_file.path
            csv_buffer = remove_duplicates_from_csv(input_path, 'english_name')

            # Créez une réponse avec le contenu du CSV
            response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=cleaned_data.csv'
            return response

    else:
        form = CSVImportForm()

    return render(request, 'myapp/csv_form.html', {'form': form})


# views.py
from django.shortcuts import render
from .models import Fish

def fish_list_view(request):
    fishes = Fish.objects.all()
    return render(request, 'fish_list.html', {'fishes': fishes})
