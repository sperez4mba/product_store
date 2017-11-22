from django.conf.urls import url

from products.api.v1.views import CategoryList, ProductList, \
    ProductUpdate

urlpatterns = [
        url(
                    r'categories/$',
                    CategoryList.as_view()
                ),
        url(
                    r'products/$',
                    ProductList.as_view()
                ),
        url(
                    r'products/(?P<pk>[0-9]+)/$',
                    ProductUpdate.as_view()
                )
]
