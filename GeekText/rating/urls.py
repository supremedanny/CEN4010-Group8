from django.urls import path
from .views import home_view,rating_list,avrating_list,CreateRatingView

app_name = "rating"

urlpatterns = [
    #path('addrating',RatingView.as_view(success_url = '/'), name="add_rating"),
    path('addrating', CreateRatingView.as_view(), name="BookRating.html"),
    path('rating_list', rating_list, name="rating_list.html"),
    path('avrating_list', avrating_list, name="averageratinglist.html"),

]

