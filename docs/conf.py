extensions = []
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = u'marturion'
copyright = u'2012, Eldarion'
version = '0.2'
release = '0.2'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = []
htmlhelp_basename = 'marturiondoc'
latex_documents = [
  ('index', 'marturion.tex', u'marturion Documentation',
   u'Eldarion', 'manual'),
]
man_pages = [
    ('index', 'marturion', u'marturion Documentation',
     [u'Eldarion'], 1)
]
