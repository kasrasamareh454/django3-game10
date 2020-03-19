
from django.shortcuts import render , redirect ,get_object_or_404

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

from django.contrib.auth.models import User

from django.db import IntegrityError

from django.contrib.auth import login , logout , authenticate

from django.contrib.auth.decorators import login_required

from .forms import QForm , Nform , SForm

from .models import Costs , CostsC , Quotation , costomer , News , Scots

import random

import pickle

# Create your views here.

l = []

def signupuser(request) :

    if (request.method == 'GET') :
        return render(request , 'startpage/signupuser.html' , {'form' : UserCreationForm()})

    else :
        if (request.POST['password1'] == request.POST['password2']) :
            try :
                user = User.objects.create_user(request.POST['username'] , password=request.POST['password1'])
                user.save()
                login(request , user)
                mojodi = 500000000
                pickle.dump(mojodi , open("{}.txt".format(request.user) , "wb"))
                sahmM = 0
                pickle.dump(sahmM , open("sahmM{}.txt".format(request.user) , "wb"))
                sahmC = 0
                pickle.dump(sahmC , open("sahmC{}.txt".format(request.user) , "wb"))

                a = request.user

                a = str(a)
                
                sahm_khD = 0
                pickle.dump(sahm_khD , open("sahm_kh{}.txt".format(a+'Dollar') , "wb"))

                sahm_khE = 0
                pickle.dump(sahm_khE , open("sahm_kh{}.txt".format(a+'Euro') , "wb"))

                sahm_khP = 0
                pickle.dump(sahm_khP , open("sahm_kh{}.txt".format(a+'Pound') , "wb"))

                sahm_khS = 0
                pickle.dump(sahm_khS , open("sahm_kh{}.txt".format(a+'Seke') , "wb"))

                sahm_khT = 0
                pickle.dump(sahm_khT , open("sahm_kh{}.txt".format(a+'Tala') , "wb"))
                return redirect('loginuser')
            except IntegrityError :
                return render(request , 'startpage/signupuser.html' , {'form' : UserCreationForm() , 'error' : '🤯نام کاربری تکراری است'})

        else :
            return render(request , 'startpage/signupuser.html' , {'form' : UserCreationForm() , 'error' : '🤯پسورد ها یکسان نیستند'})

def logoutuser(request) :
    if (request.method=='POST') :
        logout(request)
        return redirect('start')

def loginuser(request) :
    global user
    if (request.method == 'GET') :
        return render(request , 'startpage/loginuser.html' , {'form' : AuthenticationForm()})

    else :
        user = authenticate(request , username=request.POST['username'] , password=request.POST['password'])
        if (user is None) :
            return render(request , 'startpage/loginuser.html' , {'form' : AuthenticationForm() , 'error' : '🤯نام کاربری و یا کلمه عبور اشتباه است'})
        else :
            login(request , user)
            return redirect('mainpage')








def start(request) :

    return render(request , 'startpage/start.html')

@login_required

def mainpage(request) :

    try :

        #mojodi = 500000000

        #pickle.dump(mojodi , open("{}.txt".format(user) , "wb"))

        mojodi = pickle.load(open("{}.txt".format(request.user) , "rb"))

        news = News.objects.all()

        costss = Costs.objects.all()

        costssC = CostsC.objects.all()

        quotations = Quotation.objects.all().order_by('-created')

        sahmM = pickle.load(open("sahmM{}.txt".format(request.user) , "rb"))
            
        sahmC = pickle.load(open("sahmC{}.txt".format(request.user) , "rb"))

        a = request.user

        a = str(a)

        sahm_khD = pickle.load(open("sahm_kh{}.txt".format(a+'Dollar') , "rb"))

        sahm_khE = pickle.load(open("sahm_kh{}.txt".format(a+'Euro') , "rb"))

        sahm_khP = pickle.load(open("sahm_kh{}.txt".format(a+'Pound') , "rb"))

        sahm_khS = pickle.load(open("sahm_kh{}.txt".format(a+'Seke') , "rb"))

        sahm_khT = pickle.load(open("sahm_kh{}.txt".format(a+'Tala') , "rb"))

        return render(request , 'startpage/main.html' , {'costss' : costss ,'costssC' : costssC , 'quotations' : quotations , 'news' : news , 'mojodi' : mojodi , 'sahmM' : sahmM , 'sahmC' : sahmC , 'sahm_khD' : sahm_khD , 'sahm_khE' : sahm_khE , 'sahm_khP' : sahm_khP , 'sahm_khS' : sahm_khS , 'sahm_khT' : sahm_khT})

    except :

        return redirect('start')

@login_required

def Qquotation(request) :
    # quotations = Quotation.objects.all()
    if (request.method=='GET') :
         return render(request , 'startpage/Qquotation.html' , {'form' : QForm()})
    else :
        try :
            form = QForm(request.POST)
            newc = form.save(commit=False)
            newc.user = request.user
            newc.save()
            return redirect('mainpage')
            # for quotation in quotations :
            #     if (request.POST.get(Qname)) :

            #         sahmM = pickle.load(open("sahmM{}.txt".format(user) , "rb"))

            #         sahmM = int(sahmM) - int(quotation.Qquota)

            #         pickle.dump(sahmM , open("sahmM{}.txt".format(user) , "wb"))
                    
            #         return redirect('mainpage')
                # else :
                #     return render(request , 'startpage/Qquotation.html' , {'form' : QForm() , 'error' : '🤯داده وارد شده صحیح نمی باشد'})
        except ValueError :
            return render(request , 'startpage/Qquotation.html' , {'form' : QForm() , 'error' : '🤯داده وارد شده صحیح نمی باشد'})

@login_required

def extra(request) :
    costss = Costs.objects.all()
    #mojodi = 500000000
    mojodi = pickle.load(open("{}.txt".format(request.user) , "rb"))
    for cost in costss :
        if (request.POST.get(cost.name)) :
            #mojodi = cost.mojodi
            mojodi = mojodi - int((cost.cost))
            if (int(mojodi) < 0) :
                mojodi = mojodi + int((cost.cost))
                return redirect('mainpage')
            else :
                pickle.dump(mojodi , open("{}.txt".format(request.user) , "wb"))
                sahmM = cost.sahmmarket
                pickle.dump(sahmM , open("sahmM{}.txt".format(request.user) , "wb"))
                cost.delete()
                return redirect('mainpage')
                #sahmC = cost.sahmcompany
                #pickle.dump(sahmC , open("sahmC{}.txt".format(user) , "wb"))
        else :
            continue
    return redirect('mainpage')
    #return render(request , 'startpage/main.html' , {'mojodi' : mojodi})
    #mojodi = mojodi - (int(request.POST['num1']) + int(request.POST['num2']))

@login_required

def extraC(request) :
    costssC = CostsC.objects.all()
    #mojodi = 500000000
    mojodi = pickle.load(open("{}.txt".format(request.user) , "rb"))
    for costC in costssC :
        if (request.POST.get(costC.name)) :
            #mojodi = cost.mojodi
            mojodi = mojodi - int((costC.cost))
            if (int(mojodi) < 0) :
                mojodi = mojodi + int((costC.cost))
                return redirect('mainpage')
            else :
                pickle.dump(mojodi , open("{}.txt".format(request.user) , "wb"))
                sahmC = costC.sahmcompany
                pickle.dump(sahmC , open("sahmC{}.txt".format(request.user) , "wb"))
                costC.delete()
                return redirect('mainpage')
        else :
            continue
    return redirect('mainpage')
    #return render(request , 'startpage/main.html' , {'mojodi' : mojodi})


def quotationforedit(request , quotation_pk) :

    quotation = get_object_or_404(Quotation , pk=quotation_pk)

    if request.method=='GET' :

        form = QForm(instance=quotation)

        return render (request , 'startpage/quotationforedit.html' , {'quotation' : quotation , 'form' : form})

    else :
        try :

            form = QForm(request.POST , instance=quotation)
            
            form.save()

            #costssC = CostsC.objects.all()

            if (quotation.Qname == 'دلار' or quotation.Qname == 'یورو' or quotation.Qname == 'پوند' or quotation.Qname == 'سکه' or quotation.Qname == 'طلا') :

                if (int(quotation.Qforbuy) < 0) :

                    quotation.Qforbuy = 0

                    quotation.Qforsell = 0

                    form.save()

                    return redirect('mainpage')
                
                else :

                    pass

                if (int(quotation.Qforsell) < 0) :

                    quotation.Qforsell = 0

                    quotation.Qforsell = 0

                    form.save()

                    return redirect('mainpage')
                
                else :

                    pass

                quotation.Qquota = int(quotation.Qquota) - int(quotation.Qforbuy)

                if (int(quotation.Qquota) < 0) :

                    quotation.Qquota = int(quotation.Qquota) + int(quotation.Qforbuy)

                    quotation.Qforbuy = 0

                    quotation.Qforsell = 0

                    form.save()

                    return render(request, 'startpage/quotationforedit.html', {'quotation': quotation, 'form':form, 'error':'😁میزان سهم موجود کمتر از مقدار انتخابی شماست'})

                else :

                    form.save()

                    mojodi = pickle.load(open("{}.txt".format(quotation.user) , "rb"))

                    mojodi = mojodi + (int(quotation.Qforbuy)*int(quotation.Qcost)) - (int(quotation.Qforsell)*int(quotation.Qcost))

                    if (int(mojodi) < 0) :
                        return render(request, 'startpage/quotationforedit.html', {'quotation': quotation, 'form':form, 'error':'☹️موجودی مارکت دار مورد نظر کافی نمی باشد'})
                    else :
                        pickle.dump(mojodi , open("{}.txt".format(quotation.user) , "wb"))

                        mojodi = pickle.load(open("{}.txt".format(request.user) , "rb"))

                        mojodi = mojodi - (int(quotation.Qforbuy)*int(quotation.Qcost)) + int(quotation.Qforsell)*int(quotation.Qcost)

                        if (mojodi < 0) :

                            mojodi = pickle.load(open("{}.txt".format(quotation.user) , "rb"))

                            mojodi = mojodi - (int(quotation.Qforbuy)*int(quotation.Qcost)) + (int(quotation.Qforsell)*int(quotation.Qcost))

                            pickle.dump(mojodi , open("{}.txt".format(quotation.user) , "wb"))

                            mojodi = pickle.load(open("{}.txt".format(request.user) , "rb"))

                            mojodi = mojodi - (int(quotation.Qforbuy)*int(quotation.Qcost)) + int(quotation.Qforsell)*int(quotation.Qcost)

                            mojodi = mojodi + (int(quotation.Qforbuy)*int(quotation.Qcost)) - int(quotation.Qforsell)*int(quotation.Qcost)

                            quotation.Qquota = int(quotation.Qquota) + int(quotation.Qforbuy)

                            quotation.Qforbuy = 0
                            
                            quotation.Qforsell = 0

                            form.save()

                            return render(request, 'startpage/quotationforedit.html', {'quotation': quotation, 'form':form, 'error':'☹️موجودی شما کافی نمی باشد'})

                        else :

                            pickle.dump(mojodi , open("{}.txt".format(request.user) , "wb"))

                            sahmM = pickle.load(open("sahmM{}.txt".format(quotation.user) , "rb"))

                            sahmM = int(sahmM) - int(quotation.Qforbuy)

                            pickle.dump(sahmM , open("sahmM{}.txt".format(quotation.user) , "wb"))

                            sahmM = int(sahmM) + int(quotation.Qforsell)

                            pickle.dump(sahmM , open("sahmM{}.txt".format(quotation.user) , "wb"))

                            if (quotation.Qname == 'دلار') :
                                sahm_khD = pickle.load(open("sahm_kh{}.txt".format(str(request.user)+'Dollar') , "rb"))
                                sahm_khD = int(sahm_khD) + int(quotation.Qforbuy)
                                pickle.dump(sahm_khD , open("sahm_kh{}.txt".format(str(request.user)+'Dollar') , "wb"))
                            
                            elif (quotation.Qname == 'یورو') :
                                sahm_khE = pickle.load(open("sahm_kh{}.txt".format(str(request.user)+'Euro') , "rb"))
                                sahm_khE = int(sahm_khE) + int(quotation.Qforbuy)
                                pickle.dump(sahm_khE , open("sahm_kh{}.txt".format(str(request.user)+'Euro') , "wb"))

                            elif (quotation.Qname == 'پوند') :
                                sahm_khP = pickle.load(open("sahm_kh{}.txt".format(str(request.user)+'Pound') , "rb"))
                                sahm_khP = int(sahm_khP) + int(quotation.Qforbuy)
                                pickle.dump(sahm_khP , open("sahm_kh{}.txt".format(str(request.user)+'Pound') , "wb"))

                            elif (quotation.Qname == 'سکه') :
                                sahm_khS = pickle.load(open("sahm_kh{}.txt".format(str(request.user)+'Seke') , "rb"))
                                sahm_khS = int(sahm_khS) + int(quotation.Qforbuy)
                                pickle.dump(sahm_khS , open("sahm_kh{}.txt".format(str(request.user)+'Seke') , "wb"))

                            elif (quotation.Qname == 'طلا') :
                                sahm_khT = pickle.load(open("sahm_kh{}.txt".format(str(request.user)+'Tala') , "rb"))
                                sahm_khT = int(sahm_khT) + int(quotation.Qforbuy)
                                pickle.dump(sahm_khT , open("sahm_kh{}.txt".format(str(request.user)+'Tala') , "wb"))
                            
                            quotation.Qforbuy = 0

                            quotation.Qforsell = 0

                            form.save()

                            return redirect('mainpage')

            elif (quotation.Qname == 'ماکروسافت' or quotation.Qname == 'اپل' or quotation.Qname == 'سامسونگ' or quotation.Qname == 'بنز' or quotation.Qname == 'بی ام و' or quotation.Qname == 'تیوتا' or quotation.Qname == 'فورد' or quotation.Qname == 'سونی' or quotation.Qname == 'نایک') :

                if (int(quotation.Qforbuy) < 0) :

                    quotation.Qforbuy = 0

                    quotation.Qforsell = 0

                    form.save()

                    return redirect('mainpage')
                
                else :

                    pass

                if (int(quotation.Qforsell) < 0) :

                    quotation.Qforsell = 0

                    quotation.Qforsell = 0

                    form.save()

                    return redirect('mainpage')
                
                else :

                    pass

                quotation.Qquota = int(quotation.Qquota) - int(quotation.Qforbuy)

                if (int(quotation.Qquota) < 0) :

                    quotation.Qquota = int(quotation.Qquota) + int(quotation.Qforbuy)

                    quotation.Qforbuy = 0

                    quotation.Qforsell = 0

                    form.save()

                    return redirect('mainpage')

                else :

                    form.save()

                    mojodi = pickle.load(open("{}.txt".format(quotation.user) , "rb"))

                    mojodi = mojodi + (int(quotation.Qforbuy)*int(quotation.Qcost)) - (int(quotation.Qforsell)*int(quotation.Qcost))

                    if (int(mojodi) < 0) :
                        return render(request, 'startpage/quotationforedit.html', {'quotation': quotation, 'form':form, 'error':'☹️موجودی مارکت دار مورد نظر کافی نمی باشد'})
                    else :
                        pickle.dump(mojodi , open("{}.txt".format(quotation.user) , "wb"))

                        mojodi = pickle.load(open("{}.txt".format(request.user) , "rb"))

                        mojodi = mojodi - (int(quotation.Qforbuy)*int(quotation.Qcost)) + int(quotation.Qforsell)*int(quotation.Qcost)

                        if (mojodi < 0) :

                            mojodi = pickle.load(open("{}.txt".format(quotation.user) , "rb"))

                            mojodi = mojodi - (int(quotation.Qforbuy)*int(quotation.Qcost)) + (int(quotation.Qforsell)*int(quotation.Qcost))

                            pickle.dump(mojodi , open("{}.txt".format(quotation.user) , "wb"))

                            mojodi = pickle.load(open("{}.txt".format(request.user) , "rb"))

                            mojodi = mojodi - (int(quotation.Qforbuy)*int(quotation.Qcost)) + int(quotation.Qforsell)*int(quotation.Qcost)

                            mojodi = mojodi + (int(quotation.Qforbuy)*int(quotation.Qcost)) - int(quotation.Qforsell)*int(quotation.Qcost)

                            quotation.Qquota = int(quotation.Qquota) + int(quotation.Qforbuy)

                            quotation.Qforbuy = 0
                            
                            quotation.Qforsell = 0

                            form.save()

                            return render(request, 'startpage/quotationforedit.html', {'quotation': quotation, 'form':form, 'error':'☹️موجودی شما کافی نمی باشد'})

                        else :

                            pickle.dump(mojodi , open("{}.txt".format(request.user) , "wb"))

                            sahmC = pickle.load(open("sahmC{}.txt".format(quotation.user) , "rb"))

                            sahmC = int(sahmC) - int(quotation.Qforbuy)

                            pickle.dump(sahmC , open("sahmC{}.txt".format(quotation.user) , "wb"))

                            sahmC = int(sahmC) + int(quotation.Qforsell)

                            pickle.dump(sahmC , open("sahmC{}.txt".format(quotation.user) , "wb"))

                            quotation.Qforbuy = 0

                            quotation.Qforsell = 0

                            form.save()

                            return redirect('mainpage')
                
            else :

                return render(request, 'startpage/quotationforedit.html', {'quotation': quotation, 'form':form, 'error':'🤯نام مارکت یا شرکت وارد شده صحیح نمی باشد'})
                
        except  ValueError:

            return render(request, 'startpage/quotationforedit.html', {'quotation': quotation, 'form':form, 'error':'🤯داده وارد شده صحیح نمی باشد'})

@login_required
def newsnews(request , news_pk) :
    
    new = get_object_or_404(News , pk=news_pk)

    if request.method=='GET' :

        form = Nform(instance=new)

        return render (request , 'startpage/createnews.html' , {'new' : new , 'form' : form})
    else :
        try :
            form = Nform(request.POST , instance=new)
            
            form.save()

            return redirect('mainpage')
        
        except ValueError :
            return render(request, 'startpage/createnews.html', {'new': new, 'form':form, 'error':'🤯داده وارد شده صحیح نمی باشد'})

@login_required

def createnews(request) :
    
    if (request.method == 'GET') :
        
     return render(request , 'startpage/createnews.html' , {'form' : Nform()})

    else:

        try :
        
            form = Nform(request.POST)

            # newcreatenews = form.save(commit=False)

            # newcreatenews.user = request.user

            # newcreatenews.save()

            form.save()

            return redirect('mainpage')
 
        except ValueError :
            
            return render(request , 'startpage/createnews.html' , {'form' : Nform() , 'error' : '🤯داده وارد شده صحیح نمی باشد'})


# def quotationforedit(request , quotation_pk) :

#     quotation = get_object_or_404(Quotation , pk=quotation_pk)

#     if request.method=='GET' :

#         form = QForm(instance=quotation)

#         return render (request , 'startpage/quotationforedit.html' , {'quotation' : quotation , 'form' : form})

#     else :
#         try :

#             form = QForm(request.POST , instance=quotation)

#             form.save()

#             return redirect('mainpage')
        
#         except  ValueError:

#              return render(request, 'startpage/quotationforedit.html', {'quotation': quotation, 'form':form, 'error':'🤯داده وارد شده صحیح نمی باشد'})


def scotpage(request) :
    scots = Scots.objects.filter(user=request.user)
    if (request.method == 'GET') :

        return render(request , 'startpage/scotpage.html' , {'form' : SForm()})
    
    else :
        form = SForm(request.POST)

        newscotform = form.save(commit=False)

        newscotform.user = request.user

        newscotform.save()

        for scot in scots :
            mojodi = pickle.load(open("{}.txt".format(request.user) , "rb"))
            mojodi = mojodi - scot.scot
            if (mojodi < 0) :
                mojodi = mojodi + scot.scot
                pickle.dump(mojodi , open("{}.txt".format(request.user) , "wb"))
                scot.scot = 0
                return render(request, 'startpage/scotpage.html', {'scots': scots , 'form':form, 'error':'☹️موجودی شما کافی نمی باشد'})
            else :
                pickle.dump(mojodi , open("{}.txt".format(request.user) , "wb"))
                mojodi = pickle.load(open("{}.txt".format(scot.name) , "rb"))
                mojodi = mojodi + scot.scot
                pickle.dump(mojodi , open("{}.txt".format(scot.name) , "wb"))
                scot.scot = 0
                return redirect('mainpage')