"""project_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# 파일업로드
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('sns/',include('sns.urls')),
]

# dev에서는 꼭 써야 함. (DEBUG='TRUE')
# 배포(DEBUG='False')상태에서는 빈 배열이 들어오는데 += 연산이므로 영향이 없다.
# 꼭 써주는 것이 좋다.
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
