#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from pathlib import Path
from argparse import ArgumentParser
import argcomplete

def main(**args):
  pass

if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('source_file', metavar='INPUT', choices=['spam', 'eggs'])
  argcomplete.autocomplete(parser)
  args = parser.parse_args()
  main(**vars(args))
