from django.contrib import admin
from .models import Person, Entry, Author, Blog

admin.site.register(Person)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)