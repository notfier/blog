from django.test import  TestCase, Client
from django.core.urlresolvers import reverse

from blog.models import Post, Tag, Comments

import os

# Create your tests here.


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

