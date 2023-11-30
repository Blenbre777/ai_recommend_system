"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import recommend_system.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/recommend_system/recommend_form/ 추첨 폼
    path("recommend_system/recommend_form/", recommend_system.views.recommend_form),

    # http://127.0.0.1:8000/recommend_system/recommend_proc/ 추천 결과 출력
    path("recommend_system/recommend_proc/", recommend_system.views.recommend_proc),
]