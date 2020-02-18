from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',views.product_data),
    path('products/<int:id>/',views.get_product),
    path('products/add/',views.add_product),
    path('products/paginated/<int:page_num>/<int:num_data>',views.product_objects_pagination),
    path('products/change/<int:id>/',views.update_api_data),
    ]
