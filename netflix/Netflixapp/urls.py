from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/Netflix/(?P<pk>[0-9]+)$',
        views.get_delete_update_Netflix,
        name='get_delete_update_Netflix'
    ),
    url(
        r'^api/v1/Netflixapp/$',
        views.get_post_Netflixapp,
        name='get_post_Netflixapp'
    )
]
