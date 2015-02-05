from django.test import  TestCase, Client
from django.core.urlresolvers import reverse

from test_blog.settings import BASE_DIR, MEDIA_URL
from blog.models import Post, Tag, Comments

import os

# Create your tests here.


class PostTest(TestCase):
    """
    Check the post creation.
    """

    def setUp(self):
        c = Client()
        with open(os.path.join(BASE_DIR, 'media/tests/trueorfalse.png'),
                                                            'rb') as fp:
            Post.objects.create(title="TestPost",
                                text="I am testing robot, yeah, yeah.",
                                slug="TestPost")
            c.post(MEDIA_URL, {'picture': fp})

    def test_result(self):
        test_post = Post.objects.get(title="TestPost")
        self.assertEqual(test_post.title, 'TestPost')


class TestTag(TestCase):
    """
    Check the tag adding.
    """

    def setUp(self):
        c = Client()
        Tag.objects.create(name="test tag", slug="test_slug")

    def test_result(self):
        test_tag = Tag.objects.get(name='test tag')
        self.assertEqual(test_tag.name, 'test tag')


class TestComments(TestCase):
    """
    Check the comments creation.
    """

    def setUp(self):
        c = Client()
        Post.objects.create(title="TestPost", text="I am tester.",
                            slug="TestPost")
        Comments.objects.create(comment=Post.objects.get(
                                title="TestPost"),
                                author="Tester",
                                comment_text="I am testero.")

    def test_result(self):
        comment = Comments.objects.get(comment=Post.objects.get(
                                       title="TestPost"),
                                       comment_text="I am testero.")
        self.assertEqual(comment.comment_text, 'I am testero.')


class TestViews(TestCase):

    def setUp(self):
        c = Client()

    def test_view_main_result(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_single_post(self):
        """
        Check the single post url.
        """
        self.post = Post.objects.create(title="Testo",
                                        picture="emul",
                                        text='Tester tested testo.',
                                        slug="test_single_post")
        response = self.client.get(reverse('single_post',
                                   kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)

    def test_view_tag_result(self):
        """
        Check the tag url.
        """
        self.tag = Tag.objects.create(name="Testo Tag",
                                      slug="testo_tag")
        response = self.client.get(reverse('tagger',
                                    kwargs={'slug': self.tag.slug}))
        self.assertEqual(response.status_code, 200)

    def test_view_add_comment_result(self):
        """
        Check the comment adding.
        """
        self.post = Post.objects.create(title="Testo",
                                        picture="emul",
                                        text='Tester tested testo.',
                                        slug="test_single_post")
        print(self.post)
        self.comment = Comments.objects.create(
                                comment=Post.objects.get(
                                title="Testo"),
                                author="Commentor",
                                comment_text='oops. comment.')
        print(self.comment)
        response = self.client.get(reverse('commenter',
                                        kwargs={'slug': self.post.slug}))
        print(list(response))
        self.assertEqual(response.status_code, 302)

