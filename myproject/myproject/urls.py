"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
#import settings
from django.conf.urls import static
from makeup.views import Shops,shop_details,allposts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops', Shops),
    path('details/<int:shop_id>/', shop_details, name='post_detail'),
    path('main/page', allposts),
    # path('comments/<int:post_id>/', makeup_comments),
    # path('comments/<int:pk_id>/', skincare_comments),
    # path('comments/<int:p_id>/', digitalstuf_comments),

]
#if settings.DEBUGP:
#    urlpatterns +=static(settings.MEDIA_URL,ducument_root=settings.MEDIA_ROOT)
