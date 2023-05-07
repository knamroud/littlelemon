from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    # path("about", views.about, name="about"),
    path("api/book", views.BookingView.as_view(), name="book"),
    path("api/menu", views.MenuItemView.as_view(), name="menu"),
    path("api/menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu_item"),
]
