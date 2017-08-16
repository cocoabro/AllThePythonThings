import shutil
import os

source = '/mnt/c/Users/rmcelvenny/Downloads/'
zipFiles = '/mnt/c/Users/rmcelvenny/Google Drive/DownloadsBKUP/Zip/'
pdfFiles = '/mnt/c/Users/rmcelvenny/Google Drive/DownloadsBKUP/PDF/'
installerFiles = '/mnt/c/Users/rmcelvenny/Google Drive/DownloadsBKUP/Installers/'
docFiles = '/mnt/c/Users/rmcelvenny/Google Drive/DownloadsBKUP/Docs/'
execFiles = '/mnt/c/Users/rmcelvenny/Google Drive/DownloadsBKUP/Executables/'
excelFiles = '/mnt/c/Users/rmcelvenny/Google Drive/DownloadsBKUP/Excel/'
imageFiles = '/mnt/c/Users/rmcelvenny/Google Drive/DownloadsBKUP/Images/'
pythonFiles = '/mnt/c/Users/rmcelvenny/Google Drive/DownloadsBKUP/Python'

# list out the files within the directory. 
files = os.listdir(source) 


# loop through the files (in the os.listdir)
for f in files:
    if f.endswith(".zip") or f.endswith(".rar") or f.endswith(".tar.gz") or f.endswith("gzip"):
        shutil.move(source + f, zipFiles)
        print(f + ' moved successfully')
    
    if f.endswith(".png") or f.endswith(".jpg") or f.endswith("gif") or f.endswith("JPG"):
        shutil.move(source + f, imageFiles)
        print(f + ' moved successfully')

    if f.endswith(".py"): 
        shutil.move(source + f, pythonFiles)
        print(f + ' moved successfully')
    
    if f.endswith(".msi"): 
        shutil.move(source + f, installerFiles)
        print(f + ' moved successfully')

    if f.endswith(".pdf"):
        shutil.move(source + f, pdfFiles)
        print(f + ' moved successfully')
        
    
    if f.endswith(".exe"): 
        shutil.move(source + f, execFiles)
        print(f + ' moved successfully')
    
    if f.endswith(".doc") or f.endswith(".docx"):
        shutil.move(source + f, docFiles)
        print(f + ' moved successfully')
    
    if f.endswith(".xlsx") or f.endswith(".csv"):
        shutil.move(source + f, excelFiles)
        print(f + ' moved successfully')   