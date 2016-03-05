from django.contrib import admin


from .models import Perfil

class PostModelAdmin(admin.ModelAdmin):	
	class Meta:
		model = Perfil

admin.site.register(Perfil, PostModelAdmin)
