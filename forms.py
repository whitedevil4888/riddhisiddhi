from django import forms
class Contact(forms.Form):
    firstname=forms.CharField(max_length=122)
    lastname=forms.CharField(max_length=122)
    phone=forms.CharField(max_length=15)
    email=forms.CharField(max_length=90)
    subject=forms.TextField()
    class Meta:		fields = ['firstname', 'lastname','phone','email','subject']
