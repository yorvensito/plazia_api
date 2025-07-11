from rest_framework.routers import DefaultRouter

from .views import FavoriteViewSet

router = DefaultRouter()
router.register(r"", FavoriteViewSet)

urlpatterns = router.urls
