from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='')
    slug=models.SlugField()
    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    slug=models.SlugField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField(upload_to='')
    
    book_available=models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.title
class Cart(models.Model):
    cart_id=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    timestamp=models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)

    def __str__(self):
        return self.product.title
    def update_quantity(self,quantity):
        self.quantity+=quantity
        self.save()
    def total(self):
        return self.quantity*self.price
class Buy(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product.title+'_'+str(self.id)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # Add other book details like ISBN, genre, etc.

    def __str__(self):
        return self.title
class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.user.username

class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)
    rent_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} rented {self.book.title}"

class Fine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent = models.OneToOneField(Rent, on_delete=models.CASCADE)
    fine_amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Fine for {self.rent.user}'s rent on {self.rent.book.title}"
        
class Order(models.Model):
    name = models.CharField(max_length=100)

    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name
class TimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

	class Meta:
		abstract = True
class Review(TimeStamp):
	post = models.ForeignKey(Product,on_delete = models.CASCADE)
	review = models.TextField()

	def __str__(self):
		return self.review         