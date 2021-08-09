import os
from agm_io_utils.io_utils import get_all_files_recursively_from_path
from agm_io_utils.io_utils import check_path_and_return_new_file_name_with_postfix
import unittest


class MyTestCase(unittest.TestCase):
    my_path = r"C:\Users\mtri\Documents\test"

    def test_check_path_and_return_new_file_name_with_postfix(self):
        res = check_path_and_return_new_file_name_with_postfix("testfile.test")
        self.assertEqual("", res)

    def test_get_all_files_recursively_from_path(self):
        res = get_all_files_recursively_from_path(self.my_path)
        self.assertTrue(res)
        for f in res:
            print(f)


if __name__ == '__main__':
    unittest.main()
