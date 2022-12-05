from os.path import join, isabs

# join two path if the second path is relative, otherwise return only the secind path
def check_if_abs(arg_to_join, possible_abs_path):
    if(isabs(possible_abs_path)):
        return possible_abs_path
    return join(arg_to_join, possible_abs_path)


from os import makedirs
from os.path import dirname, exists, isabs, isfile, join

def create_multiple_file(*paths):
  for path in paths:
    if(isfile(path)): continue
    
    dir_file = dirname(path)
    try:
      if not exists(dir_file): 
        makedirs(dir_file)
    
      f = open(path, "w")
      f.close()
    except PermissionError:
      print("errore di permesso nell'accedere al file")

# s = string to search into file
def searching_string_in_file(path, s):
  with open(path, "r") as txt_file:
    if str(s) in txt_file.readlines(): return True
  return False