from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):

    def test_string_representation(self):
        post = Post(title="Test Title")
        self.assertEqual(str(post), "Test Title")

    def test_post_creation(self):
        post = Post.objects.create(title="New Post", content="Content here", published=True)
        self.assertEqual(Post.objects.count(), 1)
        self.assertTrue(post.published)

class PostListViewTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Published Post", content="Visible", published=True)
        Post.objects.create(title="Draft Post", content="Hidden", published=False)

    def test_only_published_posts_visible(self):
        response = self.client.get(reverse('post_list'))  # Assume URL name is 'post_list'
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Published Post")
        self.assertNotContains(response, "Draft Post")
