# allrepos.py: get stuff done with 100x git repo directories

Utility for working with multiple repos when repos have been placed in a single top level dir

# Couple of example use cases

## Run fetch for all
`python allrepos.py fetch`

## Get default branches
`python allrepos.py symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@ @'`

## Delete all branches with name foo from remotes:
`python allrepos.py ls-remote --exit-code --heads origin foo IF_OK_EXECUTE_ALSO push origin --delete foo`



# Requirements
- Python 3.6+ since uses f-strings.
- Git.

Note: the examples here involve usage of unix tools, but this is not limited to unix.
