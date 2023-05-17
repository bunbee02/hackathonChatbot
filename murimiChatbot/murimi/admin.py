from django.contrib import admin
from .models import Province, Crop, Practice,Product
from .models import info

admin.site.register(Province)
admin.site.register(Crop)
admin.site.register(Practice)
admin.site.register(Product)
admin.site.register(info)

