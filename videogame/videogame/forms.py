from django import forms
from videogame.models import user

class userforms(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"
        
