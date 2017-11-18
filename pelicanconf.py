#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = u'Cloud-init Project Info'
SITEURL = ''
AUTHOR = u'chad.smith@canonical.com'
SITEURL = ''
SITENAME = 'Cloud-init Info'
SITETITLE = 'Cloud-init'
SITESUBTITLE = 'Make your cloud images be all they can be'
SITEDESCRIPTION = 'Cloud-init project updates and general information'
SITELOGO = SITEURL + '/images/cloud-init-orange.svg'
FAVICON = SITEURL + '/theme/img/favicon.ico'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

BROWSER_COLOR = '#2c001e'
ROBOTS = 'index, follow'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Docs', 'https://cloudinit.readthedocs.org/'),
         ('Overview', 'https://cloud-init.io'),
         ('Hacking', 'https://cloudinit.readthedocs.io/en/latest/topics/hacking.html'),
         ('CI builds', 'https://jenkins.ubuntu.com/server/view/cloud-init/'),
         ('Code', 'https://launchpad.net/cloud-init'),)

# Social widget
SOCIAL = (('github', 'https://github.com/cloud-init'),
          ('wechat', 'https://webchat.freenode.net/?channels=cloud-init'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'Flex'
# Plugins config
JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.i18n']
}
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'i18n_subsites', 'post_stats']

STATIC_PATHS = ['images', 'extra']
