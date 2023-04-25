from django.urls import path
from user import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView,

)

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user_detail_view')
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
