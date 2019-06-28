"""Functional test of the 'git_log_to_json.py' """
from subprocess import Popen, PIPE

def test_output_of_parser():
    '''
    Test the error output
    '''
    program = 'src/git_log_to_json.py'
    output = Popen(['python.exe', program], stdout=PIPE).communicate()[0]
    assert b'git_log_to_json.py' in output
    assert b'Argument missing' in output
