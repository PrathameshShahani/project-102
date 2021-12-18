import os
import shutil
import sys
import dropbox
from dropbox.client import DropboxClient

path = input("enter the name of the directory to be sorted :- ")

list_of_files = os.listdir(path)

for file in list_of_files:
    name, ext = os.path.splitext(file)

    ext = ext[1:]

    if ext == '':
        continue

    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

access_token, local_directory, dropbox_destination = sys.argv[1:4]

client = DropboxClient(access_token)

# enumerate local files recursively
for root, dirs, files in os.walk(local_directory):

    for filename in files:

        # construct the full local path
        local_path = os.path.join(root, filename)

        # construct the full Dropbox path
        relative_path = os.path.relpath(local_path, local_directory)
        dropbox_path = os.path.join(dropbox_destination, relative_path)

        # upload the file
        with open(local_path, 'rb') as f:
            client.put_file(dropbox_path, f)