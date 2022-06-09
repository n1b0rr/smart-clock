import global_variable_test as global_variable
from to_do import *
from menu import Menu
import unittest


class TestRemoveToDo(unittest.TestCase):

    def test_0(self):
        global_variable.to_do_list = {0: "douchen", 1: "Eten", 2: "Gamen", 3: "studeren"}
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
    
    
class TestMenu(unittest.TestCase):
    def test_add_function(self):
        myMenu = Menu(5)
        myMenu.add_function("f1", None)
        myMenu.add_function("f2", None)
        myMenu.add_function("f3", None)
        self.assertEqual(3, myMenu.size())
        
    
    def test_delete_function(self):
        myMenu = Menu(5)
        myMenu.add_function("f1", None)
        myMenu.add_function("f2", None)
        myMenu.add_function("f3", None)
        
        myMenu.delete_function("f1")
        myMenu.delete_function("f2")
        myMenu.delete_function("f3")
        self.assertEqual(0, myMenu.size())
    
    def test_up_down(self):
        myMenu = Menu(5)
        myMenu.add_function("f1", None)
        myMenu.add_function("f2", None)
        myMenu.add_function("f3", None)
        
        self.assertEqual(myMenu.get_cursor(), 0)
        myMenu.up()
        self.assertEqual(myMenu.get_cursor(), 0)
        myMenu.down()
        self.assertEqual(myMenu.get_cursor(), 1)
        myMenu.down()
        self.assertEqual(myMenu.get_cursor(), 2)
        myMenu.down()
        self.assertEqual(myMenu.get_cursor(), 2)
        myMenu.up()
        myMenu.up()
        self.assertEqual(myMenu.get_cursor(), 0)
        

if __name__ == '__main__':
    unittest.main()