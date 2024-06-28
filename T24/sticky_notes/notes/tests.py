from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteCreationTestCase(TestCase):

    def test_create_note(self):
        # Create a new note object
        new_note = Note.objects.create(
            title="Test Note",
            content="This is a test note."
        )
        # Check if the note was created successfully
        self.assertEqual(new_note.title, "Test Note")
        self.assertEqual(new_note.content, "This is a test note.")

    def test_create_note_view(self):
        # Test the view that renders the form for creating a new note
        url = reverse('note_new')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test creating a new note using POST data
        response = self.client.post(url, {'title': 'New Test Note', 'content': 'Test content'})
        self.assertEqual(response.status_code, 302)  # Check if redirection happens after successful creation
        new_note = Note.objects.last()
        self.assertEqual(new_note.title, 'New Test Note')
        self.assertEqual(new_note.content, 'Test content')

"""
TEST DELETION

class NoteEditingTestCase(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Initial Note",
            content="This is the initial content."
        )

    def test_edit_note_view(self):
        # Test the view that renders the form for editing a note
        url = reverse('note_edit', args=[self.note.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test editing the note using POST data
        response = self.client.post(url, {'title': 'Edited Note', 'content': 'Edited content'})
        self.assertEqual(response.status_code, 302)  # Check if redirection happens after successful editing
        edited_note = Note.objects.get(pk=self.note.pk)
        self.assertEqual(edited_note.title, 'Edited Note')
        self.assertEqual(edited_note.content, 'Edited content')

"""

"""
TEST EDITING

# notes/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteEditingTestCase(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Initial Note",
            content="This is the initial content."
        )

    def test_edit_note_view(self):
        # Test the view that renders the form for editing a note
        url = reverse('note_edit', args=[self.note.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test editing the note using POST data
        response = self.client.post(url, {'title': 'Edited Note', 'content': 'Edited content'})
        self.assertEqual(response.status_code, 302)  # Check if redirection happens after successful editing
        edited_note = Note.objects.get(pk=self.note.pk)
        self.assertEqual(edited_note.title, 'Edited Note')
        self.assertEqual(edited_note.content, 'Edited content')

"""