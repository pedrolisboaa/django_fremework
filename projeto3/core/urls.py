from django.urls import path
from .views import index

from django.conf.urls import handler404, handler500


urlpatterns = [
    path('', index, name='index')
]

handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'
