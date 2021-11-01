import os
import string
import argparse

def rename(path,old_keyword,new_keyword):
    for file in os.listdir(path):
        tmp = file
        if old_keyword in tmp:
            print(f'found "{tmp}"')
            new_name = tmp.replace(old_keyword,new_keyword)
            print(f'change to "{new_name}"')
            os.rename(os.path.join(path,tmp), os.path.join(path,new_name))
    
    print('Done.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Rename Files')
    parser.add_argument('path', metavar='PATH', type=str,help='Input file directory')
    parser.add_argument('old_name', metavar='old name', type=str, help='Old file names')
    parser.add_argument('new_name', metavar='new name', type=str, help='New file names')
    input_dir = parser.parse_args().path
    old_name = parser.parse_args().old_name
    new_name = parser.parse_args().new_name
    rename(input_dir,old_name,new_name)
    