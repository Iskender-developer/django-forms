from django import forms

clacChoise = (
("-", '-'),
("+", '+'),
("*", '*'),
("/", '/'),
)

class ClacForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c_choise = forms.ChoiceField(choices=clacChoise)