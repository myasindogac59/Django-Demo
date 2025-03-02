from django.urls import path
from .views import(
  about_us,
  contact_us,
  home,
  vision_us,
)
urlpatterns = [
    path('', home, name = "home"),
    path('about_us/', about_us, name = "about"),
    path('contact/', contact_us, name = "contact"),
    path('vision/', vision_us, name = "vision"),
]