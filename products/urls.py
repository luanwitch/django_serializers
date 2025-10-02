from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('categories.urls')),  # categories
    path('api/', include('api.urls')),         # cursos e alunos
    path('api/', include('products.urls')),    # produtos
    path('api/', include('orders.urls')),      # pedidos
]
