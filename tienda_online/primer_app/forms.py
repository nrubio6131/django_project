from django import forms

class form_contacto2(forms.Form):
    asunto= forms.CharField(help_text='100 characters max.')
    email= forms.EmailField(required=False)
    motivos= forms.CharField(widget=forms.Textarea)