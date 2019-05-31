'''
This module use git2json package to transform the
output from the `git log` command into json format

The output is written to a file after removing EOL
characters
'''
import sys
from subprocess import Popen, PIPE
try:
    import git2json # pylint: disable=W0611
except ModuleNotFoundError:
    print('Please install git2json package:')
    print('       Usage: pip install git2json')
    sys.exit(1)

def accept_argument():
    '''
    This function would accept argument.
    If no arguments are given the function will
    throw an error
    '''
    git_dir = sys.argv[1:]
    if len(git_dir) != 1:
        print('Argument missing:')
        print('      Usage: python {} {}'.format(sys.argv[0], 'git directory'))
        sys.exit()
    return git_dir

def parse_json_logs(git_dir, module_name):
    '''
    This function will call the git2json module
    and create a JSON output
    '''
    process = Popen(module_name, cwd=git_dir[0], stdout=PIPE, stderr=PIPE)
    (process, error) = process.communicate() # pylint: disable=unused-variable
    remove_byte_literal = process.decode('utf-8')
    return remove_byte_literal

def write_to_outputfile(data):
    '''
    This function will write the json to
    local output file
    '''
    with open('out.json', 'w') as file_name:
        print(data, file=file_name)

DOT_GIT_DIRECTORY = accept_argument()
MODULE_NAME = 'git2json'
GIT_LOG_JSON_OUTPUT = parse_json_logs(DOT_GIT_DIRECTORY, MODULE_NAME)
write_to_outputfile(GIT_LOG_JSON_OUTPUT)
