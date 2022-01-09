from django.contrib import admin
from .models import Quadro
from .models import Linha
from .models import Coluna
from .models import Status
from .models import Tipo
from .models import Epico
from .models import Atividade

admin.site.register(Quadro)
admin.site.register(Linha)
admin.site.register(Coluna)
admin.site.register(Status)
admin.site.register(Tipo)
admin.site.register(Epico)
admin.site.register(Atividade)