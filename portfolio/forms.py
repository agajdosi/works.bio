from django import forms

class Artwork(forms.Form):
  title = forms.CharField(label='Title', max_length=100)
  created = forms.DateField(label='Created')
  preview = forms.FileField(label='preview')
  file = forms.FileInput()
  