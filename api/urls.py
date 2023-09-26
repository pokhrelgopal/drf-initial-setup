from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from .views import UserViewSet, BlogViewSet, CommentViewSet, CategoryViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("blogs", BlogViewSet, basename="blogs")
router.register("category", CategoryViewSet, basename="category")
router.register("comment", CommentViewSet, basename="comment")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]
urlpatterns += router.urls
