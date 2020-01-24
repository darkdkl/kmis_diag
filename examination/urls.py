from rest_framework.routers import DefaultRouter
from .views import DiagnosticsViewSet

router = DefaultRouter()
router.register(r'diag', DiagnosticsViewSet)
urlpatterns = router.urls
