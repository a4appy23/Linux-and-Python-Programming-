import sys
import glob
import os
import stat

# Import pywrapper (complication due to dot in directory name)
import importlib
spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
sh_pywrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh_pywrapper)

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    module.process = sh_pywrapper.create_process()
    module.commands_list = sh_pywrapper.parse('handin2.sh')
    module.base_dir = os.path.abspath(sh_pywrapper.get_cwd(process)).strip()

def teardown_module(module):
    """Make sure process is dead"""
    sh_pywrapper.kill_process(module.process)

def test_ex1():
    '''Test whether student background file exists'''
    sh_pywrapper.run(process, commands_list[0])

    # Check that file exists
    assert os.path.exists(os.path.join(base_dir, "background.txt"))

    # Check that file is not empty
    with open("background.txt") as f:
        assert len(f.read()) > 0

def test_ex2():
    '''Test whether thesaurus file was found'''
    sh_pywrapper.run(process, commands_list[1])
    assert(os.path.exists(os.path.join(base_dir, "th_en_US_v2.dat")))

def test_ex3():
    '''Test for search for the word hacker'''
    output = [line for line in sh_pywrapper.run(process, commands_list[2]) if len(line.strip()) > 0]
    output = [line.strip() for line in "".join(output).split('\n') if len(line.strip()) > 0]
    print(output)
    assert(len(output) == 17)

def test_ex4():
    '''Test for search for the word hacker - starting with ('''
    output = [line for line in sh_pywrapper.run(process, commands_list[3]) if len(line.strip()) > 0]
    output = [line.strip() for line in "".join(output).split('\n') if len(line.strip()) > 0]
    print(output)
    assert(len(output) == 11)

def test_ex5():
    '''Test for search for the word hacker - starting with ( - only first'''
    output = [line for line in sh_pywrapper.run(process, commands_list[4]) if len(line.strip()) > 0]
    output = [line.strip() for line in "".join(output).split('\n') if len(line.strip()) > 0]
    print(output)
    assert(len(output) == 1)

def test_ex6():
    '''Test for search for the word hacker - starting with ( - only first - split'''
    output = [line for line in sh_pywrapper.run(process, commands_list[5]) if len(line.strip()) > 0]
    output = [line.strip() for line in "".join(output).split('\n') if len(line.strip()) > 0]
    print(output)
    assert(len(output) == 8)

def test_ex7():
    '''Test for search for the word hacker - starting with ( - only first - split - omit first'''
    output = [line for line in sh_pywrapper.run(process, commands_list[6]) if len(line.strip()) > 0]
    output = [line.strip() for line in "".join(output).split('\n') if len(line.strip()) > 0]
    print(output)
    assert(len(output) == 7)

def test_ex8():
    '''Test for search for the word hacker - starting with ( - only first - split - omit first - with line numbers'''
    output = [line for line in sh_pywrapper.run(process, commands_list[7]) if len(line.strip()) > 0]
    output = [line.strip() for line in "".join(output).split('\n') if len(line.strip()) > 0]
    print(output)
    assert(len(output) == 7)
    for line in output:
        assert(line[0].isdigit())

def test_ex9():
    '''Test for search for the word hacker - starting with ( - only first - split - omit first - with line numbers - save to file'''
    sh_pywrapper.run(process, commands_list[8])
    print(os.path.join(base_dir, "hacker_output.txt"))
    assert(os.path.exists(os.path.join(base_dir, "hacker_output.txt")))


    
