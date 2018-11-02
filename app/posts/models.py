from django.db import models

class Post(models.Model):
    author = models.ForeignKey(
        # <app_name>.<Model.name>
        'members.User',
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(upload_to='post')


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'members.User',
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    tags = models.ManyToManyField(
        'HashTag',
        blank=True,
    )


class HashTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


