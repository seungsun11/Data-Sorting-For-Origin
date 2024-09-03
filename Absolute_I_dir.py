import os
import Absoute_I_onefile


def apply_absolute_in_dir (path):
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
            original_file = path+ "\\" + file
            Absoute_I_onefile.apply_absolute_values(original_file, new_file)
            
            
dir_path = "C:\\Users\\user\\Desktop\\측정 데이터\\0717_CTM (Al2O3 , Bi2O3, BN)\\BN 5.6 , Bi2O3 9.6 , Al2O3 20cy\\2-13"
        
apply_absolute_in_dir(dir_path)