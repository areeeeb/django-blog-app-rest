from django.db import models
from django.utils import timezone  # for time on the date_posted
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)  # Max length 100 characters
    content = models.TextField()  # The TextField has got no char limits unlike CharField

    date_posted = models.DateTimeField(default=timezone.now)  # No paran after the timezone.now because we dont want to
    # execute it at that point

    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey because User and post have 1 to many
    # relationship, User is the table of users that we will create and models.CASCADE will delete all the posts if the
    # user is deleted

    def __str__(self):
        return self.title  # Added str dunder method to show the title of the post when "Post.objects.all()" is executed

    def get_absolute_url(self):  # Part 10 CreatePostView
        # reverse is same as redirect but it returns the url as string instead of redirecting to that url
        return reverse('post-detail', kwargs={'pk': self.pk})
