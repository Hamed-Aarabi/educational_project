from django.urls import path, re_path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.CartDetailView.as_view(), name='detail'),
    re_path(r'add/(?P<slug>[-\w]+)', views.AddToCartView.as_view(), name='add-item'),
    path('remove/<str:id>', views.RemoveFromCartView.as_view(), name='remove-item'),
    path('order/create', views.OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/peyment', views.PaymentView.as_view(), name='order-payment'),
]
