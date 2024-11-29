from django.test import TestCase

# Create your tests here.


class TestModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.user.save()
        self.post = Post.objects.create(user=self.user, title='Test Post', content='This is a test post')
        self.post.save()
        self.comment = Comment.objects.create(post=self.post, user=self.user, content='This is a test comment')
        self.comment.save()
        self.like = Like.objects.create(post=self.post, user=self.user)
        self.like.save()
        self.dislike = Dislike.objects.create(post=self.post, user=self.user)
        self.dislike.save()
        self.tag = Tag.objects.create(name='testtag')
        self.tag.save()
        self.post.tag.add(self.tag)
        self.post.save()
        self.post2 = Post.objects.create(user=self.user, title='Test Post 2', content ='This is a test post 2')