from . models import watchupload,contact
from django import forms



class uploadforms(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control', 'rows': 3}),
        required=True
    )

    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class':'form-control'}),
        required=True
    )

    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class':'form-control'}),
        required=True
    )

    class Meta:
        model = watchupload
        fields=['name','description','price','image']


class contactform(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )
    message=forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'})
    )

    class Meta:
        model =contact
        fields=['name','email','message']
