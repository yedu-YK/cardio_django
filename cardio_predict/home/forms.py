from django import forms
from .models import CardioModel


class CardioForm(forms.ModelForm):
    class Meta:
        model = CardioModel
        fields = ("user_name","age","gender","cholesterol","height","weight","sbp","dbp","gluc","smoke","alco","active")
        labels = {
        'user_name':'Name',
        'sbp':'Systolic Blood Pressure',
        'dbp':'Diastolic Blood Pressure',
        'active':'Physical Activity',
        'gluc':'Glucose Level',
        'alco':'Alchol',
        'dbp':'Diastolic Blood Pressure',
        }
        widgets = {'bmi':forms.HiddenInput(),'bpc':forms.HiddenInput()}