#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Gr\xe9gory D'Angelo"
SITENAME = u"Gr\xe9gory D'Angelo - Data Science, Machine Learning, & Artificial Intelligence"
SITEURL = ''
THEME = 'theme/'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/gdangel0'),
          ('linkedin', 'https://www.linkedin.com/in/gregorydangelo'),
          ('github', 'https://github.com/gdangelo'),
          ('kaggle', 'https://www.kaggle.com/gdangel0'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

AUTHOR_SAVE_AS = False

MARKUP = ('md')

#PLUGIN_PATHS = ['./plugins']
#PLUGINS = ['ipynb.markup']

DIRECT_TEMPLATES = ['index', 'about', 'contact', 'search']

# static paths will be copied under the same name
STATIC_PATHS = ['assets', 'extra/CNAME', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.png': {'path': 'favicon.png'},
}
