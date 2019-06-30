from django.forms import ModelForm
from web import models


class PaymentForm(ModelForm):
    """
    账单表单
    """
    class Meta:
        model = models.Payment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        for name,field in self.files.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        self.fields['customer'].empty_label = '请选择客户'


class PaymentUserForm(ModelForm):
    """
    账单的客户表单
    """
    class Meta:
        model = models.Payment
        exclude = ['customer',]

    def __init__(self, *args, **kwargs):
        super(PaymentUserForm, self).__init__(*args, **kwargs)

        for name,field in self.files.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
