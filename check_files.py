import os

# back to parent location
os.chdir('..')

# print every files in one particular folder
for path in ['/lib']:
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            print(os.path.join(r, file))
