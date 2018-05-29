#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Laird Streak'
SITENAME = "'Laird Streak`s Personal Blog'"
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
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/lairdstreak'),
          ('GitHub', 'https://github.com/LairdStreak'),)     

TWITTER_USERNAME = 'lairdstreak'          

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#THEME = "themes/pelican-alchemy/alchemy"
THEME = "themes/blueidea"

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
