from glob import glob 
import os 

list_all_files = glob('store/*.svg')
for file in list_all_files:
    new_file = file.replace('_lowerthan001', '_AF < 1%').replace("_from001to005", "_1% < AF < 5%")
    os.rename(file, new_file)