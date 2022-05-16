import shutil, os

# Os module can interact with the Operating System
# Shutil module can do things with files

def ord_file(sursa_fisier_dir, destinatia_fisier_dir):
    sursa_dir = sursa_fisier_dir
    destinatia_dir = destinatia_fisier_dir


    file_names = os.listdir(sursa_dir)

    for file_name in file_names:
        if os.path.join(sursa_dir, file_name).endswith('.mp3' or 'm4a' or 'wav'):
            shutil.move(os.path.join(sursa_dir, file_name), os.path.join(destinatia_dir, 'audios'))

        if os.path.join(sursa_dir, file_name).endswith('.mp4' or '.avi' or 'mov'):
            shutil.move(os.path.join(sursa_dir, file_name), os.path.join(destinatia_dir, 'videos'))

        if os.path.join(sursa_dir, file_name).endswith('.zip'):
            shutil.move(os.path.join(sursa_dir, file_name), os.path.join(destinatia_dir, 'zip'))

        if os.path.join(sursa_dir, file_name).endswith('.pdf' or '.doc' or '.xlsx' or 'pwp'):
            shutil.move(os.path.join(sursa_dir, file_name), os.path.join(destinatia_dir, 'Documents'))

        if os.path.join(sursa_dir, file_name).endswith('.jpg' or '.png'):
            shutil.move(os.path.join(sursa_dir, file_name), os.path.join(destinatia_dir, 'pictures'))

        if os.path.join(sursa_dir, file_name).endswith('.exe'):
            shutil.move(os.path.join(sursa_dir, file_name), os.path.join(destinatia_dir, 'Other'))

        print("success!!!!!")



ord_file('C:\\Users\\user\\Downloads', 'C:\\Users\\user\\Downloads')

# To change the directory use the 'chdir()' funtion
# To see the current working directory, use the 'getcwd()' function

#print(os.getcwd())
#os.chdir('C:\\Users\\mlora\\Downloads')
#os.mkdir('example')
#os.rename('example','example2')
#os.remove('desktop.ini')
#os.rmdir('example2')
#print(os.listdir())


#Se poate lucra cu biblioteca - mp3 to audios ex.