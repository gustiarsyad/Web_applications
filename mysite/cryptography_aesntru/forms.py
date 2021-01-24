from django import forms

class Cryptographyaesntru(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email
