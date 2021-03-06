from django.urls import path 
from users.views import(
    password_change_view,
    registration_view,
    PropertiesView,
    account_update_view,
    account_info_view,
    credit_card_view,
    CardView,
    card_registration_view,
)
    
app_name = "users"

urlpatterns = [
    path('register',registration_view, name="register"),
    path('cardregister',card_registration_view, name="cardregister"),
    path('list', PropertiesView.as_view(), name="list"),
    path('cardlist', CardView.as_view(), name="cardlist"),
    path('<email>/update', account_update_view, name="update"),
    path('<email>/passwordchange', password_change_view, name="change"),
    path('<email>/', account_info_view, name = "info"),
    path('<email>/creditcard', credit_card_view, name="creditcard"),

]

