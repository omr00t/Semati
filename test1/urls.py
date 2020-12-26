from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:test_id>/', views.take_test, name='take_test'),
    path('show/', views.show_result, name='show_result'),
]
