import os
import Data_Merge
import Data_Merge_only_I_V
import Data_Merge_only_G_V

def Data_Merge_files (input, path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    try:
        os.mkdir(path+"\output")
    except:
        pass

    for file in files:
        print(file)
        name = file.split('.')[0]
        ext = file.split('.')[1]
        if ext == 'xls':
            new_file = path+"\output\\"+name + ".xlsx"
            
            if input == 1:
                print(path)
                Data_Merge.Data_Merge_file(path + "\\" + file, new_file)
            elif input == 2:
                Data_Merge_only_I_V.Data_Merge_file_I_V(path + "\\" + file, new_file)
            elif input == 3:
                Data_Merge_only_G_V.Data_Merge_file_G_V(path + "\\" + file, new_file)
                
        

