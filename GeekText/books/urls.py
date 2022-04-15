from django.urls import include, path
from rest_framework import routers
from . import views
from .views import GenreFilter, SalesFilter, RatingsFilter, IDFilter

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('search/genre/', GenreFilter.as_view(), name='Genre Filter'),
    path('search/sales/', SalesFilter.as_view(), name='Top Sellers'),
    path('search/rating/', RatingsFilter.as_view(), name='Ratings'),
    path('search/id/', IDFilter.as_view(), name='ID Filter')
]