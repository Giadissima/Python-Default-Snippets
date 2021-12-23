from os.path import join, isabs

# join two path if the second path is relative, otherwise return only the secind path
def check_if_abs(arg_to_join, possible_abs_path):
    if(isabs(possible_abs_path)):
        return possible_abs_path
    return join(arg_to_join, possible_abs_path)


from os.path import isfile

def create_multiple_file(*paths):
  for path in paths:
    if not isfile(path): 
      f = open(path, "w")
      f.close()