from django.urls import include, path
from rest_framework import routers
from .views import MedicamentosViewSet

router = routers.DefaultRouter()
router.register(r'', MedicamentosViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
