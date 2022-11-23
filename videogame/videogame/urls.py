"""videogame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('showuser', views.showuser, name="showuser"),
     path('Insertuser', views.Insertuser, name="Insertuser"),
     path('showgame', views.showgame, name="showgame"),
     path('Insertgame', views.Insertgame, name="Insertgame"),
     path('showtournament', views.showtournament, name="showtournament"),
     path('Inserttournament', views.Inserttournament, name="Inserttournament"),
     path('Deluser/<int:id>', views.Deluser, name="Deluser"),
     path('Delgame/<int:id>', views.Delgame, name="Delgame"),
     path('Deltournament/<int:id>', views.Deltournament, name="Deltournament"),
     path('sortuser',views.sortuser,name="sortuser"),
     path('sortgame',views.sortgame,name="sortgame"),
     path('sorttournament',views.sorttournament,name="sorttournament"),
     path('edituser/<int:id>', views.edituser, name="edituser"),
     path('updateuser/<int:id>', views.updateuser, name="updateuser"),
     path('runQueryuser',views.runQueryuser,name="runQueryuser"),
     path('ProcessCustomQuery/', views.ProcessCustomQuery, name="ProcessCustomQuery"),
     path('InputCustomQuery/', views.InputCustomQuery, name="InputCustomQuery"),
    # path('EditEvent/<int:id>',views.EditEvent,name="EditEvent"),
    path("", views.index,name='index'),
]
