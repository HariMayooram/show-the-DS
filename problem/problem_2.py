import os

def find_files(suffix, path):
    if suffix == '':
        return 'Please enter a valid suffix.'
    
    if os.path.isdir(path):
        list_for_path = []
        dir_entries = os.listdir(path)
        for entry in dir_entries:
            path_to_enter = os.path.join(path, entry)
            if os.path.isdir(path_to_enter):
                list_for_path += find_files(suffix, path_to_enter)
            elif os.path.isfile(path_to_enter):
                list_for_path.append(path_to_enter) if path_to_enter.endswith(suffix) else None
        
        return list_for_path
    else: 
        return 'Invalid path provided'

print(find_files('', 'testdir')) #Returns a message asking user to enter a suffix
print(find_files('.c', 'test')) #Returns a message telling the user that the path is wrong
print(find_files('.py', 'testdir')) #Returns an empty list
print(find_files('.c', 'testdir')) #Returns a list of all the '.c' files
print(find_files('.h', 'testdir')) #Returns a list of all the '.h' files