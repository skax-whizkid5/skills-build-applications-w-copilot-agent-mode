import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from .views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    UserViewSet,
    WorkoutViewSet,
)

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = 'http://localhost:8000'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('teams', TeamViewSet, basename='teams')
router.register('activities', ActivityViewSet, basename='activities')
router.register('leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register('workouts', WorkoutViewSet, basename='workouts')


@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'users': f'{base_url}/api/users/',
            'users_detail': f'{base_url}/api/users/<id-or-objectid>/',
            'teams': f'{base_url}/api/teams/',
            'teams_detail': f'{base_url}/api/teams/<id-or-objectid>/',
            'activities': f'{base_url}/api/activities/',
            'activities_detail': f'{base_url}/api/activities/<id-or-objectid>/',
            'leaderboard': f'{base_url}/api/leaderboard/',
            'leaderboard_detail': f'{base_url}/api/leaderboard/<id-or-objectid>/',
            'workouts': f'{base_url}/api/workouts/',
            'workouts_detail': f'{base_url}/api/workouts/<id-or-objectid>/',
        }
    )

urlpatterns = [
    path('', api_root, name='root-api'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
