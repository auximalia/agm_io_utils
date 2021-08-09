from agm_io_utils.io_utils import get_all_files_recursively_from_path

if __name__ == '__main__':
    my_path = r"C:\Users\mtri\Documents\test"
    result = get_all_files_recursively_from_path(my_path)
    for r in result:
        print(r)