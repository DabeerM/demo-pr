import os

# Specify the directory path
path = os.getcwd()
file_name = 'File.txt'
msg = 'New file created!'

# Creating a file at specified folder
# join directory and file path
with open(os.path.join(path, file_name), 'w') as fp:
    # uncomment below line if you want to create an empty file
    fp.write(msg)