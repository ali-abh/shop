from django.contrib import admin
from makeup.models import Shop
from makeup.models import User
from makeup.models import Makeup
from makeup.models import Skincare
from makeup.models import Sell
from makeup.models import Digitalstuff

# Register your models here.

admin.site.register(Shop)
admin.site.register(User)
admin.site.register(Makeup)
admin.site.register(Skincare)
admin.site.register(Digitalstuff)
admin.site.register(Sell)