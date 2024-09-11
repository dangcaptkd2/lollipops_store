from glob import glob 
import os 

list_all_files = glob('store/*.svg')
for file in list_all_files:
    # new_file = file.replace('_lowerthan001', '_AF < 1%').replace("_from001to005", "_1% < AF < 5%")
    new_file = file.replace("_AF < 1%", "_AF<0.01").replace("_1% < AF < 5%", "_0.01<AF<0.05")
    os.rename(file, new_file)