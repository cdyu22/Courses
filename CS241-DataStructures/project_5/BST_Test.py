import unittest
from Binary_Search_Tree import Binary_Search_Tree

class Binary_Search_Tree_Tester(unittest.TestCase):

    def setUp(self):
        self.__BST = Binary_Search_Tree()

    def test_empty_BST_string(self):
        self.assertEqual('[ ]', str(self.__BST))

    def test_height_empty(self):
        self.assertEqual(0,self.__BST.get_height())

    def test_insert_once(self):
        self.__BST.insert_element(0)
        self.assertEqual('[ 0 ]',str(self.__BST))

    def test_height_one(self):
        self.__BST.insert_element(5)
        self.assertEqual(1,self.__BST.get_height())

    def test_insert_negative(self):
        self.__BST.insert_element(-5)
        self.assertEqual('[ -5 ]',str(self.__BST))

    def test_insert_twice(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        self.assertEqual('[ 0, 5 ]', str(self.__BST))

    def test_insert_twice_height(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        self.assertEqual(2,self.__BST.get_height())

    def test_left_left_balance(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        self.assertEqual(2,self.__BST.get_height())

    def test_remove_from_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(5)
        self.assertEqual('[ ]', str(self.__BST))

    def test_height_remove_from_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(5)
        self.assertEqual(0, self.__BST.get_height())

    def test_insert_value_already_in_tree(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        with self.assertRaises(ValueError):
            self.__BST.insert_element(0)
        self.assertEqual('[ 0, 5 ]', str(self.__BST))

    def test_insertion_removal_string(self):
        self.__BST.insert_element(10)
        self.__BST.remove_element(10)
        self.assertEqual('[ ]', str(self.__BST))

    def test_insertion_removal_height(self):
        self.__BST.insert_element(10)
        self.__BST.remove_element(10)
        self.assertEqual(0, self.__BST.get_height())

    def test_two_insertions_one_removal_string(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.remove_element(0)
        self.assertEqual('[ 10 ]',str(self.__BST))

    def test_two_insertions_one_removal_string(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.remove_element(0)
        self.assertEqual(1,self.__BST.get_height())


#Imbalance with Matching Sign___________________________________________________
    def test_left_left_insertion_height(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        self.assertEqual(2, self.__BST.get_height())

    def test_left_left_insertion_in_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        self.assertEqual('[ 0, 5, 10 ]', self.__BST.in_order())

    def test_left_left_insertion_pre_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        self.assertEqual('[ 5, 0, 10 ]',self.__BST.pre_order())

    def test_left_left_insertion_post_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        self.assertEqual('[ 0, 10, 5 ]',self.__BST.post_order())

    def test_right_right_insertion_height(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(5)
        self.__BST.insert_element(10)
        self.assertEqual(2, self.__BST.get_height())

    def test_right_right_insertion_in_order(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(5)
        self.__BST.insert_element(10)
        self.assertEqual('[ 0, 5, 10 ]',self.__BST.in_order())

    def test_right_right_insertion_pre_order(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(5)
        self.__BST.insert_element(10)
        self.assertEqual('[ 5, 0, 10 ]',self.__BST.pre_order())

    def test_right_right_insertion_post_order(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(5)
        self.__BST.insert_element(10)
        self.assertEqual('[ 0, 10, 5 ]',self.__BST.post_order())

    def test_single_rotation_right_to_left_carryover(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.assertEqual(3,self.__BST.get_height())

    def test_single_rotation_right_to_left_carryover_in_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.assertEqual('[ 5, 10, 15, 20, 25, 30 ]',self.__BST.in_order())

    def test_single_rotation_right_to_left_carryover_pre_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.assertEqual('[ 20, 10, 5, 15, 25, 30 ]',self.__BST.pre_order())

    def test_single_rotation_right_to_left_carryover_post_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.assertEqual('[ 5, 15, 10, 30, 25, 20 ]',self.__BST.post_order())

    def test_single_rotation_left_to_right_carryover_height(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual(3,self.__BST.get_height())

    def test_single_rotation_left_to_right_carryover_in_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 5, 10, 15, 20, 25, 30 ]',self.__BST.in_order())

    def test_single_rotation_left_to_right_carryover_pre_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 15, 10, 5, 25, 20, 30 ]',self.__BST.pre_order())

    def test_single_rotation_left_to_right_carryover_post_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 5, 10, 20, 30, 25, 15 ]',self.__BST.post_order())

#Imbalance with Different Signs
    def test_left_right_insertion_height(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(0)
        self.__BST.insert_element(5)
        self.assertEqual(2,self.__BST.get_height())

    def test_left_right_insertion_in_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(0)
        self.__BST.insert_element(5)
        self.assertEqual('[ 0, 5, 10 ]',self.__BST.in_order())

    def test_left_right_insertion_pre_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(0)
        self.__BST.insert_element(5)
        self.assertEqual('[ 5, 0, 10 ]',self.__BST.pre_order())

    def test_left_right_insertion_post_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(0)
        self.__BST.insert_element(5)
        self.assertEqual('[ 0, 10, 5 ]',self.__BST.post_order())

    def test_right_left_insertion_height(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual(2,self.__BST.get_height())

    def test_right_left_insertion_in_order(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 0, 5, 10 ]',self.__BST.in_order())

    def test_right_left_insertion_pre_order(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 5, 0, 10 ]',self.__BST.pre_order())

    def test_right_left_insertion_post_order(self):
        self.__BST.insert_element(0)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 0, 10, 5 ]',self.__BST.post_order())

    def test_double_rotation_right_to_left_carryover_height(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.assertEqual(3,self.__BST.get_height())

    def test_double_rotation_right_to_left_carryover_in_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.assertEqual('[ 5, 10, 15, 20, 25, 30 ]',self.__BST.in_order())

    def test_double_rotation_right_to_left_carryover_pre_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.assertEqual('[ 15, 10, 5, 25, 20, 30 ]',self.__BST.pre_order())

    def test_double_rotation_right_to_left_carryover_post_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.assertEqual('[ 5, 10, 20, 30, 25, 15 ]',self.__BST.post_order())

    def test_double_rotation_left_to_right_carryover_height(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.assertEqual(3,self.__BST.get_height())

    def test_double_rotation_left_to_right_carryover_in_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.assertEqual('[ 5, 10, 15, 20, 25, 30 ]',self.__BST.in_order())

    def test_double_rotation_left_to_right_carryover_pre_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.assertEqual('[ 20, 10, 5, 15, 25, 30 ]', self.__BST.pre_order())

    def test_double_rotation_left_to_right_carryover_post_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.assertEqual('[ 5, 15, 10, 30, 25, 20 ]', self.__BST.post_order())

#______________________________________________________________________________
    def test_same_sign_remove_left_heavy_height(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.remove_element(20)
        self.assertEqual(2,self.__BST.get_height())

    def test_same_sign_remove_left_heavy_in_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.remove_element(20)
        self.assertEqual('[ 5, 10, 15 ]',self.__BST.in_order())

    def test_same_sign_remove_left_heavy_pre_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.remove_element(20)
        self.assertEqual('[ 10, 5, 15 ]',self.__BST.pre_order())

    def test_same_sign_remove_left_heavy_post_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(5)
        self.__BST.remove_element(20)
        self.assertEqual('[ 5, 15, 10 ]',self.__BST.post_order())

    def test_same_sign_remove_right_heavy_height(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual(2, self.__BST.get_height())

    def test_same_sign_remove_right_heavy_in_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 15, 20 ]',self.__BST.in_order())

    def test_same_sign_remove_right_heavy_pre_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 15, 10, 20 ]',self.__BST.pre_order())

    def test_same_sign_remove_right_heavy_post_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 20, 15 ]',self.__BST.post_order())

    def test_remove_left_heavy_left_carryover_height(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(15)
        self.__BST.remove_element(35)
        self.assertEqual(3,self.__BST.get_height())

    def test_remove_left_heavy_left_carryover_in_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(15)
        self.__BST.remove_element(35)
        self.assertEqual('[ 5, 10, 15, 20, 25, 30 ]',self.__BST.in_order())

    def test_remove_left_heavy_left_carryover_pre_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(15)
        self.__BST.remove_element(35)
        self.assertEqual('[ 20, 10, 5, 15, 25, 30 ]',self.__BST.pre_order())

    def test_remove_left_heavy_left_carryover_post_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(15)
        self.__BST.remove_element(35)
        self.assertEqual('[ 5, 15, 10, 30, 25, 20 ]',self.__BST.post_order())

    def test_remove_right_heavy_left_carryover_height(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(35)
        self.__BST.remove_element(5)
        self.assertEqual(3,self.__BST.get_height())

    def test_remove_right_heavy_left_carryover_in_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(35)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 15, 20, 25, 30, 35 ]',self.__BST.in_order())

    def test_remove_right_heavy_left_carryover_pre_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(35)
        self.__BST.remove_element(5)
        self.assertEqual('[ 25, 15, 10, 20, 30, 35 ]',self.__BST.pre_order())

    def test_remove_right_heavy_left_carryover_post_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(35)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 20, 15, 35, 30, 25 ]',self.__BST.post_order())

#______________________________________________________________________________

    def test_opposite_signs_remove_left_heavy_height(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(20)
        self.assertEqual(2,self.__BST.get_height())

    def test_opposite_signs_remove_left_heavy_in_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(20)
        self.assertEqual('[ 5, 10, 15 ]',self.__BST.in_order())

    def test_opposite_signs_remove_left_heavy_pre_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(20)
        self.assertEqual('[ 10, 5, 15 ]',self.__BST.pre_order())

    def test_opposite_signs_remove_left_heavy_post_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(20)
        self.assertEqual('[ 5, 15, 10 ]',self.__BST.post_order())

    def test_remove_left_heavy_right_carryover_height(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(20)
        self.__BST.remove_element(35)
        self.assertEqual(3,self.__BST.get_height())

    def test_remove_left_heavy_right_carryover_in_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(20)
        self.__BST.remove_element(35)
        self.assertEqual('[ 5, 10, 15, 20, 25, 30 ]',self.__BST.in_order())

    def test_remove_left_heavy_right_carryover_pre_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(20)
        self.__BST.remove_element(35)
        self.assertEqual('[ 15, 10, 5, 25, 20, 30 ]',self.__BST.pre_order())

    def test_remove_left_heavy_right_carryover_post_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(20)
        self.__BST.remove_element(35)
        self.assertEqual('[ 5, 10, 20, 30, 25, 15 ]',self.__BST.post_order())


#______________________________________________________________________________

    def test_opposite_signs_remove_right_heavy_height(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual(2,self.__BST.get_height())

    def test_opposite_signs_remove_right_heavy_in_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 15, 20 ]',self.__BST.in_order())

    def test_opposite_signs_remove_right_heavy_pre_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 15, 10, 20 ]',self.__BST.pre_order())

    def test_opposite_signs_remove_right_heavy_post_order(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 20, 15 ]',self.__BST.post_order())

    def test_remove_right_heavy_carryover_height(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(25)
        self.__BST.insert_element(35)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual(3,self.__BST.get_height())

    def test_remove_right_heavy_carryover_in_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(25)
        self.__BST.insert_element(35)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 15, 20, 25, 30, 35 ]',self.__BST.in_order())

    def test_remove_right_heavy_carryover_pre_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(25)
        self.__BST.insert_element(35)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 25, 15, 10, 20, 30, 35 ]',self.__BST.pre_order())

    def test_remove_right_heavy_carryover_post_order(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.insert_element(25)
        self.__BST.insert_element(35)
        self.__BST.insert_element(20)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 20, 15, 35, 30, 25 ]',self.__BST.post_order())

#______________________________________________________________________________

    def test_double_removal_height(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(50)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(20)
        self.assertEqual(4, self.__BST.get_height())

    def test_double_removal_in_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(50)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(20)
        self.assertEqual('[ 5, 10, 15, 25, 30, 35, 40, 45, 50, 55, 60 ]',
        self.__BST.in_order())

    def test_double_removal_pre_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(50)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(20)
        self.assertEqual('[ 40, 25, 10, 5, 15, 35, 30, 50, 45, 55, 60 ]',
        self.__BST.pre_order())

    def test_double_removal_post_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(50)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(20)
        self.assertEqual('[ 5, 15, 10, 30, 35, 25, 45, 60, 55, 50, 40 ]',
        self.__BST.post_order())

    def test_two_rotations_two_carryovers_height(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(25)
        self.__BST.remove_element(40)
        self.assertEqual(3,self.__BST.get_height())

    def test_two_rotations_two_carryovers_in_order(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(25)
        self.__BST.remove_element(40)
        self.assertEqual('[ 5, 10, 15, 20, 25, 30, 35 ]',
        self.__BST.in_order())

    def test_two_rotations_two_carryovers_pre_order(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(25)
        self.__BST.remove_element(40)
        self.assertEqual('[ 20, 10, 5, 15, 30, 25, 35 ]',
        self.__BST.pre_order())

    def test_two_rotations_two_carryovers_post_order(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(25)
        self.__BST.remove_element(40)
        self.assertEqual('[ 5, 15, 10, 25, 35, 30, 20 ]',
        self.__BST.post_order())

    def test_two_removals_height(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(40)
        self.__BST.remove_element(45)
        self.assertEqual(4,self.__BST.get_height())

    def test_two_removals_in_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(40)
        self.__BST.remove_element(45)
        self.assertEqual('[ 5, 10, 15, 20, 25, 30, 35, 50, 55, 60 ]',
        self.__BST.in_order())

    def test_two_removals_pre_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(40)
        self.__BST.remove_element(45)
        self.assertEqual('[ 25, 10, 5, 15, 20, 50, 35, 30, 55, 60 ]',
        self.__BST.pre_order())

    def test_two_removals_post_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(40)
        self.__BST.remove_element(45)
        self.assertEqual('[ 5, 20, 15, 10, 30, 35, 60, 55, 50, 25 ]',
        self.__BST.post_order())

    def test_two_removals_two_rotations_height(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(25)
        self.__BST.remove_element(5)
        self.assertEqual(4,self.__BST.get_height())

    def test_two_removals_two_rotations_in_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(25)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 15, 20, 30, 35, 40, 45, 50, 55, 60 ]',
        self.__BST.in_order())

    def test_two_removals_two_rotations_pre_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(25)
        self.__BST.remove_element(5)
        self.assertEqual('[ 30, 15, 10, 20, 50, 40, 35, 45, 55, 60 ]',
        self.__BST.pre_order())

    def test_two_removals_two_rotations_post_order(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(25)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 20, 15, 35, 45, 40, 60, 55, 50, 30 ]',
        self.__BST.post_order())

    def test_to_list_method_empty(self):
        self.assertEqual([],self.__BST.to_list())

    def test_to_list_method(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(10)
        self.__BST.insert_element(40)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(5)
        self.__BST.insert_element(50)
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(60)
        self.__BST.remove_element(25)
        self.__BST.remove_element(5)
        self.assertEqual([10,15,20,30,35,40,45,50,55,60],self.__BST.to_list())

if __name__ == '__main__':
    unittest.main()
