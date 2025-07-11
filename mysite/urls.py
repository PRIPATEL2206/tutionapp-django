"""
URL configuration for mysite project.

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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from classroom.views import StandardApiView,SubjectApiView, StudentApiView,TestApiView,MarksApiView,AttendanceApiView,UserApiView,MessageApiView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('user/',UserApiView.as_view()),
    # path('student/',StudentApiView.as_view())
]

router = DefaultRouter()
router.register(r'standard',StandardApiView)
router.register(r'subject',SubjectApiView)
router.register(r'student',StudentApiView)
router.register(r'test',TestApiView)
router.register(r'marks',MarksApiView)
router.register(r'attendance',AttendanceApiView)
router.register(r'messages',MessageApiView)

urlpatterns+=router.urls