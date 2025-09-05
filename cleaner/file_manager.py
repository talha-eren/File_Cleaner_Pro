import os 
import shutil
import zipfile

def delete_files(file_list):
    for file_path in file_list:
        if os.path.isfile(file_path):
            os.remove(file_path)
    return True


def archive_files(file_list,archive_folder):

    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    zip_path = os.path.join(archive_folder,"archive.zip")

    
    
    
    
         
    with zipfile.ZipFile(zip_path,"a") as zipf:
        for file_path in file_list:
            if os.path.isfile(file_path):
                filename = os.path.basename(file_path)
                zipf.write(file_path,filename)
                os.remove(file_path)
    
    return True 
