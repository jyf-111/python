import unittest
from name_function import get_formatted_name,get_formatted_name2

class NamesTestCase(unittest.TestCase):
    """测试name_function"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name2('J','Y','F')
        self.assertEqual(formatted_name,'J Y F')
        
if __name__ == '__main__':
    unittest.main()