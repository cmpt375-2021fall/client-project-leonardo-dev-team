from django.contrib import admin
from .models import Post
from .models import Calender
from .models import Newsletter
from .models import MembershipInfo
# Register your models here.

admin.site.register(Post)
admin.site.register(Calender)
admin.site.register(Newsletter)
admin.site.register(MembershipInfo)
