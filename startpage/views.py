
from django.shortcuts import render , redirect ,get_object_or_404

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

from django.contrib.auth.models import User

from django.db import IntegrityError

from django.contrib.auth import login , logout , authenticate

from django.contrib.auth.decorators import login_required

from .forms import QForm

from .models import Costs , CostsC , Quotation , costomer

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

        costss = Costs.objects.all()

        costssC = CostsC.objects.all()

        quotations = Quotation.objects.all().order_by('-created')[:10]

        sahmM = pickle.load(open("sahmM{}.txt".format(request.user) , "rb"))
            
        sahmC = pickle.load(open("sahmC{}.txt".format(request.user) , "rb"))

        return render(request , 'startpage/main.html' , {'costss' : costss ,'costssC' : costssC , 'quotations' : quotations , 'mojodi' : mojodi , 'sahmM' : sahmM , 'sahmC' : sahmC})

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

            if (quotation.Qname == 'دلار' or quotation.Qname == 'درهم' or quotation.Qname == 'یورو' or quotation.Qname == 'پوند' or quotation.Qname == 'سکه' or quotation.Qname == 'طلا' or quotation.Qname == 'انس' or quotation.Qname == 'آهن' or quotation.Qname == 'مس' or quotation.Qname == 'لاستیک' or quotation.Qname == 'نفت') :

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

                            sahmM = pickle.load(open("sahmM{}.txt".format(quotation.user) , "rb"))

                            sahmM = int(sahmM) - int(quotation.Qforbuy)

                            pickle.dump(sahmM , open("sahmM{}.txt".format(quotation.user) , "wb"))

                            sahmM = int(sahmM) + int(quotation.Qforsell)

                            pickle.dump(sahmM , open("sahmM{}.txt".format(quotation.user) , "wb"))

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