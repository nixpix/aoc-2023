# Handling input and output

def read_file_to_list(filename, strip_new_lines):
  with open(filename) as file:
    content = []
    if strip_new_lines:
      for line in file:
          content.append(line.rstrip())
    else:
      content = file.readlines()
    return content

def read_file_to_string(filename):
  with open(filename) as file:
    content = file.read()
    return content

def write_to_file(filename, content):
  with open(filename, 'w') as writer:
    writer.writelines(content)