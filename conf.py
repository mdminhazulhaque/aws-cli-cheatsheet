project = 'aws-cli-cheatsheet'
copyright = '2023, Md Minhazul Haque'
author = 'Md Minhazul Haque'

extensions = [
  'sphinx_rtd_theme',
  'sphinxemoji.sphinxemoji',
  'sphinxext.opengraph',
]

templates_path = ['_templates']
exclude_patterns = ['build.sh']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_extra_path = ['CNAME', '.nojekyll']

ogp_image = "/_static/aws-jq.png"
