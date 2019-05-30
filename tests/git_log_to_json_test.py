"""Functional test of the 'git_log_to_json.py' sample program"""
import pytest
from subprocess import Popen, PIPE

def test_output_of_parser():
    program = 'src/git_log_to_json.py'
    output = Popen(['python',program],stdout=PIPE).communicate()[0]
    assert b'git_log_to_json.py\r\nArgument missing:\r\n' in output