from django.core.management.base import BaseCommand
from django.db import transaction

from octofit_tracker.models import Activity, LeaderboardEntry, Team, User, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    @transaction.atomic
    def handle(self, *args, **options):
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        marvel_team = Team.objects.create(
            name='Marvel Team',
            universe='Marvel',
            description='Earth\'s Mightiest Heroes',
        )
        dc_team = Team.objects.create(
            name='DC Team',
            universe='DC',
            description='Justice League core squad',
        )

        users = [
            User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel_team, total_points=980),
            User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel_team, total_points=910),
            User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc_team, total_points=940),
            User.objects.create(name='Diana Prince', email='diana@dc.com', team=dc_team, total_points=930),
        ]

        activity_seed = [
            ('HIIT Sprint', 25, 320),
            ('Strength Circuit', 45, 410),
            ('Mobility Flow', 20, 140),
        ]
        for user in users:
            for activity_name, duration, calories in activity_seed:
                Activity.objects.create(
                    user=user,
                    activity_type=activity_name,
                    duration_minutes=duration,
                    calories_burned=calories,
                )

        sorted_users = sorted(users, key=lambda item: item.total_points, reverse=True)
        for rank, user in enumerate(sorted_users, start=1):
            LeaderboardEntry.objects.create(user=user, score=user.total_points, rank=rank)

        workout_seed = [
            ('Power Upper', 'hard', 12, False),
            ('Core Blast', 'medium', 18, True),
            ('Speed Ladder', 'hard', 10, False),
        ]
        for index, user in enumerate(users):
            title, difficulty, reps, completed = workout_seed[index % len(workout_seed)]
            Workout.objects.create(
                user=user,
                title=title,
                difficulty=difficulty,
                target_reps=reps,
                is_completed=completed,
            )

        self.stdout.write(self.style.SUCCESS('octofit_db 샘플 데이터 적재가 완료되었습니다.'))
