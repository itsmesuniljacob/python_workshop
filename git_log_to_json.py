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

def main():
    '''
    Main program
    '''
    package_names = ['git2json']
    for package_name in package_names:
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            print(package_name+' not installed')
            sys.exit()
    program_name = sys.argv[0]
    print(program_name)
    git_dir = sys.argv[1:]
    if len(git_dir) != 1:
        print('Argument missing:')
        print('      Usage: python {} {}'.format(sys.argv[0], 'git directory'))
        sys.exit()

    module_name = 'git2json'
    process = Popen(module_name, cwd=git_dir[0], stdout=PIPE, stderr=PIPE)
    (process, error) = process.communicate()
    print(error)
    remove_byte_literal = process.decode('utf-8')
    with open('out.json', 'w') as file_name:
        print(remove_byte_literal, file=file_name)

if __name__ == '__main__':
    main()
