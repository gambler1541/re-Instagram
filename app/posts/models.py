from django.db import models

from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(
        # <app_name>.<Model.name>
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자',
    )
    photo = models.ImageField(
        '사진',
        upload_to='post'
    )
    # auto_now_add: 객체가 처음 생성될때의 시간 저장
    # auto_now: 객체의 save()가 호출될 때 마다 저장
    created_at = models.DateTimeField(auto_now_add=True,)
    modified_a = models.DateTimeField(auto_now=True,)


    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = f'{verbose_name} 목록'
        # 가장 최신의 post가 위로
        # 객체가 복사될 때 기능을 안 할 수도있음
        # -created_at을 하는게 더 효과적
        ordering = ['-pk']


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='포스트',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자',
    )
    content = models.TextField(
        '댓글 내용'
    )
    tags = models.ManyToManyField(
        'HashTag',
        blank=True,
        verbose_name='해시태그 목록',
    )

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = f'{verbose_name} 목록'


class HashTag(models.Model):
    name = models.CharField(
        '태그명',
        max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '해시태그'
        verbose_name_plural = f'{verbose_name} 목록'
