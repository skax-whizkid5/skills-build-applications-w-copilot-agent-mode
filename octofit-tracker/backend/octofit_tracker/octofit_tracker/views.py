from bson import ObjectId
from bson.errors import InvalidId
from django.http import Http404
from rest_framework import viewsets

from .models import Activity, LeaderboardEntry, Team, User, Workout
from .serializers import (
    ActivitySerializer,
    LeaderboardEntrySerializer,
    TeamSerializer,
    UserSerializer,
    WorkoutSerializer,
)


class ObjectIdLookupMixin:
    """Resolve detail routes by numeric PK first, then Mongo ObjectId."""

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup_value = self.kwargs.get(lookup_url_kwarg)
        model_cls = queryset.model

        try:
            obj = queryset.get(**{self.lookup_field: lookup_value})
            self.check_object_permissions(self.request, obj)
            return obj
        except (model_cls.DoesNotExist, ValueError, TypeError):
            pass

        try:
            object_id = ObjectId(str(lookup_value))
        except (InvalidId, TypeError):
            raise Http404

        obj = queryset.filter(_id=object_id).first()
        if obj is None:
            raise Http404

        self.check_object_permissions(self.request, obj)
        return obj


class TeamViewSet(ObjectIdLookupMixin, viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related('members').all().order_by('name')
    serializer_class = TeamSerializer


class UserViewSet(ObjectIdLookupMixin, viewsets.ModelViewSet):
    queryset = User.objects.select_related('team').all().order_by('name')
    serializer_class = UserSerializer


class ActivityViewSet(ObjectIdLookupMixin, viewsets.ModelViewSet):
    queryset = Activity.objects.select_related('user').all().order_by('-performed_at')
    serializer_class = ActivitySerializer


class LeaderboardViewSet(ObjectIdLookupMixin, viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.select_related('user').all().order_by('rank', '-score')
    serializer_class = LeaderboardEntrySerializer


class WorkoutViewSet(ObjectIdLookupMixin, viewsets.ModelViewSet):
    queryset = Workout.objects.select_related('user').all().order_by('title')
    serializer_class = WorkoutSerializer
