"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#media url settings
from django.conf import settings
from django.conf.urls.static import static

# swagger ui settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# set schema view settings
schema_view = get_schema_view(
   openapi.Info(
      title="Pdf Receipt Generator API",
      default_version='v1',
      description="Generate receipt in pdf format based on user input.\
                    You need to first register an account, login with the newly created details,\
                    then use the authentication access token to authorize the receipt endpoints"
                    "\n\nYou can view the generated pdf files in the admin using this credential:\
                    Username: \"Dukka\", Password= \"Dukka123\" "
                    "\n              OR"
                    "\nCopy the pdf url and append it to the url e.g https://receipt-generation-system.herokuapp.com/<receipt url>",
      terms_of_service="https://receipt_generator/policies/terms/",
      contact=openapi.Contact(email="faruqabdulsalam@yahoo.com"),
      license=openapi.License(name="Receipt Generator License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pdf_receipt.urls', namespace="pdf")),
    path('', include('authentication.urls', namespace="auth")),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
