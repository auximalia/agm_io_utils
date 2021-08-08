# agm_io_utils

This package provides some more complex functions e.g. for looking for files and creating unique filenames.  

Install:  
```
pip install agm_io_utils
```
Example:
```
from agm_io_utils import io_utils

p = r"C:\Users\micro\OneDrive\Dokumente"
result_list = io_utils.get_all_files_recursively_from_path(path=p,
                                                              file_extensions=[".xmind"],
                                                              not_allowed_in_files_name_list=["test", "optional"],
                                                              not_allowed_in_path_string_list=["duplicate"],
                                                              must_be_a_part_of_files_name_list=["python"])
for file_name in result_list:
    print(file_name)
```
Output:  
```
2 files found in folder 'C:\Users\micro\OneDrive\Dokumente'
C:\Users\micro\OneDrive\Dokumente\Python.xmind
C:\Users\micro\OneDrive\Dokumente\wmr\Wissen\Python.xmind
```