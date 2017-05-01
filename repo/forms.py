from django import forms

class URLForm(forms.Form):
    input_url = forms.CharField(
        label='input_url',
        max_length = 300
    )
