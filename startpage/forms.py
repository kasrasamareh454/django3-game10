
from django.forms import ModelForm

from .models import Quotation , costomer , News , Scots

class QForm(ModelForm) :
    class Meta :
        model = Quotation
        fields = ['Qname' , 'Qcost' , 'Qquota' , 'Qforbuy' , 'Qforsell']

class Cform(ModelForm) :
    class Meta :
        model = costomer
        fields = ['Cbuy']

class Nform(ModelForm) :
    class Meta :
        model = News
        fields = ['newnews' , 'important']

class SForm(ModelForm):
    class Meta:
        model = Scots
        fields = ['scot', 'name']