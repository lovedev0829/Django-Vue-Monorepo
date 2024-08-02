from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status

from api.models import Note, User
from api.core.v1.serializers import NoteSerializer
from api.core.v1.viewsets.note_viewsets import NoteViewSet

class NoteViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user = User.objects.create_user(
            username="testuser", 
            first_name="John",
            last_name="Doe",
            email="testuser@sample.com", 
            password="testpassword"
        )

        response = self.client.post(
            "/api/auth/users/jwt/create", {
                "email": "testuser@sample.com", 
                "password": "testpassword"
            }
        )

        if response.status_code == status.HTTP_200_OK:
            self.token = response.data["access"]
        else:
            self.token = None

        self.note = Note.objects.create(
            title="Test Note", 
            body="Test Body", 
            user_id=self.user
        )


    def test_list_notes(self):
        url = "/api/v1/notes/"
        request = self.factory.get(
            url, 
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        view = NoteViewSet.as_view({"get": "list"})

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_note(self):
        url = "/api/v1/notes/"
        data = {"title": "New Note", "body": "New Body"}
        request = self.factory.post(
            url, 
            data,
            format="json", 
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        view = NoteViewSet.as_view({"post": "create"})

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_note(self):
        url = f"/api/v1/notes/{self.note.id}/"
        request = self.factory.get(
            url, 
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        view = NoteViewSet.as_view({"get": "retrieve"})

        response = view(request, pk=self.note.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note(self):
        url = f"/api/v1/notes/{self.note.id}/"
        data = {"title": "Updated Note", "body": "Updated Body"}
        request = self.factory.put(
            url, 
            data, 
            format="json", 
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        view = NoteViewSet.as_view({"put": "update"})

        response = view(request, pk=self.note.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_note(self):
        url = f"/api/v1/notes/{self.note.id}/"
        data = {"title": "Partial Update"}
        request = self.factory.patch(
            url, 
            data, 
            format="json", 
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        view = NoteViewSet.as_view({"patch": "partial_update"})

        response = view(request, pk=self.note.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note(self):
        url = f"/api/v1/notes/{self.note.id}/"
        request = self.factory.delete(
            url, 
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        view = NoteViewSet.as_view({"delete": "destroy"})

        response = view(request, pk=self.note.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
