from django import forms
from formsApp.models import Employee

class UserRegistrationForm(forms.Form):
    GENDER = [('M', 'Masculino'), ('F', 'Feminino')]
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('Primeiro nome muito grande')
        return inputFirstName
    
class EmpregadoForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'