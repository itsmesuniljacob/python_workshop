'''
This module use git2json package to transform the
output from the `git log` command into json format

The output is written to a file after removing EOL
characters
'''
import sys
import importlib.util
from subprocess import Popen, PIPE
import git2json # pylint: disable=W0611

PACKAGE_NAMES = ['git2json']
for PACKAGE_NAME in PACKAGE_NAMES:
    spec = importlib.util.find_spec(PACKAGE_NAME)
    if spec is None:
        print(PACKAGE_NAME+' not installed')
        sys.exit()
PROGRAM_NAME = sys.argv[0]
GIT_DIR = sys.argv[1:]

if len(GIT_DIR) != 1:
    print('Argument missing:')
    print('      Usage: python {} {}'.format(sys.argv[0], 'git directory'))
    sys.exit()

MODULE_NAME = 'git2json'
PROCESS = Popen(MODULE_NAME, cwd=GIT_DIR[0], stdout=PIPE, stderr=PIPE)
(PROCESS, ERROR) = PROCESS.communicate()
REMOVE_BYTE_LITERAL = PROCESS.decode('utf-8')
with open('out.json', 'w') as f:
    print(REMOVE_BYTE_LITERAL, file=f)
