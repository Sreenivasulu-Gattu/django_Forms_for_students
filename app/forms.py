from django import forms

class SchoolForm(forms.Form):
    sname = forms.CharField()
    age = forms.IntegerField()
    