from django import forms
from rbac import models

class RoleModelForm(forms.ModelForm):
    """
    角色表单
    """
    class Meta:
        model = models.Role
        fields = ['title']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'})
        }