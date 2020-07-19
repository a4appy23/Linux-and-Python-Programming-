import os

# Import pywrapper (complication due to dot in directory name)
import importlib
spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
sh_pywrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh_pywrapper)

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    module.process = sh_pywrapper.create_process()
    module.commands_list = sh_pywrapper.parse('handin3.sh')
    module.python_line_block_list = sh_pywrapper.parse('handin3.py')
    module.base_dir = os.path.abspath(sh_pywrapper.get_cwd(process)).strip()

    import urllib.request 
    urllib.request.urlretrieve("https://wouterboomsma.github.io/lpp2019/data/experimental_results.txt", "experimental_results.txt")
    urllib.request.urlretrieve("https://wouterboomsma.github.io/lpp2019/data/alice.txt", "alice.txt")
    
def teardown_module(module):
    """Make sure process is dead"""
    sh_pywrapper.kill_process(module.process)

def test_unix_ex1():
    '''Check for compressed file'''
    sh_pywrapper.run(process, commands_list[0])
    # Check that the original experimental_results.txt file still exists
    assert(os.path.exists("experimental_results.txt"))
    # Check that experimental_results.txt.gz exists
    assert(os.path.exists("experimental_results.txt.bz2"))

def test_unix_ex2():
    '''Check two sizes'''
    outputs = [output for output in sh_pywrapper.run(process, commands_list[1]) if len(output)>0]
    # Check that there is output from only one command
    assert(len(outputs)==1)
    # Split command by newline
    output_values = outputs[0].split('\n')
    print(output_values)
    output1 = int(output_values[0].strip())
    output2 = int(output_values[1].strip())
    # Check that size1 > size2
    assert(output1 > output2)

def test_unix_ex3():
    '''Check zeroed-out file'''
    sh_pywrapper.run(process, commands_list[2])
    assert(os.path.exists("experimental_results_zeros.txt"))
    for line in open("experimental_results_zeros.txt"):
        line = line.strip()
        for value in line.split():
            assert(value == "0.000000")
            
def test_unix_ex4():
    '''Check that size of zeroed out file is the same as original'''
    outputs = [output for output in sh_pywrapper.run(process, commands_list[3]) if len(output)>0]
    # Check that there is output from only one command
    assert(len(outputs)==1)
    # Split command by newline
    output_values = outputs[0].split('\n')
    output1 = int(output_values[0].strip())
    output2 = int(output_values[1].strip())
    # Check that size1 > size2
    assert(output1 == output2)
    
def test_unix_ex5():
    '''Compress zeros file and check size'''
    outputs = [output for output in sh_pywrapper.run(process, commands_list[4]) if len(output)>0]

    # Extract last output from commands
    output_values = outputs[-1].split('\n')
    output1 = int(output_values[0].strip())
    output2 = int(output_values[1].strip())
    # Check that size1 > size2
    assert(output1 > output2)
    

def test_unix_ex6():
    '''Explain difference'''
    output = "".join(sh_pywrapper.run(process, commands_list[5]))
    assert(os.path.exists("explanation.txt"))
    explanation1 = output.strip()
    explanation2 = open("explanation.txt").read().strip()

    # Remove whitespace at ends
    assert (explanation1 == explanation2)



    
def test_python_ex1():
    '''Test reading of content into list'''
    sh_pywrapper.exec_python(python_line_block_list[0])
    # Check for book_file variable name
    assert('lines' in vars(sh_pywrapper))
    # Check that book_file is of type list
    assert(isinstance(sh_pywrapper.lines, list))

def test_python_ex2():
    '''Test counting lines'''
    output = sh_pywrapper.exec_python(python_line_block_list[1])[1].strip()
    correct_length = "3736"
    assert(output == correct_length)

def test_python_ex3():
    '''Test printing of 41st line'''
    output = sh_pywrapper.exec_python(python_line_block_list[2])[1].strip()
    correct_line = "CHAPTER I. Down the Rabbit-Hole"
    assert(output == correct_line)

def test_python_ex4():
    '''Test counting words in of 43rd line'''
    output = sh_pywrapper.exec_python(python_line_block_list[3])[1].strip()
    correct_count = "14"
    assert(correct_count == output)
    
def test_python_ex5():
    '''Test for correct lines in junk output file'''
    sh_pywrapper.exec_python(python_line_block_list[4])
    assert(os.path.exists("junk.txt"))
    with open("junk.txt") as junk_file:
        junk_content = junk_file.readlines()
    assert(junk_content == ["Title: Alice's Adventures in Wonderland\n", "\n", "Author: Lewis Carroll\n"])
