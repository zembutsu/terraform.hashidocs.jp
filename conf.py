# -*- coding: utf-8 -*-

import sys
import os
import shlex

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Terraform 日本語版文章'
copyright = u'2016, Pocketstudio.net Documentation Project'
author = u'Masahito Zembutsu'
version = '0.1.0'
release = '0.1-beta'
language = 'ja'

exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['./_themes/']
html_static_path = ['_static']
html_search_language = 'ja'
htmlhelp_basename = 'Terraform-docs-ja-jp'
