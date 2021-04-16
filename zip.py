import os
import shutil

def create_zip(source,destination):
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source)

    

    shutil.make_archive(archive_to,'zip',archive_from,archive_to)
    shutil.move(f'{os.getcwd()}\\{archive_to}.zip',destination)
    
source = ''
destination = ''

while source == '':
    source = input('What is the path to your folder? (Include folder itself) ')

while destination == '':
    destination = input('What is the path you want the zipped folder to be created? ')



create_zip(source,destination)

print(f'File zipped and stored at {destination}')
