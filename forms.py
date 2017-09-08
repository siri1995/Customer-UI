from django.forms import ModelForm, inlineformset_factory

from .models import Customer, Address


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ()




AddressFormSet = inlineformset_factory(Customer, Address,
                                            form=AddressForm, extra=1)