from django.db import models

class Author(models.Model):
    """
    Model representing the author of a bulletin board post.

    Fields:
    - name: CharField for the author's name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Model representing a bulletin board post.

    Fields:
    - title: CharField for the post title with a maximum length of 255 characters.
    - content: TextField for the post content.
    - created_at: DateTimeField set to the current date and time when the post is created.
    - author: ForeignKey representing the author of the post.

    Relationships:
    - author: ForeignKey to the Author model, establishing the author of the post.

    Methods:
    - No specific methods are defined in this model.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
