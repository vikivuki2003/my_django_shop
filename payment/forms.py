from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, label="Full name")
    email = forms.EmailField(required=True, label="Email address")
    street_address = forms.CharField(max_length=255, required=True, label="Street address")
    apartment_address = forms.CharField(max_length=255, required=False, label="Apartment address")
    country = forms.CharField(max_length=100, required=False, label="Country")
    zipcode = forms.CharField(max_length=20, required=False, label="Zip code (Optional)")