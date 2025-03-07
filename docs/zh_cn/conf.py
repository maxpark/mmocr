# Copyright (c) OpenMMLab. All rights reserved.
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import subprocess
import sys

import pytorch_sphinx_theme

sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------

project = 'MMOCR'
copyright = '2020-2030, OpenMMLab'
author = 'OpenMMLab'

# The full version, including alpha/beta/rc tags
version_file = '../../mmocr/version.py'
with open(version_file) as f:
    exec(compile(f.read(), version_file, 'exec'))
__version__ = locals()['__version__']
release = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_markdown_tables',
    'sphinx_copybutton',
    'myst_parser',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
]
autodoc_typehints = 'description'

autodoc_mock_imports = ['mmcv._ext']
autosummary_generate = True  # Turn on sphinx.ext.autosummary
# Ignore >>> when copying code
copybutton_prompt_text = r'>>> |\.\.\. '
copybutton_prompt_is_regexp = True

myst_enable_extensions = ['colon_fence']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'pytorch_sphinx_theme'
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]
html_theme_options = {
    'logo_url':
    'https://mmocr.readthedocs.io/zh_CN/dev-1.x/',
    'menu': [
        {
            'name':
            '教程 Notebook',
            'url':
            'https://colab.research.google.com/github/open-mmlab/mmocr/blob/'
            'dev-1.x/demo/tutorial.ipynb'
        },
        {
            'name': 'GitHub',
            'url': 'https://github.com/open-mmlab/mmocr'
        },
        {
            'name':
            '上游库',
            'children': [
                {
                    'name': 'MMEngine',
                    'url': 'https://github.com/open-mmlab/mmengine',
                    'description': '深度学习模型训练基础库'
                },
                {
                    'name': 'MMCV',
                    'url': 'https://github.com/open-mmlab/mmcv',
                    'description': '基础视觉库'
                },
                {
                    'name': 'MMDetection',
                    'url': 'https://github.com/open-mmlab/mmdetection',
                    'description': '目标检测工具箱'
                },
            ]
        },
        {
            'name':
            '版本',
            'children': [
                {
                    'name': 'MMOCR 0.x',
                    'url': 'https://mmocr.readthedocs.io/zh_CN/latest/',
                    'description': 'main 分支文档'
                },
                {
                    'name': 'MMOCR 1.x',
                    'url': 'https://mmocr.readthedocs.io/zh_CN/dev-1.x/',
                    'description': '1.x 分支文档'
                },
            ],
            'active':
            True,
        },
    ],
    # Specify the language of shared menu
    'menu_lang':
    'cn',
}

language = 'zh_CN'

master_doc = 'index'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'https://cdn.datatables.net/1.13.2/css/dataTables.bootstrap5.min.css',
    'css/readthedocs.css'
]
html_js_files = [
    'https://cdn.datatables.net/1.13.2/js/jquery.dataTables.min.js',
    'https://cdn.datatables.net/1.13.2/js/dataTables.bootstrap5.min.js',
    'js/collapsed.js',
    'js/table.js',
]

myst_heading_anchors = 4

# Configuration for intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'torch': ('https://pytorch.org/docs/stable/', None),
    'mmcv': ('https://mmcv.readthedocs.io/zh_CN/2.x/', None),
    'mmengine': ('https://mmengine.readthedocs.io/zh_CN/latest/', None),
    'mmdetection': ('https://mmdetection.readthedocs.io/zh_CN/dev-3.x/', None),
}


def builder_inited_handler(app):
    subprocess.run(['./cp_origin_docs.sh'])
    subprocess.run(['./merge_docs.sh'])
    subprocess.run(['./stats.py'])
    subprocess.run(['./dataset_zoo.py'])
    subprocess.run(['./project_zoo.py'])


def setup(app):
    app.connect('builder-inited', builder_inited_handler)
