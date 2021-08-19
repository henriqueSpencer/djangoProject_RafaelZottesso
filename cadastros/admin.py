from django.contrib import admin

from .models import Campo, Atividade
# Vou colocar as classes que poderao ser acessadas pela pagina de admin

admin.site.register(Campo)
admin.site.register(Atividade)