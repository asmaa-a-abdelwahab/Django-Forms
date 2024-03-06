from django import forms
from .models import Compound

class CompoundForm(forms.Form):
    
    email = forms.EmailField(label='Please enter your institutional Email Address')
    cpd_id = forms.IntegerField(label='Compound ID')
    
    is_synthesis_protocol_available = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'}),
        label='Is the synthesis protocol used for this compound already available in the database? If yes, check this box and enter the id in the next field'
    )
    
