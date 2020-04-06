from django.contrib import admin
from travello_app.models import Book, Lang, Instance, Artist, Genre, Album, Track

# Register your models here.

admin.site.register(Book)
admin.site.register(Lang)
admin.site.register(Instance)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)