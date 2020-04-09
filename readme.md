# Disk Orgnizer with python
 
 this application have a simple idea of orgnizing the fills that being unsorted in user download or hard disk , this application seek to orginze your files with just one run 


 starting py importing the os moudle 

 ```python 
 import os # to be able to navigate the os 
 import shutil # for easy file copying and deleting
 import time # just control the time console stay open after code finishes
```
 as this file orgnize in the directory its in 

getting the location of the current dir and the file name for :

```python
Appname=os.path.basename(__file__).split('.')
current_dir= os.path.dirname(os.path.realpath(__file__))
```

creating a dectionary to hold the files extention

```python 
dict_file_type={
    'Pictures':('.jpg','.png','.jpeg','.gif','.svg'),
    'Media':('.mp3','.vlc','.wav','.mov','.mp4'),
    'Archive':('.zip','.rar','.7z','.tar'),
    'Document':('.pdf','.doc','.docx','.xlsx','.xls','.ppt','.pptx','.txt'),
    'Applications':('.exe','.msi','.dmg','.iso','.deb'),
    'Code':('.js','.html','.css','.py'),
    'Design':('.xd')
}
```

this code is to exclude all folder and the script file for this code
```python 
def final_files():
    files=list()
    for file in os.listdir(current_dir):
        exe_file=Appname[0]+'.exe'
        if file != os.path.basename(__file__) and file != exe_file:
            if not os.path.isdir(file):
                files.append(file)
    return files
```
then assining the value that return from the function:
```python 
files=final_files()
```
create this function to check on the file and distribute them by extension and decied to which category they belong and gave the extension that is not coverd inthe dictionary to folder named General, then after passing the file checking then handling them to the function organize(category, filename):
passingnto the function the category of the file and the file name 
```python
def checking_files(dict_file_type,files):
    # bar = IncrementalBar('Organizing', max = len(files))
    for category , ext in dict_file_type.items():
        for filename in files:
            if filename !='clean_disk.py':
                if filename.endswith(ext):
                    orgnize(category,filename)
                else:
                    orgnize('General',filename)
```

after organize function recieves the required parameters \
1.  it will check if tthe folder the we are going to create exist or not  if not it will create it so next time the code runs we wont have any errors
2. after folder checking done will copy the file using shutil to the folder that the script create it earlier and then remove it from the main directory 
```python
def orgnize(folder_name, filename):
    # print("i ran")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    try:
        shutil.copy(filename,folder_name)
        print(filename,'=======> Done')
        os.remove(filename)
    except :
        pass
```