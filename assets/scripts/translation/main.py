import sys
import argparse
import os
from core import translate

USAGE = '''todo
    
'''

def write_in_chunks(f,pos,data):
    f.seek(pos)
    f.write(data)

def read_in_chunks(f, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = f.read(chunk_size)
        if not data:
            break
        yield data

def translate_all(src_dir,dst_dir):
    #loop through files in this directory, looking for .md files
    for file in os.listdir(src_dir ):
        name = file.split('.')[0]
        suffix = file.split('.')[1]
        if(suffix == 'md' and name.endswith('_en') ):
            #create dst folder
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            #read file
            filepath = src_dir+'/'+file
            print(f"read file: ",name, "| size: ", {os.path.getsize(filepath)} )
            
            filepath_en = dst_dir+'/'+name+"_en."+suffix
            print(filepath_en)
            if os.path.exists(filepath_en):
                os.remove(filepath_en)
            
            #read file
            fread = open(file=filepath,mode="r",encoding="utf-8")
            #write file
            fwrite = open(file=filepath_en, mode="wb")
            #copy front matter


            # pos = 0
            for piece in read_in_chunks(fread):
                print(type(piece))
                print(piece)
                piece.replace('\n','%%')
                print("--------------------------------------")
                # data = translate(piece)
                # print(data)
                # write_in_chunks(fwrite,pos,data)
                # pos+=1024;
        
            fread.close()
            fwrite.close()

def main():
    if(len(sys.argv) < 2):
        print(USAGE)
        return 1
    else:
        src_path = os.path.abspath(sys.argv[1])
        if not os.path.exists(src_path):
                print("Source folder doesn't exist")
                return 1
        src_path = os.path.abspath(src_path);        
        dst_path = os.path.abspath(sys.argv[2])
        translate_all(src_path,dst_path)

if __name__ == '__main__':
    main()