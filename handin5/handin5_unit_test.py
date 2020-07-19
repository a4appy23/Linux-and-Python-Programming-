import os
import pytest

# Import pywrapper (complication due to dot in directory name)
import importlib
spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
sh_pywrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh_pywrapper)

import handin5
import handin5_test

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    module.process = sh_pywrapper.create_process()
    module.commands_list = sh_pywrapper.parse('handin5.sh')

def teardown_module(module):
    '''Cleanup process'''
    sh_pywrapper.kill_process(module.process)

def test_unix_ex1():
    '''Test for existence of files'''
    sh_pywrapper.run(process, commands_list[0])[-1].strip()
    assert os.path.exists("british-english")
    assert os.path.exists("british-english-subset")

def test_unix_ex2():
    '''Test for identification of omitted letters'''
    output = [line.strip() for line in sh_pywrapper.run(process, commands_list[1])[-1].strip().split('\n')]
    expected_output = ['X','Y','Z'] 
    assert output == expected_output

def test_unix_ex3():
    '''Test that subset file was correctly reproduced'''
    sh_pywrapper.run(process, commands_list[2])[-1].strip()

    # Check the subset2 file exists
    assert os.path.exists("british-english-subset2")

    # Read contents of original subset file
    subset1_file = open("british-english-subset")
    subset1 = subset1_file.read()
    subset1_file.close()

    # Read contents of new subset file
    subset2_file = open("british-english-subset2")
    subset2 = subset2_file.read()
    subset2_file.close()

    # Compare new subset file to original
    assert subset1 == subset2


def test_python_ex1():
    '''Test read_fasta function'''

    # Check that the function has a doc-string
    assert handin5.read_fasta.__doc__ !=  None

    global data
    data = handin5.read_fasta('Ecoli.prot.fasta')

    # Check that function returns something
    assert data is not None

    # Check that it has keys
    assert len(data.keys()) > 0

    # Check that keys do not contain '>' character
    for key in data.keys():
        assert key[0] != '>'

        
def test_python_ex2():
    '''Test the test of the read_data function'''
    # Check that variable exists
    assert hasattr(handin5_test, 'fasta_dict')

    # Check for number of keys in dictionary
    assert len(handin5_test.fasta_dict.keys()) == 4183

    
def test_python_ex3():
    '''Test find_prot function'''

    # Check that the function has a doc-string
    assert handin5.find_prot.__doc__ !=  None

    # Test that function returns something
    assert handin5.find_prot(data, 'YHCN_ECOLI') is not None


def test_python_ex4():
    '''Test the test of the find_prot function'''    

    # Check that variable exists
    assert hasattr(handin5_test, 'yhcn')

    # Check that test program produces same result as calling
    # function directly
    assert handin5_test.yhcn == handin5.find_prot(data, 'YHCN_ECOLI')
    

def test_python_ex5():
    '''Test the test of the find_prot function'''    

    # Check that variable exists
    assert hasattr(handin5_test, 'boom')

    # Check that the boom variable is None as expected
    assert handin5_test.boom is None
    

def test_python_ex6():
    '''Test find_prot2 function'''

    # Check that the function has a doc-string
    assert handin5.find_prot2.__doc__ !=  None

    # Test that function returns all keys when given appropriate regexp
    assert len(handin5.find_prot2(data, '.*')) == len(data)


def test_python_ex7():
    '''Test the test of the find_prot2 function'''
    
    # Check that variable exists
    assert hasattr(handin5_test, 'matches')

    # Check that matches is a list
    assert isinstance(handin5_test.matches, list)
    
    # Test number of matches
    assert len(handin5_test.matches) == 233
    
    
