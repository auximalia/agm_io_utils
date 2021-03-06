# agm_io_utils

This package provides some more complex functions e.g. for looking for files and creating unique filenames.  

Install:  
```
pip install agm_io_utils
```
**Example 1:**
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
**Example 2:**

Explanation: Sometimes you get a path to a file through user input. Now the following has to be done:

1. Check whether the file type specified by the user is actually the correct one (e.g. '.txt')
2. Test whether the file actually exists
3. To save the original file from being changed, find a new file name for the target file.  
   A postfix can either be appended here or, if no postfix is specified, a time stamp is automatically appended. In any case, it must be ensured that the target file does not yet exist in the file system. 
   If so, count up the file name with an additional index.
```
from agm_io_utils import io_utils

    path_to_file = r"C:\Users\micro\OneDrive\Dokumente\clean_this_xminds.txt"  
    
    new_filename = io_utils.check_path_and_return_new_file_name_with_postfix(path=path_to_file, extension="txt", postfix="tested")
    print(new_filename)
```
Output:
```
C:\Users\micro\OneDrive\Dokumente\clean_this_xminds_tested_06.txt
```



