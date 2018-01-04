#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Lockney'
SITENAME = u'Prehensile Tail'
SITEURL = u''
# TAGLINE = u'Pseudo-random musings'
TAGLINE = u'The miscellaneous ramblings of Thomas Lockney.'
TWITTER_USERNAME = u'tlockney'

PATH = u'content'

TIMEZONE = u'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
  ('twitter', 'https://twitter.com/@tlockney'),
  ('github','https://github.com/tlockney'),
  ('linkedin','https://www.linkedin.com/in/thomaslockney'),
  ('facebook','https://www.facebook.com/tlockney'),
  ('book', 'https://www.goodreads.com/author/show/8141502.Thomas_Lockney'),
)

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# articles
ARTICLE_URL= 'blog/{date:%Y}/{date:%M}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%M}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%M}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%M}/{date:%d}/index.html'

# tags
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# pages
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']

THEME='themes/pure-single-master'