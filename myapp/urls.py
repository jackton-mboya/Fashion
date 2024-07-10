from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('products/', views.products, name='products'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('product-detail', views.product_details, name='product_details'),
]