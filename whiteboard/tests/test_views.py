from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.test.client import Client
from django.urls import reverse


@override_settings(AXES_ENABLED=False)
class HomeTestCase(TestCase):
    fixtures = ["lifts"]

    def setUp(self):
        self.client = Client()
        self.correctPassword = "correct"
        self.wrongPassword = "wrong"
        self.user = User.objects.get(username="dan")
        self.user.set_password(self.correctPassword)
        self.user.save()

    def test_home_bad_password(self):
        self.client.login(username="dan", password=self.wrongPassword)
        response = self.client.get(
            reverse("home"),
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login")

    def test_home_good_password(self):
        self.client.login(username="dan", password=self.correctPassword)
        response = self.client.get(
            reverse("home"),
        )
        self.assertEqual(response.status_code, 200)


@override_settings(AXES_ENABLED=False)
class LiftListCreateTestCase(TestCase):
    fixtures = ["lifts"]

    def setUp(self):
        self.client = Client()
        self.correctPassword = "correct"
        self.wrongPassword = "wrong"
        self.user = User.objects.get(username="dan")
        self.user.set_password(self.correctPassword)
        self.user.save()

    def test_lift_list_create_bad_password(self):
        self.client.login(username="dan", password=self.wrongPassword)
        response = self.client.get(
            reverse("lift_list"),
        )
        self.assertEqual(response.status_code, 403)

    def test_lift_list_create_create_lift(self):
        self.client.login(username="dan", password=self.correctPassword)
        data = '{"name":"Squat", "weight": 285, "reps": 1, "one_rep_max": 285, "fake_one_rep": 0}'
        response = self.client.post(
            reverse("lift_list"),
            data,
            "application/json",
        )
        self.assertEqual(
            response.json(),
            {
                "created_at": "March 02, 2021",
                "fake_one_rep": "0.0",
                "id": 10,
                "labels": {
                    "created_at": "Date Set",
                    "fake_one_rep": "Theoretical One Rep",
                    "id": "ID",
                    "name": "Lift Name",
                    "one_rep_max": "One Rep Max",
                    "reps": "Reps",
                    "weight": "Weight Lifted",
                },
                "name": "Squat",
                "one_rep_max": 285,
                "reps": 1,
                "weight": 285,
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_lift_list_create_good_password(self):
        self.client.login(username="dan", password=self.correctPassword)
        response = self.client.get(
            reverse("lift_list"),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": 9,
                    "name": "Deadlift",
                    "weight": 315,
                    "reps": 1,
                    "one_rep_max": 315,
                    "fake_one_rep": "0.0",
                    "created_at": "February 26, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
                {
                    "id": 8,
                    "name": "Bench",
                    "weight": 190,
                    "reps": 1,
                    "one_rep_max": 190,
                    "fake_one_rep": "0.0",
                    "created_at": "February 26, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
                {
                    "id": 7,
                    "name": "Squat Clean",
                    "weight": 145,
                    "reps": 1,
                    "one_rep_max": 145,
                    "fake_one_rep": "0.0",
                    "created_at": "February 26, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
                {
                    "id": 6,
                    "name": "Power Clean",
                    "weight": 185,
                    "reps": 1,
                    "one_rep_max": 185,
                    "fake_one_rep": "0.0",
                    "created_at": "February 26, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
                {
                    "id": 5,
                    "name": "Clean and Jerk",
                    "weight": 185,
                    "reps": 1,
                    "one_rep_max": 185,
                    "fake_one_rep": "0.0",
                    "created_at": "February 26, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
                {
                    "id": 4,
                    "name": "Squat Clean and Jerk",
                    "weight": 145,
                    "reps": 1,
                    "one_rep_max": 145,
                    "fake_one_rep": "0.0",
                    "created_at": "February 26, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
                {
                    "id": 3,
                    "name": "Squat",
                    "weight": 305,
                    "reps": 1,
                    "one_rep_max": 305,
                    "fake_one_rep": "0.0",
                    "created_at": "February 26, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
                {
                    "id": 2,
                    "name": "Snatch",
                    "weight": 120,
                    "reps": 1,
                    "one_rep_max": 120,
                    "fake_one_rep": "0.0",
                    "created_at": "February 25, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
            ],
        )


@override_settings(AXES_ENABLED=False)
class LiftListTestCase(TestCase):
    fixtures = ["lifts"]

    def setUp(self):
        self.client = Client()
        self.correctPassword = "correct"
        self.wrongPassword = "wrong"
        self.user = User.objects.get(username="dan")
        self.user.set_password(self.correctPassword)
        self.user.save()
        self.user2 = User.objects.create_user(
            "dave", "dave@thedamned.com", self.correctPassword
        )

    def test_lift_list_bad_password(self):
        self.client.login(username="dan", password=self.wrongPassword)
        response = self.client.get(
            reverse("lift_list"),
        )
        self.assertEqual(response.status_code, 403)

    def test_lift_list_good_password(self):
        self.client.login(username="dan", password=self.correctPassword)
        response = self.client.get(
            reverse("single_lift", kwargs={"liftname": "Deadlift"}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": 9,
                    "name": "Deadlift",
                    "weight": 315,
                    "reps": 1,
                    "one_rep_max": 315,
                    "fake_one_rep": "0.0",
                    "created_at": "February 26, 2021",
                    "labels": {
                        "id": "ID",
                        "name": "Lift Name",
                        "one_rep_max": "One Rep Max",
                        "fake_one_rep": "Theoretical One Rep",
                        "weight": "Weight Lifted",
                        "reps": "Reps",
                        "created_at": "Date Set",
                    },
                },
            ],
        )

    def test_lift_list_good_password_user2(self):
        self.client.login(username="dave", password=self.correctPassword)
        response = self.client.get(
            reverse("single_lift", kwargs={"liftname": "Deadlift"}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [],
        )
