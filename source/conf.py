# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = u'Shieber\'s Blog'
copyright = u'2018, Shieber'
author = u'Shieber'
# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u'0.5'


# -- General configuration ---------------------------------------------------
language = u'zh_CN'
exclude_patterns = []
pygments_style = 'sphinx'
extensions = ['chinese_search']
templates_path = ['_templates']
source_suffix = ['.rst','.md']
master_doc = 'index'


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'ShiebersBlogdoc'


# -- Options for LaTeX output ------------------------------------------------

# 注：在生成html的时候这句话要注释
# latex_engine = 'xelatex'

latex_elements={
#'papersize':'a4paper',
#'pointsize':'12pt',
#'classoptions':',oneside',
#'babel':'',
#'inputenc':'',
#'utf8extra':'',
#'preamble': r"""
#\hepersetup{unicode=true}
#\usepackage{xeCJK}
#\usepackage{indentfirst}
#\setlength{\parindent}{2em}
#\setCJKmainfont{WenQuanYi Micro Hei}
#\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
#\setCJKfamilyfont{song}{WenQuanYi Micro Hei}
#\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
#\XeTeXlinebreaklocale "zh"
#\XeTeXlinebreakskip = 0pt plus 1pt
#"""
'papersize':'a4paper',
'pointsize':'12pt',
'classoptions':',oneside',
'preamble': r'''
\hypersetup{unicode=true}
\usepackage{CJKutf8}
\usepackage{indentfirst} 
\setlength{\parindent}{2em}
\setCJKmainfont{WenQuanYi Micro Hei}
\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
\setCJKfamilyfont{song}{WenQuanYi Micro Hei}
\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
\DeclareUnicodeCharacter{00A0}{\nobreakspace}
\DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
\DeclareUnicodeCharacter{2713}{x}
\DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
\DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
\DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\begin{CJK}{UTF8}{gbsn}
\AtEndDocument{\end{CJK}}
''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ShiebersBlog.tex', u'Shieber\'s Blog Documentation',
     u'Shieber', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'shiebersblog', u'Shieber\'s Blog Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ShiebersBlog', u'Shieber\'s Blog Documentation',
     author, 'ShiebersBlog', 'One line description of project.',
     'Miscellaneous'),
]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# otherwise, readthedocs.org uses their theme by default, so no need to specify it
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

_exts = "../exts"
sys.path.append(os.path.abspath(_exts))
# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config



# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
