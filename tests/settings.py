#!/usr/bin/env python
# -*- coding: utf-8 -*-

HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'easy_thumbnails',
        'filer',
        'mptt',
        'djangocms_text_ckeditor',
        'djangocms_link',
        'djangocms_picture',
        'djangocms_bootstrap4',
        'djangocms_bootstrap4.contrib.bootstrap4_alerts',
        'djangocms_bootstrap4.contrib.bootstrap4_badge',
        'djangocms_bootstrap4.contrib.bootstrap4_card',
        'djangocms_bootstrap4.contrib.bootstrap4_carousel',
        'djangocms_bootstrap4.contrib.bootstrap4_collapse',
        'djangocms_bootstrap4.contrib.bootstrap4_grid',
        'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
        'djangocms_bootstrap4.contrib.bootstrap4_link',
        'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
        'djangocms_bootstrap4.contrib.bootstrap4_media',
        'djangocms_bootstrap4.contrib.bootstrap4_picture',
        'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    ],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'LANGUAGE_CODE': 'en',
    'ALLOWED_HOSTS': ['localhost'],
    'DJANGOCMS_PICTURE_RESPONSIVE_IMAGES': False,
    'DJANGOCMS_PICTURE_RESPONSIVE_IMAGES_VIEWPORT_BREAKPOINTS': [576, 768, 992],
}


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_bootstrap4')


if __name__ == '__main__':
    run()
