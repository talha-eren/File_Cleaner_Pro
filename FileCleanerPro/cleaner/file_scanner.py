import os 
import datetime 

def scan_folder(folder_path, extensions=None, older_than_days=None, smaller_than_kb=None):
    result = []
    now = datetime.datetime.now()
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file)

        if not os.path.isfile(file_path):
            continue 
        

        if extensions and not file.endswith(tuple(extensions)):
            continue
        
        if older_than_days:
            file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

            if(now-file_mtime).days<older_than_days:
                continue
        
        if smaller_than_kb:
            size_kb = os.path.getsize(file_path)/1024
            if size_kb>smaller_than_kb :
                continue
        result.append(file_path)
    return result 