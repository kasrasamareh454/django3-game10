
from django.db import models
from django.contrib.auth.models import User
import os
import pickle



class Costs(models.Model) :
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    sahmmarket = models.CharField(max_length=100 , blank=True , default=100)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    # mypath ="C:/Users/Asus Pc/Desktop/Django/game2/startpage/static/startpage"
    # if not os.path.exists(mypath):
    #     os.makedirs(mypath, 755)
    #     #print("Path is created")
    # fname = mypath + "/" + "{}.dat".format(user)
    # with open(fname,"wb") as x:
    #     pickle.dump(mojodi, x)
    #mojodi = pickle.load(open("{}.txt".format(User) , "rb"))
    #mojodi = 500000000
    #pickle.dump(mojodi , open("d.txt" , "wb"))
    
    def __str__(self) :
        return self.name

class CostsC(models.Model) :
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    sahmcompany = models.CharField(max_length=100 , blank=True , default=100)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    # mypath ="C:/Users/Asus Pc/Desktop/Django/game2/startpage/static/startpage"
    # if not os.path.exists(mypath):
    #     os.makedirs(mypath, 755)
    #     #print("Path is created")
    # fname = mypath + "/" + "{}.dat".format(user)
    # with open(fname,"wb") as x:
    #     pickle.dump(mojodi, x)
    #mojodi = pickle.load(open("{}.txt".format(User) , "rb"))
    #mojodi = 500000000
    #pickle.dump(mojodi , open("d.txt" , "wb"))
    
    def __str__(self) :
        return self.name

class Quotation(models.Model) :
    Qname = models.CharField(max_length=40)
    Qcost = models.IntegerField(null=True , blank=True)
    Qquota = models.IntegerField(null=True , blank=True)
    Qforbuy = models.IntegerField(null=True , default=0)
    Qforsell = models.IntegerField(null=True , default=0)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # mypath ="C:/Users/Asus Pc/Desktop/Django/game2/startpage/static/startpage"
    # if not os.path.exists(mypath):
    #     os.makedirs(mypath, 755)
    #     #print("Path is created")
    # fname = mypath + "/" + "{}.dat".format(user)
    # with open(fname,"wb") as x:
    #     pickle.dump(mojodi, x)
    #mojodi = pickle.load(open("{}.txt".format(User) , "rb"))
    #mojodi = 500000000
    #pickle.dump(mojodi , open("d.txt" , "wb"))
    
    def __str__(self) :
        return self.Qname

class costomer(models.Model) :

    Cbuy = models.IntegerField(null=True , default=0)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class Balances(models.Model) :

    mojodi = models.IntegerField(default=500000000)

    sahmM = models.IntegerField(default=0)

    sahmC = models.IntegerField(default=0)
    
    user = models.ForeignKey(User , on_delete=models.CASCADE)

# class News(models.Model) :

#     newnews = models.TextField(blank=True)
    
#     user = models.ForeignKey(User , on_delete=models.CASCADE)