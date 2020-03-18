from django.urls import path, include
from . import views
from rest_framework import routers


#Because of using viewsets instead of views, automatically generate the URL conf for our API, by registering the viewsets with a router class.
router=routers.DefaultRouter()
router.register('note', views.NoteViewSet)
urlpatterns =[
    
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

#***************router.urls routes**************
# ^note/$ [name='note-list']
# ^note\.(?P<format>[a-z0-9]+)/?$ [name='note-list']
# ^note/(?P<pk>[^/.]+)/$ [name='note-detail']
# ^note/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='note-detail']
# ^$ [name='api-root']
# ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']