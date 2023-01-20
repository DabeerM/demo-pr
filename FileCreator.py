import os

# Specify the directory path
Path = os.getcwd()

# Creating a file at specified folder
# join directory and file path
for i in range(20):
    filee_name = 'File' + str(i) + '.txt'
    mSg = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'

    with open(os.path.join(Path, filee_name), 'w') as fp:
        # uncomment below line if you want to create an empty file
        fp.write(mSg)