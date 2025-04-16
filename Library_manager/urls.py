from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Library_manager.views import api_root_view

schema_view = get_schema_view(
   openapi.Info(
      title="Library Management System DRF API",
      default_version='v1',
      description="This project is a Library Management System API designed to streamline the management of a library's resources, including categories, books, authors, and borrowing records. It provides a structured backend using Django and Django Rest Framework (DRF) to handle essential library operations efficiently",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mail.achibhossen@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('', api_root_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'), name='api-root'),
    path('api-auth/', include('rest_framework.urls')),
]
