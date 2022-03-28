from django.db import models


# 게시물 타입 모델
class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, null=True)


# 게시물 태그 모델
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()


# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.ForeignKey('Type', related_name="post_type", on_delete=models.CASCADE)  # 게시물의 타입은 여러개를 가질 수 있음.
    tags = models.ManyToManyField("Tag", related_name="posts")
