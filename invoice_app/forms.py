from django import forms
from django.core  import validators
from invoice_app import models



class EntryForm(forms.ModelForm):

    class Meta:
        model = models.Item_entry  # class entry from models.py
        fields = "__all__"    # class attributes entry


class OrderForm(forms.ModelForm):

    class Meta:
        model = models.Item_sold
        fields = "__all__"

           