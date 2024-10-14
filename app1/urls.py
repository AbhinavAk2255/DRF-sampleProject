from django.urls import path
from .views import PersonsView,PersonViewset,LoginView,RegisterView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person_list', PersonViewset)

urlpatterns = [
    path('person/', PersonsView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view())

]+router.urls