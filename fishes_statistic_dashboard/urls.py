"""fishes_statistic_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import myapp as myapp
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import fish_list_view, create_fish, get_fish_by_species_code, \
    update_fish_by_species_code, delete_fish_by_species_code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]
urlpatterns += [
    # Lister tous les poissons
    path('fishes/', fish_list_view, name='fish_list'),

    # (Si vous avez une vue basée sur un formulaire pour ajouter un nouveau poisson)
    path('fishes/add/', create_fish, name='add_fish'),

    # Vue détaillée pour un poisson spécifique (basée sur le code d'espèce)
    path('fishes/<str:code>/', get_fish_by_species_code, name='fish_detail'),

    # Modifier un poisson existant
    path('fishes/<str:code>/edit/', update_fish_by_species_code, name='edit_fish'),

    # Supprimer un poisson
    path('fishes/<str:code>/delete/', delete_fish_by_species_code, name='delete_fish'),

    # ... (incluez d'autres URL comme celle pour l'upload CSV ici)
]

# Vos patterns d'URL actuels...

if settings.DEBUG:  # Seulement si DEBUG est True
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
