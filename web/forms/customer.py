from django.forms import ModelForm
from web import models

class CustomerForm(ModelForm):
    """
    客户表单
    """
    #   类似serializer序列化，（model就是指定序列化对象， fields就是指定序列化字段， __all__代表所有）
    class Meta:
        model = models.Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        #   解决多重继承问题
        super(CustomerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label