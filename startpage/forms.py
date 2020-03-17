
from django.forms import ModelForm

from .models import Quotation , costomer

class QForm(ModelForm) :
    class Meta :
        model = Quotation
        fields = ['Qname' , 'Qcost' , 'Qquota' , 'Qforbuy' , 'Qforsell']

class Cform(ModelForm) :
    class Meta :
        model = costomer
        fields = ['Cbuy']

# class Nform(ModelForm) :
#     class Meta :
#         model = News
#         fields = ['newnews']