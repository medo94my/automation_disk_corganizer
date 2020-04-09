import os 
import shutil
import time
# from tqdm.auto import tqdm
# from progress.bar import IncrementalBar
print('*'*50)
print('Welcome to Download File Organizer')
print('created by Ahmed Tawfik')
print('Email:medoroyalrma@gmail.com')
print('*'*50)
Appname=os.path.basename(__file__).split('.')
# current_dir= os.path.dirname(os.path.realpath(__file__))
Source=input('Choose your source file to orgainze:')
destination=input('Choose your destination folder or drive:') 
dict_file_type={
    'Pictures':('.jpg','.png','.jpeg','.gif','.svg'),
    'Media':('.mp3','.vlc','.wav','.mov','.mp4'),
    'Archive':('.zip','.rar','.7z','.tar'),
    'Document':('.pdf','.doc','.docx','.xlsx','.xls','.ppt','.pptx','.txt','csv'),
    'Applications':('.exe','.msi','.dmg','.iso','.deb','AppImage','run'),
    'Code':('.js','.html','.css','.py'),
    'Design':('.xd'),
    'General':('')
}
os.chdir(Source)
def final_files():
    files=list()
    for file in os.listdir():
        exe_file=Appname[0]+'.exe'
        if file != os.path.basename(__file__) and file != exe_file:
            if not os.path.isdir(file):
                files.append(file)
    return files
files=final_files()
def orgnize(folder_name, filename):
    folder=(os.path.join(destination,folder_name).strip())
    if not os.path.exists(folder):
        os.mkdir(folder)
    try:
        if os.path.exists(os.path.join(folder,filename)):
            t= input("file exists on the {} do like to replace it [Y/n]".format(folder))
            if t =='Y' or t =='y' :
                shutil.copy(filename,folder)
                print(filename,'=======> Done')
                os.remove(filename)
            else:
                pass
        else:
            shutil.move(filename,folder,)
        print(filename,'=======>', folder_name)
        # os.remove(filename)
    except :
        pass
def checking_files(dict_file_type,files):
    # bar = IncrementalBar('Organizing', max = len(files))
    for category , ext in dict_file_type.items():
        for filename in files:
            if filename.endswith(ext):
                # print('true',ext)
                orgnize(category,filename)
            
                # bar.next()


    # bar.finish()
# checking_files(dict_file_type,files)

    
if len(files) != 0:
    print('*'*50)
    checking_files(dict_file_type,files)
    print('Thank you for trying my Application')
    print('if you find it useful please share it :)')
    print('Bye ... Hope To See Again;) ')
    print('You Were Using our app',Appname[0].replace('_',' '))
    print('*'*50)

else:
    print('*'*50)
    print('Thank You For Choosing Us ')
    print('No files to organize')
    print('Bye ... Hope To See Again;) ')
    print('You Were Using our app',Appname[0].replace('_',' '))
    print('*'*50)

time.sleep(2)