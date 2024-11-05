from django.contrib import admin
from .models import *
from django.contrib import admin

#class CidadeInline(admin.TabularInline):
#    model = Cidade
#    extra = 1
#
#class UFAdmin(admin.ModelAdmin):
#    inlines = [CidadeInline]
#admin.site.register(UF, UFAdmin)

admin.site.register(Cidade)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Genero)
admin.site.register(UF)
admin.site.register(User)
admin.site.register(Emprestimo)