from django.contrib import admin
from mysite.models import Post
from mysite.models import Postdetail,PostdetailTwo

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

class PostdetailAdmin(admin.ModelAdmin):
    list_display=('Bookname','slug','State')

admin.site.register(Post,PostAdmin)
admin.site.register(Postdetail,PostdetailAdmin)