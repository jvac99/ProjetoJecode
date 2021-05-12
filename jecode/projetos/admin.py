from django.contrib import admin

from .models import Projeto
from .models import Lista
from .models import Atividade

admin.site.register(Projeto)
admin.site.register(Lista)
admin.site.register(Atividade)

# Register your models here.
