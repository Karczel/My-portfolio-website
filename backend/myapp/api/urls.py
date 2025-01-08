from rest_framework import routers
from .views import *

myapp_router = routers.DefaultRouter()

myapp_router.register(r'owners', OwnerViewSet)
myapp_router.register(r'activities', ActivityViewSet)
myapp_router.register(r'contacts', ContactViewSet)
myapp_router.register(r'illustrations', IllustrationViewSet)
myapp_router.register(r'pseudo_names', PseudoNameViewSet)
myapp_router.register(r'repositories', RepositoryViewSet)
myapp_router.register(r'skills', SkillViewSet)
myapp_router.register(r'tags', TagViewSet)
myapp_router.register(r'videos', VideoViewSet)

myapp_router.register(r'activity_images', ActivityImageViewSet)
myapp_router.register(r'repository_images', RepositoryImageViewSet)
myapp_router.register(r'illustration_tags', IllustrationTagViewSet)
myapp_router.register(r'repository_tags', RepositoryTagViewSet)
myapp_router.register(r'video_tags', VideoTagViewSet)
