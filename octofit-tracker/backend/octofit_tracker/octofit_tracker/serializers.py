from bson import ObjectId
from bson.errors import InvalidId
from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, User, Workout


class PkOrObjectIdRelatedField(serializers.PrimaryKeyRelatedField):
    """Accept relational IDs as either numeric PK or Mongo ObjectId string."""

    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except serializers.ValidationError:
            pass

        if isinstance(data, str):
            try:
                object_id = ObjectId(data)
            except (InvalidId, TypeError):
                raise serializers.ValidationError('유효한 PK 또는 ObjectId를 입력하세요.')

            instance = self.get_queryset().filter(_id=object_id).first()
            if instance is not None:
                return instance

        raise serializers.ValidationError('유효한 PK 또는 ObjectId를 입력하세요.')


class ObjectIdStringMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        mongo_object_id = getattr(instance, '_id', None)
        if mongo_object_id is not None:
            data['object_id'] = str(mongo_object_id)
        else:
            data['object_id'] = str(getattr(instance, 'id', ''))

        for key, value in data.items():
            if value is None:
                continue
            if key == 'id' or key in {'user', 'team'} or key.endswith('_id'):
                data[key] = str(value)
        return data


class TeamSerializer(ObjectIdStringMixin, serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('id',)


class UserSerializer(ObjectIdStringMixin, serializers.ModelSerializer):
    team = PkOrObjectIdRelatedField(queryset=Team.objects.all(), allow_null=True, required=False)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)


class ActivitySerializer(ObjectIdStringMixin, serializers.ModelSerializer):
    user = PkOrObjectIdRelatedField(queryset=User.objects.all())

    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ('id', 'performed_at')


class LeaderboardEntrySerializer(ObjectIdStringMixin, serializers.ModelSerializer):
    user = PkOrObjectIdRelatedField(queryset=User.objects.all())

    class Meta:
        model = LeaderboardEntry
        fields = '__all__'
        read_only_fields = ('id',)


class WorkoutSerializer(ObjectIdStringMixin, serializers.ModelSerializer):
    user = PkOrObjectIdRelatedField(queryset=User.objects.all())

    class Meta:
        model = Workout
        fields = '__all__'
        read_only_fields = ('id',)
