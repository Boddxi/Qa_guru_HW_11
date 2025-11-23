import os

def get_resource_path(filename):
    current_dir = os.path.dirname(__file__)
    resources_dir = os.path.join(current_dir, '..', 'resources')
    file_path = os.path.join(resources_dir, filename)
    absolute_path = os.path.abspath(file_path)
    return absolute_path