from django.contrib import admin
from django.contrib.auth.views import LogoutView

from posts.views import LoginView, RegisterView, guest_register_view
from posts.views import checkout_address_create_view, chekout_address_reuse_view
from posts.views import cart_detail_api_view

from .views import home_page, about_page, contact_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', chekout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^products/', include("products.urls")
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^admin/', admin.site.urls),
    ]