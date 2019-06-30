from django import forms
from django.utils.safestring import mark_safe

from rbac import models


ICON_LIST = [
    ['fa fa-area-chart','<i class="fa fa-area-chart" aria-hidden="true"></i>'],
    ['fa fa-address-book','<i class="fa fa-address-book" aria-hidden="true"></i>'],
    ['fa fa-bandcamp','<i class="fa fa-bandcamp" aria-hidden="true"></i>'],
    ['fa fa-drivers-license-o','<i class="fa fa-drivers-license-o" aria-hidden="true"></i>'],
]
for item in ICON_LIST:
    item[1] = mark_safe(item[1])

class MenuModelForm(forms.ModelForm):
    """
    菜单表单
    """
    class Meta:
        model = models.Menu
        fields = ['title','icon']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'icon':forms.RadioSelect(
                choices=ICON_LIST
            )

        }