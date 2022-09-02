from django.db import models
from django.utils import timezone


# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=40)
    slug=models.SlugField(unique=True,max_length=50)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(School,self).save(*args,**kwargs)
        return (School.slug)
    
class Person(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=40)
    enrollment_date=models.DateField(default=timezone.now)
    score=models.IntegerField()
    is_succeed=models.BooleanField()
    class Meta:
        verbose_name='Person'
        verbose_name_plural='list Person'

     #ORM
#1
p=Person(first_name="James",last_name="Arthur",email="james@gmail.com",score=43,is_succed=True)
p.save()
	#2
a=Person.objects.create(first_name="Martine",last_name="Moise",email="martine@gmail.com",score=56,is_succed=True)

#3
a.first_name="Jean"
a.last_name="Charles"
a.save()


#6
l=Person.objects.filter(firstname__startwith="L")

#7
v=['a','e','i','o','u','y']
n=""
for i in v: 
    if n ==i:
        n2=Person.objects.filter(firstname__startwith=n)

#8
k=Person.objects.filter(score>=75,score__ORDERBY= DESC)

#13
p3=Person.objects.filter(stock_total=0, score__ORDERBY=ASC)
p3.save()


    
class School2():
    name=models.CharField(max_length=40)
    slug=models.SlugField(unique=True,max_length=50)
    location=models.CharField(max_length=50)
    photo=models.ImageField()
    total_students=models.IntegerField()
    phone=models.NumberField()
    area_code=models.CharField()
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(School,self).save(*args,**kwargs)
        return (School.slug)

	#ORM
    #20
	if (School2.objects.filter(photo.is_empty() or photo.is_not_empty())):
	    School2.objects.all().delete()

    
class Exchange():
    list_money=[
        ("USD","EURO","CAN","HTG")
    ]
    currency_from=models.CharField(max_length=9,choices=list_money)
    currency_to=models.CharField(max_length=9,choices=list_money)
    rate=models.CharField( max_length=50)
    date_created=models.DateField(default=timezone.now)
    date_modified=models.DateTime(default=timezone.now)

    #ORM
#16 li poko fini
p4=Exchange.objects.filter(lis_money[0])
p4.rate='121.40'
p4.save()

#17
p4=Exchange.objects.filter(lis_money[2])
add=p4.rate + 10.00
add.save()
    
    
class Produit():
    category_choices=[
        ("electroniques")
        ("nourriture")
        ("boisson")
    ]
    code=models.IntegerField()
    name=models.CharField(max_length=50)
    category=modesl.models.CharField( max_length=50,choices=category_choices)
    description=models.TextField(max_length=1500)
    photo=models.ImageField()
    price=models.IntegerField(default=0)
    old_price=models.IntegerField()
    is_active=models.CharField(default=True)
    stock_total=models.IntegerField()

    #ORM
#9
k2=Produit.objects.filter(is_active=True)

#10
if (Produit.objects.filter(is_active=False)):
    Produit.objects.all().delete()


#11
p=Produit.objects.filter(old_price)
if p.is_empty():
	p.save()

#12
Produit.objects.filter(description__icontaint="expired")

#14
Produit.objects.filter(category__icontaint="electronique")

#15
p2=Produit.objects.filter(price<100 price=0 ASC)
p2.save()

#18
if (Produit.objects.filter(stock_total=0 photo=0)):
    p5=Produit.objects.filter(is_active="False")
    p5.save()


#19
if (Produit.objects.filter(is_active="False"))
    Produit.objects.all().delete()
	    
	

# Create your models here.


