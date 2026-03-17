from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, User, Workout


class ObjectIdAdminMixin:
    readonly_fields = ('object_id',)

    @admin.display(description='ObjectId')
    def object_id(self, obj):
        return str(getattr(obj, '_id', ''))


@admin.register(Team)
class TeamAdmin(ObjectIdAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'object_id', 'name', 'universe')
    search_fields = ('name', 'universe')


@admin.register(User)
class UserAdmin(ObjectIdAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'object_id', 'name', 'email', 'team', 'total_points')
    list_filter = ('team',)
    search_fields = ('name', 'email')


@admin.register(Activity)
class ActivityAdmin(ObjectIdAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'object_id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'performed_at')
    list_filter = ('activity_type',)
    search_fields = ('user__name', 'activity_type')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(ObjectIdAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'object_id', 'user', 'score', 'rank')
    ordering = ('rank', '-score')


@admin.register(Workout)
class WorkoutAdmin(ObjectIdAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'object_id', 'user', 'title', 'difficulty', 'target_reps', 'is_completed')
    list_filter = ('difficulty', 'is_completed')
    search_fields = ('user__name', 'title')
