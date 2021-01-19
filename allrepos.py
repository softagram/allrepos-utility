# Utility for working with multiple repos when repos have been placed in a single top level dir
#
# Example use cases:
#
# Get default branches.
#  python allrepos.py symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@ @'
#
# Delete all branches with name foo from remotes:
#  python allrepos.py ls-remote --exit-code --heads origin foo IF_OK_EXECUTE_ALSO push origin --delete foo


import sys, os, re

args = sys.argv[1:]
ext_slot = ''
ext_args = []
if 'IF_OK_EXECUTE_ALSO' in args:
    pos = args.index('IF_OK_EXECUTE_ALSO')
    ext_args = args[pos+1:]
    args = args[:pos]

for fn in os.listdir('.'):
    if os.path.isdir(fn) and os.path.exists(fn + '/.git'):
        main_cmd = f'echo {fn} && git -C {fn} ' + ' '.join(args)
        if ext_args:
            ext_slot = f' && git -C {fn} ' + ' '.join(ext_args)
        os.system(main_cmd + ext_slot)

