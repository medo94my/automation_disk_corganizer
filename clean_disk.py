import os 
import shutil
from pathlib import Path
import time
# from tqdm.auto import tqdm
from progress.bar import IncrementalBar
print('*'*50)
print('Welcome to Download File Organizer')
print('created by Ahmed Tawfik')
print('Email:medoroyalrma@gmail.com')
print('*'*50)
Appname=os.path.basename(__file__).split('.')
current_dir= os.path.dirname(os.path.realpath(__file__))
dict_file_type={
    'Pictures':('.jpg','.png','.jpeg','.gif','.svg'),
    'Media':('.mp3','.vlc','.wav','.mov','.mp4'),
    'Archive':('.zip','.rar','.7z','.tar'),
    'Document':('.pdf','.doc','.docx','.xlsx','.xls','.ppt','.pptx','.txt'),
    'Applications':('.exe','.msi','.dmg','.iso','.deb'),
    'Code':('.js','.html','.css','.py'),
    'Design':('.xd')
}
def final_files():
    files=list()
    for file in os.listdir(current_dir):
        if file != os.path.basename(__file__) and file != 'env':
            if not os.path.isdir(file):
                files.append(file)
    return files
files=final_files()
def orgnize(folder_name, filename):
    # print("i ran")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    try:
        shutil.copy(filename,folder_name)
        os.remove(filename)
    except Exception as e:
        print(e)
def checking_files(dict_file_type,files):
    bar = IncrementalBar('Organizing', max = len(files))
    for category , ext in dict_file_type.items():
        for filename in files:
            if filename !='clean_disk.py':
                if filename.endswith(ext):
                    orgnize(category,filename)
                    bar.next()

    bar.finish()
if __name__=='__main__':
    
    if len(files) != 0:
        checking_files(dict_file_type,files)
        print('Thank you for trying my Application')
        print('if you find it useful please share it :)')
        print('Bye ... Hope To See Again;) ')
        print('You Were Using our app',Appname[0].replace('_',' '))
    else:
        print('Thank You For Choosing Us ')
        print('No files to organize')
        print('Bye ... Hope To See Again;) ')
        print('You Were Using our app',Appname[0].replace('_',' '))

