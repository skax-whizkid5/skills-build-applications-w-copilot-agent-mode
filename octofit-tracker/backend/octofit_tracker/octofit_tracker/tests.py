from rest_framework.test import APITestCase

from .models import Activity, LeaderboardEntry, Team, User, Workout


class OctofitCollectionsApiTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel Team', universe='Marvel', description='Heroes')
        self.user = User.objects.create(
            name='Tony Stark',
            email='tony.test@marvel.com',
            team=self.team,
            total_points=1000,
        )

        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='HIIT Sprint',
            duration_minutes=25,
            calories_burned=300,
        )

        self.leaderboard_user = User.objects.create(
            name='Steve Rogers',
            email='steve.test@marvel.com',
            team=self.team,
            total_points=900,
        )
        self.leaderboard = LeaderboardEntry.objects.create(user=self.leaderboard_user, score=900, rank=2)

        self.workout = Workout.objects.create(
            user=self.user,
            title='Power Upper',
            difficulty='hard',
            target_reps=12,
            is_completed=False,
        )

    def test_api_root_and_collection_endpoints(self):
        endpoints = [
            '/api/',
            '/api/users/',
            '/api/teams/',
            '/api/activities/',
            '/api/leaderboard/',
            '/api/workouts/',
        ]

        for endpoint in endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, 200)

    def test_team_crud(self):
        create_response = self.client.post(
            '/api/teams/',
            {'name': 'DC Team', 'universe': 'DC', 'description': 'Justice League'},
            format='json',
        )
        self.assertEqual(create_response.status_code, 201)
        team_id = create_response.data['id']

        retrieve_response = self.client.get(f'/api/teams/{team_id}/')
        self.assertEqual(retrieve_response.status_code, 200)
        self.assertIn('object_id', retrieve_response.data)

        patch_response = self.client.patch(f'/api/teams/{team_id}/', {'universe': 'DC Comics'}, format='json')
        self.assertEqual(patch_response.status_code, 200)
        self.assertEqual(patch_response.data['universe'], 'DC Comics')

        delete_response = self.client.delete(f'/api/teams/{team_id}/')
        self.assertEqual(delete_response.status_code, 204)

    def test_user_crud_with_objectid_relation(self):
        team_response = self.client.get(f'/api/teams/{self.team.id}/')
        team_object_id = team_response.data['object_id']

        create_response = self.client.post(
            '/api/users/',
            {
                'name': 'Bruce Wayne',
                'email': 'bruce.test@dc.com',
                'team': team_object_id,
                'total_points': 950,
            },
            format='json',
        )
        self.assertEqual(create_response.status_code, 201)
        user_id = create_response.data['id']

        retrieve_response = self.client.get(f'/api/users/{user_id}/')
        self.assertEqual(retrieve_response.status_code, 200)
        self.assertIn('object_id', retrieve_response.data)

        put_response = self.client.put(
            f'/api/users/{user_id}/',
            {
                'name': 'Bruce Wayne',
                'email': 'bruce.test@dc.com',
                'team': str(self.team.id),
                'total_points': 990,
            },
            format='json',
        )
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(put_response.data['total_points'], 990)

        delete_response = self.client.delete(f'/api/users/{user_id}/')
        self.assertEqual(delete_response.status_code, 204)

    def test_activity_crud(self):
        create_response = self.client.post(
            '/api/activities/',
            {
                'user': str(self.user.id),
                'activity_type': 'Strength Circuit',
                'duration_minutes': 40,
                'calories_burned': 420,
            },
            format='json',
        )
        self.assertEqual(create_response.status_code, 201)
        activity_id = create_response.data['id']

        retrieve_response = self.client.get(f'/api/activities/{activity_id}/')
        self.assertEqual(retrieve_response.status_code, 200)

        patch_response = self.client.patch(
            f'/api/activities/{activity_id}/',
            {'duration_minutes': 45},
            format='json',
        )
        self.assertEqual(patch_response.status_code, 200)
        self.assertEqual(patch_response.data['duration_minutes'], 45)

        delete_response = self.client.delete(f'/api/activities/{activity_id}/')
        self.assertEqual(delete_response.status_code, 204)

    def test_leaderboard_crud(self):
        extra_user = User.objects.create(
            name='Diana Prince',
            email='diana.test@dc.com',
            team=self.team,
            total_points=930,
        )

        create_response = self.client.post(
            '/api/leaderboard/',
            {'user': str(extra_user.id), 'score': 930, 'rank': 3},
            format='json',
        )
        self.assertEqual(create_response.status_code, 201)
        leaderboard_id = create_response.data['id']

        retrieve_response = self.client.get(f'/api/leaderboard/{leaderboard_id}/')
        self.assertEqual(retrieve_response.status_code, 200)

        patch_response = self.client.patch(f'/api/leaderboard/{leaderboard_id}/', {'rank': 1}, format='json')
        self.assertEqual(patch_response.status_code, 200)
        self.assertEqual(patch_response.data['rank'], 1)

        delete_response = self.client.delete(f'/api/leaderboard/{leaderboard_id}/')
        self.assertEqual(delete_response.status_code, 204)

    def test_workout_crud(self):
        create_response = self.client.post(
            '/api/workouts/',
            {
                'user': str(self.user.id),
                'title': 'Core Blast',
                'difficulty': 'medium',
                'target_reps': 18,
                'is_completed': False,
            },
            format='json',
        )
        self.assertEqual(create_response.status_code, 201)
        workout_id = create_response.data['id']

        retrieve_response = self.client.get(f'/api/workouts/{workout_id}/')
        self.assertEqual(retrieve_response.status_code, 200)

        patch_response = self.client.patch(
            f'/api/workouts/{workout_id}/',
            {'is_completed': True},
            format='json',
        )
        self.assertEqual(patch_response.status_code, 200)
        self.assertTrue(patch_response.data['is_completed'])

        delete_response = self.client.delete(f'/api/workouts/{workout_id}/')
        self.assertEqual(delete_response.status_code, 204)

    def test_objectid_detail_lookup(self):
        team_detail = self.client.get(f'/api/teams/{self.team.id}/')
        object_id = team_detail.data['object_id']

        objectid_response = self.client.get(f'/api/teams/{object_id}/')
        self.assertEqual(objectid_response.status_code, 200)
        self.assertEqual(objectid_response.data['name'], self.team.name)
