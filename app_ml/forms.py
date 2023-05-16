"""from django import forms

class CardioForm(forms.Form):
    name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=100)
    email= forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('1', 'Male'), ('2', 'Female')], widget=forms.RadioSelect())
    height = forms.FloatField()
    weight = forms.FloatField()
    systolic_pressure = forms.IntegerField()
    diastolic_pressure = forms.IntegerField()
    cholesterol = forms.ChoiceField(choices=[('1', 'Normal'), ('2', 'Above Normal'), ('3', 'Well Above Normal')], widget=forms.RadioSelect())
    glucose = forms.ChoiceField(choices=[('1', 'Normal'), ('2', 'Above Normal'), ('3', 'Well Above Normal')], widget=forms.RadioSelect())
    smoker = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], widget=forms.RadioSelect())
    alcohol_intake = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], widget=forms.RadioSelect())
    physical_activity = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], widget=forms.RadioSelect())
"""
from django import forms
from .models import Patient

SEXO_COICES = (
    ('Masculino', 1),
    ('Feminino', 0),
)
class CardioForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =(
            "name",
            "lastname",
            "email",
            "age",
            "gender",
            "weight",
            "height",
            "diastolic_pressure",
            "systolic_pressure",
            "glucose",
            "cholesterol",
            "smoker",
            "alcohol_intake",
            "physical_activity",

        )
