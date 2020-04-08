#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from pathlib import Path
from os.path import relpath
from argparse import ArgumentParser
import argcomplete

def main(**args):
  pass

def list_log_file_transforms():
    log_path = Path(__file__).parent.absolute()
    file_glob = log_path.glob("logs/**/*.txt")
    # Only prompt for year if multiple years
    years = set()
    file_reps = []
    file_prompts = []
    for fp in file_glob:
        rp = Path(relpath(fp, log_path))
        # transform rp
        assert len(rp.parts[1:]) == 3, f"Expected {rp} to have 3 parts, got {len(rp.parts)}"
        y, m, fn = rp.parts[1:]
        years.add(y)
        m = m[0:2]
        fn = Path(fn).stem
        file_reps.append([y, m, fn])
    for fr in file_reps:
        y, m, fn = fr
        file_prompt = ""
        if len(years) > 1:
            file_prompt += f"{y}⠶{m}:{fn}"
        else:
            file_prompt += f"{m}⠶{fn}"
        file_prompts.append(file_prompt)
    return file_prompts

if __name__ == '__main__':
  parser = ArgumentParser(add_help=False)
  file_list=list_log_file_transforms()
  print(file_list)
  parser.add_argument('source_file', metavar='INPUT', choices=file_list)
  argcomplete.autocomplete(parser)
  args = parser.parse_args()
  main(**vars(args))
