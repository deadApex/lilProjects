from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 

# For using listdir() 
import os 


# Below code does the authentication 
# part of the code 
gauth = GoogleAuth() 

# Creates local webserver and auto 
# handles authentication. 
gauth.LocalWebserverAuth()	 
drive = GoogleDrive(gauth) 

# replace the value of this variable 
# with the absolute path of the directory 
path = r"C:\senhas"

# Create a file and write "Hello World" inside it
# file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
# file1.SetContentString('Hello World!') # Set content of the file from given string.
# file1.Upload()


# iterating thought all the files/folder 
# of the desired directory 
'''
for x in os.listdir(path): 

	f = drive.CreateFile({'title': x}) 
	f.SetContentFile(os.path.join(path, x)) 
	f.Upload() 

	# Due to a known bug in pydrive if we 
	# don't empty the variable used to 
	# upload the files to Google Drive the 
	# file stays open in memory and causes a 
	# memory leak, therefore preventing its 
	# deletion 
	f = None
'''
# Auto-iterate through all files in the root folder.
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))