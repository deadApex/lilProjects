from mega import Mega

mega = Mega() # Creates Mega.py instance

m = mega.login(email, password) # Logins in mega.co.nz api
m = mega.login() # login using a temporary anonymous account

details = m.get_user() # Gets user details

balance = m.get_balance() # Gets user balance (PRO ACCOUNTS ONLY)

quota = m.get_quota() # Account Disk Quota

# specify unit output kilo, mega, gig, else bytes will output
space = m.get_storage_space(kilo=True)

files = m.get_files() # Gets account files

file = m.upload('myfile.doc') # Upload a file
m.get_upload_link(file) # Gets upload link
# see mega.py for destination and filename options

public_exported_web_link = m.export('myfile.doc')
public_exported_web_link = m.export('my_mega_folder/my_sub_folder_to_share')
# e.g. https://mega.nz/#F!WlVl1CbZ!M3wmhwZDENMNUJoBsdzFng

folder = m.find('my_mega_folder')
# Excludes results which are in the Trash folder (i.e. deleted)
folder = m.find('my_mega_folder', exclude_deleted=True)

folder = m.find('my_mega_folder')
m.upload('myfile.doc', folder[0])

file = m.find('myfile.doc')
m.download(file)
m.download_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc')
m.download(file, '/home/john-smith/Desktop')
# specify optional download filename (download_url() supports this also)
m.download(file, '/home/john-smith/Desktop', 'myfile.zip')

m.import_public_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc')
folder_node = m.find('Documents')[1]
m.import_public_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc', dest_node=folder_node)

m.create_folder('new_folder')
m.create_folder('new_folder/sub_folder/subsub_folder')

file = m.find('myfile.doc')
m.rename(file, 'my_file.doc')