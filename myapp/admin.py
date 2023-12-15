from django.contrib import admin
from myapp.models import Product,Cart,Buy,Review,Category,Rent,Fine,Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Buy)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Rent)
admin.site.register(Fine)
admin.site.register(Order)