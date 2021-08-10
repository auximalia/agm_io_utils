from agm_io_utils.io_utils import get_all_files_recursively_from_path
from agm_io_utils.io_utils import get_all_files_recursively_from_path_with_statistics

if __name__ == '__main__':
    my_path = r"C:\Users\micro\OneDrive\Dokumente\test"
    result, stats = get_all_files_recursively_from_path_with_statistics(my_path,
                                                                        not_allowed_in_files_name_list=["Heaven", "Rain"],
                                                                        not_allowed_in_path_string_list=["Download", "Wall"],
                                                                        file_extensions=[".mp3", ".mv4"],
                                                                        must_be_a_part_of_files_name_list=["Collins", "Seriously", "Jacket"],
                                                                        also_look_for_name_hits_in_path=True)
    print(stats)
    for elem in result:
        print(elem)
