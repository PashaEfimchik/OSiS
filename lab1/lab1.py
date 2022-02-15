import os
import sys

def func(root):
    file_count = 0
    subdirs_count = 0
    save_file = open('lab1.txt', 'w+')
    for path, dirs, files in os.walk(root):
        for file in files:
            print(os.path.join(path, file))
            save_file.write(os.path.join(path, file) + '\n')
            file_count += 1
        for dir in dirs:
            print(os.path.join(path, dir))
            save_file.write(os.path.join(path, dir) + '\n')
            subdirs_count += 1
    print("\nTotal number of files: ", file_count)
    print("Total number of subdirectories: ", subdirs_count)
    save_file.write("\nTotal number of files: " + str(file_count) + "\nTotal number of subdirectories: " + str(subdirs_count))

if len (sys.argv) > 1:
    func(str(sys.argv[1]))
else:
    func("/home")
