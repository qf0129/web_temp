from django.core.management import BaseCommand

#from __future__ import unicode_literals

import os
import sys
import pytz
import random
import string
from datetime import datetime
from optparse import make_option
from xml.etree import ElementTree as ET
from urllib.request import urlopen
from django.conf import settings
from django.utils import timezone
from django.core.files import File
from django.utils.text import Truncator
from django.utils.html import strip_tags
from django.utils.six.moves import input
from django.db.utils import IntegrityError
from django.utils.encoding import smart_str
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.core.management.base import CommandError
from django.core.management.base import LabelCommand
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth.models import AnonymousUser, User
from django.conf import settings
from cms.test_utils.testcases import CMSTestCase, TransactionCMSTestCase

from aldryn_newsblog.cms_apps import NewsBlogApp
from aldryn_people.models import Person
from aldryn_newsblog.models import Article, NewsBlogConfig
from aldryn_categories.models import Category
from parler.utils.context import switch_language
#import django_comments as comments

#from tagging.models import Tag

from django.utils.timezone import now
from django.utils.translation import activate, override

from cms import api
from cms.utils import get_cms_setting
from aldryn_newsblog.tests import NewsBlogTestsMixin, CleanUpMixin, NewsBlogTestCase


from aldryn_newsblog.tests import NewsBlogTestCase

class NewsBlogAPI( NewsBlogTestsMixin ):
    @classmethod
    def create_user_by_name(self, uname:str, fname:str, lname:str):
        return User.objects.create(
            username=uname, first_name=fname,
            last_name=lname)
    @classmethod
    def create_person_by_user(self, user:User, slug:str):
        return Person.objects.create(user, slug)

    def create_article(self, content=None, **kwargs):
        try:
            author = kwargs['author']
        except:
            user = User.objects.all().filter(username='ray')
        try:
            if user is None:
                user = User.objects.create(username = kwargs['author'])
                person = create_person_by_user(user, "", kwargs['author'] )
                slug = kwargs['author']
            else:
                print("user ", author, "found")

        except TypeError:
            self.stdout.write("failed query")
        except KeyError:
            self.stdout.write("user not exist")



        fields = {
            'title': self.rand_str(),
            'slug': self.rand_str(),
            'author': user,
            'owner': user,
            'app_config': self.app_config,
            'publishing_date': now(),
            'is_published': True,
        }

        fields.update(kwargs)

        article = Article.objects.create(**fields)
        # save again to calculate article search_data.
        article.save()

        if content:
            api.add_plugin(article.content, 'TextPlugin',
                           self.language, body=content)
        return article

    def create_tagged_articles(self, num_articles=3, tags=('tag1', 'tag2'),
                               **kwargs):
        """Create num_articles Articles for each tag"""
        articles = {}
        for tag_name in tags:
            tagged_articles = []
            for _ in range(num_articles):
                article = self.create_article(**kwargs)
                article.save()
                article.tags.add(tag_name)
                tagged_articles.append(article)
            tag_slug = tagged_articles[0].tags.slugs()[0]
            articles[tag_slug] = tagged_articles
        return articles

    def setup_categories(self):
        """
        Sets-up i18n categories (self.category_root, self.category1 and
        self.category2) for use in tests
        """
        self.language = settings.LANGUAGES[0][0]

        categories = []
        # Set the default language, create the objects
        with override(self.language):
            code = "{0}-".format(self.language)
            self.category_root = Category.add_root(
                name=self.rand_str(prefix=code, length=8))
            categories.append(self.category_root)
            self.category1 = self.category_root.add_child(
                name=self.rand_str(prefix=code, length=8))
            categories.append(self.category1)
            self.category2 = self.category_root.add_child(
                name=self.rand_str(prefix=code, length=8))
            categories.append(self.category2)

        # We should reload category_root, since we modified its children.
        self.category_root = self.reload(self.category_root)

        # Setup the other language(s) translations for the categories
        for language, _ in settings.LANGUAGES[1:]:
            for category in categories:
                with switch_language(category, language):
                    code = "{0}-".format(language)
                    category.name = self.rand_str(prefix=code, length=8)
                    category.save()

    def setUp(self):
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.root_page = api.create_page(
            'root page', self.template, self.language, published=True)
        self.app_config = NewsBlogConfig.objects.create(
            namespace=self.rand_str(), paginate_by=15)
        self.page = api.create_page(
            'page', self.template, self.language, published=True,
            parent=self.root_page,
            apphook='NewsBlogApp',
            apphook_namespace=self.app_config.namespace)
        self.plugin_page = api.create_page(
            title="plugin_page", template=self.template, language=self.language,
            parent=self.root_page, published=True)
        self.placeholder = self.page.placeholders.all()[0]

        self.setup_categories()

        for page in self.root_page, self.page:
            for language, _ in settings.LANGUAGES[1:]:
                api.create_title(language, page.get_slug(), page)
                page.publish(language)




##from . import NewsBlogTestCase, NewsBlogTransactionTestCase, TESTS_STATIC_ROOT
#SPECIFIC_OPTION = "filename"
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	# Show this when the user types help
    help = "import wordpress XML to django"
    args = 'wordpress.xml'

    def add_arguments(self, parser):
        parser.add_argument('--xmlfile', type=str)
	# A command must define handle()
    def handle(self, *args, **options):
        self.stdout.write("Doing All The Things!",)
        self.stdout.write(str(options))
        args = options['xmlfile']
        #activate(self.language)
        activate('en')
        tmodel = NewsBlogAPI()
        tmodel.setUp()
        title = u'This is a title from command line'
        #u = tmodel.create_user_by_name("ray", "ray", "ray")


        fields = {
            'title': u'Title 1',
            'slug': u'T1',
            'app_config': tmodel.app_config,
            'publishing_date': now(),
            'is_published': True,
        }


        tmodel.create_article(content="aaaa", **fields)


