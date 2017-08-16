import shutil
import os

source = '/mnt/c/Users/rmcelvenny/Google Drive/'
docFiles = '/mnt/c/Users/rmcelvenny/Google Drive/Docs/'
sheetsFiles = '/mnt/c/Users/rmcelvenny/Google Drive/Sheets/'
gSlidesFiles = '/mnt/c/Users/rmcelvenny/Google Drive/Slides/'

# list out the files within the directory. 
files = os.listdir(source) 


# loop through the files (in the os.listdir)
for f in files:
    if f.endswith(".gdoc") or f.endswith(".doc") or f.endswith(".docx"):
        shutil.move(source + f, docFiles)
        print(f + ' moved successfully')
    
    if f.endswith(".gsheet") or f.endswith(".xlsx"):
        shutil.move(source + f, sheetsFiles)
        print(f + ' moved successfully')

    if f.endswith(".gslides"):
        shutil.move(source + f, gSlidesFiles)
        print(f + ' moved successfully')
