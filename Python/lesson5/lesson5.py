import os

#1
new_folder = "new_directory"
os.makedirs(new_folder, exist_ok=True)
print(f"Folder '{new_folder}' created.")

#2
folder_path = "new_directory"
try:
    os.rmdir(folder_path)
    print(f"Folder '{folder_path}' has been deleted.")
except OSError as e:
    print(f"Error: {e}")

# #3 ,4
directory = 'new_directory'
file_name = 'new_file.txt'
file_path = os.path.join(directory, file_name)

# Create a new file in the specified folder
with open(file_path, 'w') as file:
    file.write('This is a new file created in the local folder.')

print(f"File '{file_path}' has been created.")

#5
file_path = 'new_directory/new_file.txt'

try:
    os.remove(file_path)
    print(f"File '{file_path}' has been deleted.")
except OSError as e:
    print(f"Error: {e}")

#6
directory = 'new_directory'
try:
    files_and_dirs = os.listdir(directory)
    print(f"Files and directories in '{directory}':")
    for item in files_and_dirs:
        print(item)
except FileNotFoundError:
    print(f"Error: The directory '{directory}' does not exist.")

#7

current_directory = os.getcwd()
print(f"The full path of the current folder is: {current_directory}")