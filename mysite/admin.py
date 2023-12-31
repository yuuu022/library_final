from django.contrib import admin
from mysite import models 
from mysite.models import Post,Postdetail,PostdetailTwo

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

class PostdetailAdmin(admin.ModelAdmin):
    list_display=('Bookname','slug','State')

admin.site.register(Post,PostAdmin)
admin.site.register(Postdetail,PostdetailAdmin)
admin.site.register(models.User)