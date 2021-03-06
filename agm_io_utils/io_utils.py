# -*- coding: utf-8 -*-
import os
from collections import defaultdict
from typing import List
from datetime import datetime


def check_path_and_return_new_file_name_with_postfix(path: str, extension: str = "", postfix: str = "") -> str:
    # 1. check extension
    if extension and not path.endswith(extension):
        print(f"Error -> File: '{path}' is not a {extension} file.")
        return ""
    # 2. file exists?
    if not os.path.exists(path):
        print(f"Error -> File: '{path}' could not be found.")
        return ""
    # 3. decompose path
    path, file_name = os.path.split(path)
    name, ext = os.path.splitext(file_name)
    # 4. create postfix if not exists as timestamp
    if not postfix:
        postfix = datetime.now().strftime("%Y-%m-%d %a %H.%M.%S")
    new_path = os.path.join(path, f"{name}_{postfix}{ext}")
    counter = 0
    while os.path.exists(new_path):
        counter += 1
        new_path = os.path.join(path, f"{name}_{postfix}_{str(counter).rjust(2, '0')}{ext}")
        if counter >= 1000:
            print("Error: A new file name cannot be generated. All constructed names already exist. Abort after 1,000 unsuccessful attempts.")
            return ""
    # 5. return new path
    return new_path


def get_all_files_recursively_from_path(path: str,
                                        file_extensions: List[str] = None,
                                        not_allowed_in_files_name_list: List[str] = None,
                                        must_be_a_part_of_files_name_list: List[str] = None,
                                        not_allowed_in_path_string_list: List[str] = None):
    # version from August 2021
    def __ist_tag_from_list_in_name(_name: str, _list_with_tags: List[str]) -> bool:
        for elem in _list_with_tags:
            if elem in _name:
                return True
        return False

    # 0. initialize and format the parameter lists
    if file_extensions:
        file_extensions = [elem.upper() for elem in file_extensions]
    if not_allowed_in_files_name_list:
        not_allowed_in_files_name_list = [elem.upper() for elem in not_allowed_in_files_name_list]
    if must_be_a_part_of_files_name_list:
        must_be_a_part_of_files_name_list = [elem.upper() for elem in must_be_a_part_of_files_name_list]
    if not_allowed_in_path_string_list:
        not_allowed_in_path_string_list = [elem.upper() for elem in not_allowed_in_path_string_list]

    list_with_filenames = []
    # 1. iterate through all folders recursively
    for (dir_path, dir_names, file_names) in os.walk(path):
        # 0. process the path filter
        if not_allowed_in_path_string_list:
            jump_over = False
            for not_allowed_in_path_string in not_allowed_in_path_string_list:
                if not_allowed_in_path_string in dir_path.upper():
                    jump_over = True
                    break
            if jump_over:
                continue

        for a_file_name in file_names:

            # 1.1 split filename in name and extension and upper it
            name, extension = os.path.splitext(a_file_name)
            name = name.upper()
            extension = extension.upper()

            # 1.2 process the filters
            if file_extensions and extension not in file_extensions:
                continue
            if not_allowed_in_files_name_list and __ist_tag_from_list_in_name(name, not_allowed_in_files_name_list):
                continue
            if must_be_a_part_of_files_name_list and not __ist_tag_from_list_in_name(name, must_be_a_part_of_files_name_list):
                continue

            # 1.3 compile the abs path and add it to the result list
            list_with_filenames.append(os.path.join(dir_path, a_file_name))

    # 2. return the sorted list
    return sorted(list_with_filenames)


def get_all_files_recursively_from_path_with_statistics(path: str,
                                                        file_extensions: List[str] = None,
                                                        not_allowed_in_files_name_list: List[str] = None,
                                                        must_be_a_part_of_files_name_list: List[str] = None,
                                                        not_allowed_in_path_string_list: List[str] = None,
                                                        also_look_for_name_hits_in_path: bool = False):
    my_stats = defaultdict(int)

    # version from August 2021
    def __ist_tag_from_list_in_name(_name: str, _list_with_tags: List[str], stats: bool = False) -> str:
        for elem in _list_with_tags:
            if elem in _name:
                if stats:
                    my_stats[f"{elem} - in filename"] += 1
                return str(elem)
        return ""

    # 0. initialize and format the parameter lists
    if file_extensions:
        file_extensions = [elem.upper() for elem in file_extensions]
    if not_allowed_in_files_name_list:
        not_allowed_in_files_name_list = [elem.upper() for elem in not_allowed_in_files_name_list]
    if must_be_a_part_of_files_name_list:
        must_be_a_part_of_files_name_list = [elem.upper() for elem in must_be_a_part_of_files_name_list]
    if not_allowed_in_path_string_list:
        not_allowed_in_path_string_list = [elem.upper() for elem in not_allowed_in_path_string_list]

    list_with_filenames = []
    # 1. iterate through all folders recursively
    for (dir_path, dir_names, file_names) in os.walk(path):
        # 0. process the path filter
        if not_allowed_in_path_string_list:
            jump_over = False
            for not_allowed_in_path_string in not_allowed_in_path_string_list:
                if not_allowed_in_path_string in dir_path.upper():
                    jump_over = True
                    break
            if jump_over:
                continue
        if also_look_for_name_hits_in_path:
            current_elem = __ist_tag_from_list_in_name(dir_path.upper(), must_be_a_part_of_files_name_list)
            if current_elem:
                for each_file_name in file_names:
                    a_name, a_extension = os.path.splitext(each_file_name)
                    a_name = a_name.upper()
                    a_extension = a_extension.upper()
                    # 1.2 process the filters
                    if file_extensions and a_extension not in file_extensions:
                        continue
                    if not_allowed_in_files_name_list and __ist_tag_from_list_in_name(a_name, not_allowed_in_files_name_list):
                        continue
                    list_with_filenames.append(os.path.join(dir_path, each_file_name))
                    my_stats[f"{current_elem} - in path"] += 1
                continue

        for a_file_name in file_names:

            # 1.1 split filename in name and extension and upper it
            name, extension = os.path.splitext(a_file_name)
            name = name.upper()
            extension = extension.upper()

            # 1.2 process the filters
            if file_extensions and extension not in file_extensions:
                continue
            if not_allowed_in_files_name_list and __ist_tag_from_list_in_name(name, not_allowed_in_files_name_list):
                continue
            if must_be_a_part_of_files_name_list and not __ist_tag_from_list_in_name(name, must_be_a_part_of_files_name_list, stats=True):
                continue

            # 1.3 compile the abs path and add it to the result list
            list_with_filenames.append(os.path.join(dir_path, a_file_name))

    # 2. return the sorted list
    return sorted(list_with_filenames), sorted(my_stats.items(), key=lambda x: x[0])


def get_unique_filename(path_with_file_name):
    path, basename = os.path.split(path_with_file_name)
    filename, file_extension = os.path.splitext(basename)
    counter = 0
    while os.path.exists(path_with_file_name):
        counter += 1
        path_with_file_name = os.path.join(path, filename + " " + str(counter).rjust(2, '0') + file_extension)
    return path_with_file_name
