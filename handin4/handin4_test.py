import os
import pytest

# Import pywrapper (complication due to dot in directory name)
import importlib
spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
sh_pywrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh_pywrapper)

import urllib.request 
urllib.request.urlretrieve("https://wouterboomsma.github.io/lpp2019/data/experimental_results.txt", "experimental_results.txt")

import handin4

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    module.process = sh_pywrapper.create_process()
    module.commands_list = sh_pywrapper.parse('handin4.sh')

    
def teardown_module(module):
    '''Cleanup process'''
    sh_pywrapper.kill_process(module.process)

def test_unix_ex1():
    '''Check for largest column value'''
    output = sh_pywrapper.run(process, commands_list[0])[-1].strip()
    assert(output == "0.999681")

def test_unix_ex2():
    '''Check for sorted size-annotated dict files'''
    outputs = [output for output in sh_pywrapper.run(process, commands_list[1]) if len(output)>0]
    # Check that there is output from only one command
    assert(len(outputs)==1)
    outputs = [output for output in outputs[0].split('\n') if len(output) > 0]
    print(outputs)

    # Check for number of output lines
    assert(len(outputs) == 2)
    # Expand test into individual asserts to make error messages easier to understand
    assert(outputs[0].strip() == '948\t/usr/share/dict/british-english')
    assert(outputs[1].strip() == '952\t/usr/share/dict/american-english')
    
def test_python_ex1():
    '''Check read_data function'''
    global list_of_rows

    # Check that the function has a doc-string
    assert handin4.read_data.__doc__ !=  None

    # Call function
    list_of_rows = handin4.read_data('experimental_results.txt')

    # Check for number of lines
    assert len(list_of_rows) == 1000

    # Check that there are two values in last line
    assert len(list_of_rows[-1]) == 2
    
def test_python_ex2():
    '''Check calc_averages function'''

    # Check that the function has a doc-string
    assert handin4.calc_averages.__doc__ !=  None

    # Call function
    averages = handin4.calc_averages(list_of_rows)

    # Check that there are two return values
    assert len(averages) == 2

    # Check individual return values
    assert pytest.approx(averages[0], 1E-5) == 0.49505
    assert pytest.approx(averages[1], 1E-5) == 0.49895


def test_python_ex3():
    '''Check transpose_data function'''

    # Check that the function has a doc-string
    assert handin4.transpose_data.__doc__ !=  None

    # Call function
    list_of_columns = handin4.transpose_data(list_of_rows)

    # Check that there are two return values
    assert len(list_of_columns) == 2

    # Check that there are 1000 values in last line
    assert len(list_of_columns[-1]) == 1000
    
