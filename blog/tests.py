from django.test import TestCase
from blog.models import Post

# Create your tests here.


class PostTest(TestCase):
    """
    Check the post creation.
    """

    def setUp(self):
        Post.objects.create(title="TestPost",
                            text="Testo is not a test.")

    def test_result(self):
        test_post = Post.objects.get(title="TestPost")
        self.assertEqual(test_post.title, 'TestPost')


