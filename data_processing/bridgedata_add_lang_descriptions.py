import os
import sys

def insert_lang_file(root_dir, lang_description):
    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Check if 'traj0' directory is found
        for dirname in dirnames:
            if 'traj' in dirname and "group" not in dirname:
                traj_path = os.path.join(dirpath, dirname)
                lang_file_path = os.path.join(traj_path, 'lang.txt')
                
                # Write the language description to lang.txt
                with open(lang_file_path, 'w') as lang_file:
                    lang_file.write(lang_description)
                    
                print(f'Inserted lang.txt into {traj_path}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <root_directory> <language_description>")
        sys.exit(1)
    
    root_directory = sys.argv[1]
    language_description = sys.argv[2]
    
    insert_lang_file(root_directory, language_description)

