import random
from django.shortcuts import render, HttpResponse
from django.conf import settings

from django import forms
from app01 import models

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from utils.tencent.sms import send_sms_single

# Create your views here.


def send_sms(request):
    ''' 发送短信 
        ?tpl = login --> 548760
        ?tpl = register --> 548761
    '''
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')
    
    code = random.randrange(1000, 9999)
    res = send_sms_single('18553976920', template_id, [code,])
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])
    
    
class RegisterModelForm(forms.ModelForm):  
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'),])
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    code = forms.CharField(label='验证码')
    
    class Meta:
        model = models.UserInfo
        fields = "__all__"


def register(request):
    '''注册'''
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})