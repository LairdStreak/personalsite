#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Laird Streak'
SITENAME = "'My Personal Blog'"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/lairdstreak'),
          ('Another social link', '#'),)

TWITTER_USERNAME = 'lairdstreak'          

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pelican-blueidea"

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
