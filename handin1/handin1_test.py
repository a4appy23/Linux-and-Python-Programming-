import glob
import os

# Import pywrapper (complication due to dot in directory name)
import importlib
spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
sh_pywrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sh_pywrapper)

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    module.process = sh_pywrapper.create_process()
    module.commands_list = sh_pywrapper.parse('handin1.sh')
    module.base_dir = os.path.abspath(sh_pywrapper.get_cwd(process)).strip()
    print(module.commands_list)

def teardown_module(module):
    sh_pywrapper.kill_process(module.process)
    
def test_ex1():
    '''Test whether handin1 directory exists'''
    sh_pywrapper.run(process, commands_list[0])
    assert(os.path.exists(os.path.join(base_dir, "handin1")))
    assert(os.path.isdir(os.path.join(base_dir, "handin1")))

def test_ex2():
    '''Test whether handin1/test1 directory exists'''
    sh_pywrapper.run(process, commands_list[1])
    assert(os.path.exists(os.path.join(base_dir, "handin1/test1")))
    assert(os.path.isdir(os.path.join(base_dir, "handin1/test1")))
    # full_dir_name = sh_pywrapper.get_cwd(process)
    # base_name = os.path.basename(full_dir_name)
    # assert(base_name == 'handin1')

def test_ex3():
    '''Test whether m_scrambled has been correctly downloaded'''
    sh_pywrapper.run(process, commands_list[2])
    assert(os.path.exists(os.path.join(base_dir, "handin1/test1/m_scrambled.txt")))
    
def test_ex4():
    '''Test whether test1 was correctly copied into test2'''
    sh_pywrapper.run(process, commands_list[3])
    dir1 = os.path.join(base_dir, 'handin1/test1/')
    dir2 = os.path.join(base_dir, 'handin1/test2/')
    assert(os.path.exists(dir2))
    assert(os.path.isdir(dir2))
    content_test1 = [os.path.relpath(f, dir1) for f in glob.glob(dir1+'**')]
    content_test2 = [os.path.relpath(f, dir2) for f in glob.glob(dir2+'**')]
    assert(content_test1 == content_test2)
    
def test_ex5():
    '''Test whether find command was executed correctly'''
    output = "".join(sh_pywrapper.run(process, commands_list[4]))
    output = [f.strip() for f in output.split('\n') if f is not '']
    assert(output == ['.', './test1', './test1/m_scrambled.txt', './test2', './test2/m_scrambled.txt'])

def test_ex6():
    '''Test that the test2 directory was correctly removed'''
    sh_pywrapper.run(process, commands_list[5])
    assert(not os.path.exists(os.path.join(base_dir, "handin1/test2")))
    
def test_ex7():
    '''Test the cat command'''
    sh_pywrapper.run(process, commands_list[6])
    # No assertion done here - correct output is checked at the end

def test_ex8():
    '''Check unscrambled image against correct one'''
    sh_pywrapper.run(process, commands_list[7])

    assert(os.path.exists(os.path.join(base_dir, "handin1/test1/m.txt")))
    output_filename = os.path.join(base_dir, "handin1/test1/m.txt")
    output_file = open(output_filename)
    output = output_file.readlines()

    # Check that output has correct length
    newlines = len(output) == 150
    
    # Check that lines are unscrambled - i.e., in correct order (this is a hint! :)
    sh_outputs = sh_pywrapper.run(process, ["sort -nc " + output_filename])
    condition1 = (len(sh_outputs) == 1 and sh_outputs[0] == "")

    # Remove all whitespace and calculate checksum (for cases where first column was removed)
    import re
    import hashlib
    condition2 = (hashlib.md5(re.sub(r'\s+', '', ''.join(output)).encode('utf-8')).hexdigest() == "b89f40f9ca67d797c0808eee77a6820c")

    # Check that either condition is fulfilled
    assert condition1 or condition2
    
def test_ex9():
    '''Check one-liner'''
    
    # First remove the old version
    os.remove(os.path.join(base_dir, "handin1/test1/m.txt"))

    # Verify that command is a one-liner
    effective_command_lines = [command for command in commands_list[8] if command[0] != '#']
    assert(len(effective_command_lines) == 1)
    
    # Run command
    sh_pywrapper.run(process, commands_list[8])

    output_filename = os.path.join(base_dir, "handin1/test1/m.txt")
    output_file = open(output_filename)
    output = output_file.readlines()

    # Check that lines are unscrambled - i.e., in correct order (this is a hint! :)
    sh_outputs = sh_pywrapper.run(process, ["sort -nc " + output_filename])
    condition1 = (len(sh_outputs) == 1 and sh_outputs[0] == "")

    # Remove all whitespace and calculate checksum (for cases where first column was removed)
    import re
    import hashlib
    condition2 = (hashlib.md5(re.sub(r'\s+', '', ''.join(output)).encode('utf-8')).hexdigest() == "b89f40f9ca67d797c0808eee77a6820c")

    # Check that either condition is fulfilled
    assert condition1 or condition2

def test_ex10():
    '''Check cleanup'''
    sh_pywrapper.run(process, commands_list[9])
    assert(not os.path.exists(os.path.join(base_dir, "handin1")))

    
