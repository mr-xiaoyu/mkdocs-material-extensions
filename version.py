#!/usr/bin/env python

import argparse
import json
import sys
import yaml

from jinja2 import FileSystemLoader, Environment

# Target template
TARGET = 'overrides/partials/version.html'

# Initialize command line arguments
parser = argparse.ArgumentParser(description='Update version information')
parser.add_argument('input', help='path to JSON file with version information')

# Parse arguments and load data
args = parser.parse_args()
with open(args.input) as data:
  info = json.load(data)

# Read mkdocs.yml to determine current version
with open('./mkdocs.yml') as data:
  mkdocs = yaml.safe_load(data)

# Check that one of the versions matches site_url
selected = None
for version in info['versions']:
  if version['url'] == mkdocs['site_url']:
    selected = version['name']
if selected is None:
  raise Exception('"{0}" not found in versions'.format(mkdocs['site_url']))

# Check if the selected version is the first (= latest)
warning = None
if selected != info['versions'][0]['name']:
  warning = info['warning']

# Initialize template renderer
loader = FileSystemLoader(searchpath='data')
env    = Environment(loader=loader)

# Render template
template = env.get_template('version.html')
output   = template.render(
  selected=selected, 
  versions=info['versions'],
  warning=warning
)

# Write output to file
with open(TARGET, 'w') as partial:
  partial.write(output)

# Print message and exit
print('Updated "{0}"'.format(TARGET))
