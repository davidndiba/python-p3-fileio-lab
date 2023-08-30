import tempfile
from file_io import write_file, append_file, read_file
import uuid
import os

'''Function write_files() in file_io.py'''
def test_write_file():

  #Create temp directory to write file to and see if it exits.
  with tempfile.TemporaryDirectory() as tmp_dirname:
    filename = str(uuid.uuid4())
    expected_file_content = str(uuid.uuid4())
    write_file(f'{tmp_dirname}/{filename}',expected_file_content)
    assert os.path.exists(f'{tmp_dirname}/{filename}.txt') == True

    # Check file content
    file_content = ''
    with open(f'{tmp_dirname}/{filename}.txt') as f:
      file_content = f.read()

      assert file_content == expected_file_content
def test_write_file():
    '''file_io.py: write_file() takes a filename and input and writes the input to a file.'''
    write_file('lib/testing/write.txt', 'Hello, World!')
    f = open('lib/testing/write.txt', 'r')
    assert(f.read() == 'Hello, World!')
    os.remove('lib/testing/write.txt')

'''Function append_file() in file_io.py'''
def test_append_to_file():
    '''file_io.py: append_file() takes an existing filename and input and writes the input to the file.'''
    write_file('lib/testing/append.txt', 'Hello, World!\n')
    append_file('lib/testing/append.txt', 'How are you doing today?')

