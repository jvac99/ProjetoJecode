from django.contrib import admin

from .models import Projeto
from .models import Lista
from .models import Atividade
from .models import Subatividade

admin.site.register(Projeto)
admin.site.register(Lista)
admin.site.register(Atividade)
admin.site.register(Subatividade)

# Register your models here.
