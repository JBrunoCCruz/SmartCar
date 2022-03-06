from .models import *

class IpForm(forms.ModelForm):
    ipNumber = forms.CharField(widget = forms.TextInput(
        attrs = { 'class':'form-control', 'required':'true'}
    ))
