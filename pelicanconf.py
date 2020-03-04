#!/usr/bin/env python
from pathlib import Path

AUTHOR = 'The Burpy Bear'
SITENAME = "The Burpy Bear House"
SITEURL = ''

# Static path
STATIC_PATHS = [
    'CNAME',
]

PATH = 'content'

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}/{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/{lang}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{slug}/{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}/{lang}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

DEFAULT_PAGINATION = 10

# Datetime settings
TIMEZONE = 'America/Chicago'
DEFAULT_DATE_FORMAT = '%b %d, %Y'

DEFAULT_LANG = 'en'

# Categories
USE_FOLDER_AS_CATEGORY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []

# Social widget
SOCIAL = []

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Markdown settings
MARKDOWN = {
    'extension_configs' : {
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}