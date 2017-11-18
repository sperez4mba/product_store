from django.conf.urls import url

from products.views import CategoryList

urlpatterns = [
        url(
                    r'categories/$',
                    CategoryList.as_view()
                )
]
