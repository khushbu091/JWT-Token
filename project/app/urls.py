from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# import routers
from rest_framework import routers 
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'car', CarViewSet)



  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # this line is used to create login & logout feature in DRF window.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]