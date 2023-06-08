from django.urls import include, path
from rest_framework import routers
from incident.views import IncidentViewSet
from .views import UserRegistrationView, UserLoginView

router = routers.DefaultRouter()
router.register(r'incidents', IncidentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/users/register', UserRegistrationView.as_view(), name='user-registration'),
    path('api/users/login', UserLoginView.as_view(), name='user-login'),
]
