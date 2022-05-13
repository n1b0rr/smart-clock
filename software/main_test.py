import global_variable_test as global_variable
from to_do import *
import unittest


class TestRemoveToDo(unittest.TestCase):

    def test_0(self):
        self.assertEqual(remove(0), {1: 'Eten', 2: 'Gamen', 3: 'studeren'})
        global_variable.to_do_list = {0: "douchen", 1: "Eten", 2: "Gamen", 3: "studeren"}

    def test_1(self):
        self.assertEqual(remove(1), {0: 'douchen', 2: 'Gamen', 3: 'studeren'})
        global_variable.to_do_list = {0: "douchen", 1: "Eten", 2: "Gamen", 3: "studeren"}

    def test_2(self):
        self.assertEqual(remove(2), {0: 'douchen', 1: 'Eten', 3: 'studeren'})
        global_variable.to_do_list = {0: "douchen", 1: "Eten", 2: "Gamen", 3: "studeren"}

    def test_3(self):
        self.assertEqual(remove(-1), 2)

    def test_4(self):
        self.assertEqual(remove(10), 2)

    def test_5(self):
        self.assertEqual(remove(None), 3)

    def test_6(self):
        self.assertEqual(remove("0"), 3)
    
    
    
    
    



if __name__ == '__main__':
    unittest.main()