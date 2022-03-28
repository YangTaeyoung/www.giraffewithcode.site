from django.db import models


# 게시물 타입 모델
class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, null=True)


# 게시물 태그 모델
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()


# 게시물-태그 매핑 모델
class PostTags(models.Model):
    # 게시글이나 태그를 삭제할 때 관련된 매핑 레코드 삭제
    post = models.ForeignKey('Post', related_name='post_tag_post', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', related_name='post_tag_tag', on_delete=models.CASCADE)


# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.ForeignKey('Type', related_name="post_type", on_delete=models.CASCADE)  # 게시물의 타입은 여러개를 가질 수 있음.
