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

    def test_height_two_children(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.assertEqual(2,self.__BST.get_height())

    def test_height_left_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual(2,self.__BST.get_height())

    def test_height_right_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.assertEqual(2,self.__BST.get_height())

    def test_insert_value_already_in_tree(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(0)
        with self.assertRaises(ValueError):
            self.__BST.insert_element(0)
        self.assertEqual('[ 0, 5 ]', str(self.__BST))

    def test_insert_three_values(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.assertEqual('[ 20, 30, 40 ]',str(self.__BST))

    def test_insert_four_values(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 40 ]', str(self.__BST))

    def test_insert_five_values(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.assertEqual('[ 10, 20, 25, 30, 40 ]', str(self.__BST))

    def test_insert_six_values(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(35)
        self.assertEqual('[ 10, 20, 25, 30, 35, 40 ]',str(self.__BST))

    def test_insert_seven_values(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(35)
        self.__BST.insert_element(50)
        self.assertEqual('[ 10, 20, 25, 30, 35, 40, 50 ]',str(self.__BST))

    def test_height_three_levels(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.assertEqual(3,self.__BST.get_height())

    def test_height_of_three_root_left_child(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.assertEqual(3,self.__BST.get_height())

    def test_height_of_three_root_right_child(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(25)
        self.assertEqual(3,self.__BST.get_height())

    def test_insert_large_range(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(0)
        self.__BST.insert_element(-512)
        self.__BST.insert_element(782)
        self.assertEqual('[ -512, 0, 100, 782 ]',str(self.__BST))

    def test_insert_sorted_list(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.insert_element(4)
        self.__BST.insert_element(5)
        self.assertEqual(5,self.__BST.get_height())

    def test_insert_remove(self):
        self.__BST.insert_element(1)
        self.__BST.remove_element(1)
        self.assertEqual('[ ]',str(self.__BST))

    def test_insert_remove_height(self):
        self.__BST.insert_element(1)
        self.__BST.remove_element(1)
        self.assertEqual(0,self.__BST.get_height())

    def test_remove_from_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(5)
        self.assertEqual('[ ]', str(self.__BST))

    def test_height_remove_from_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(5)
        self.assertEqual(0, self.__BST.get_height())

    def test_remove_root_only_left_child(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(3)
        self.__BST.remove_element(5)
        self.assertEqual('[ 3 ]',str(self.__BST))

    def test_remove_root_only_left_child_height(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(3)
        self.__BST.remove_element(5)
        self.assertEqual(1,self.__BST.get_height())

    def test_remove_root_only_right_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.remove_element(10)
        self.assertEqual('[ 20 ]',str(self.__BST))

    def test_remove_root_only_right_child_height(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.remove_element(10)
        self.assertEqual(1,self.__BST.get_height())

    def test_remove_root_right_child_with_one_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(12)
        self.__BST.remove_element(15)
        self.assertEqual('[ 5, 10, 12 ]',str(self.__BST))

    def test_remove_root_right_child_with_one_child_height(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.insert_element(12)
        self.__BST.remove_element(15)
        self.assertEqual(2,self.__BST.get_height())

    def test_remove_right_child_with_two_children(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.__BST.insert_element(30)
        self.__BST.remove_element(20)
        self.assertEqual('[ 5, 10, 15, 30 ]',str(self.__BST))

    def test_remove_right_child_with_two_children_height(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(20)
        self.__BST.insert_element(15)
        self.__BST.insert_element(30)
        self.__BST.remove_element(20)
        self.assertEqual(3,self.__BST.get_height())

    def test_remove_root_left_child_with_one_child(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.remove_element(10)
        self.assertEqual('[ 5, 20, 30 ]',str(self.__BST))

    def test_remove_root_left_child_with_one_child_height(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(30)
        self.__BST.insert_element(5)
        self.__BST.remove_element(10)
        self.assertEqual(2,self.__BST.get_height())

    def test_remove_root_left_child_with_two_children(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.remove_element(10)
        self.assertEqual('[ 5, 15, 20, 30 ]',str(self.__BST))

    def test_remove_root_left_child_with_two_children_height(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.__BST.remove_element(10)
        self.assertEqual(3,self.__BST.get_height())

    def test_increasing_insert_height(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.insert_element(4)
        self.assertEqual(4,self.__BST.get_height())

    def test_remove_multiple_times(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.__BST.remove_element(25)
        self.__BST.remove_element(35)
        self.__BST.remove_element(20)
        self.assertEqual('[ 10, 15, 30, 40 ]',str(self.__BST))

    def test_remove_value_not_in_tree(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        with self.assertRaises(ValueError):
            self.__BST.remove_element(50)
        self.assertEqual('[ 10, 15, 20, 25, 30, 35, 40 ]',str(self.__BST))

#____________________________________________________________________________

    def test_in_order_only_root(self):
        self.__BST.insert_element(25)
        self.assertEqual('[ 25 ]',self.__BST.in_order())

    def test_pre_order_only_root(self):
        self.__BST.insert_element(25)
        self.assertEqual('[ 25 ]',self.__BST.pre_order())

    def test_post_order_only_root(self):
        self.__BST.insert_element(25)
        self.assertEqual('[ 25 ]',self.__BST.post_order())

    def test_in_order_two_levels(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.assertEqual('[ 10, 15, 25 ]',self.__BST.in_order())

    def test_pre_order_two_levels(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(35)
        self.__BST.insert_element(15)
        self.assertEqual('[ 25, 15, 35 ]',self.__BST.pre_order())

    def test_post_order_two_levels(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(35)
        self.__BST.insert_element(15)
        self.assertEqual('[ 15, 35, 25 ]',self.__BST.post_order())

    def test_in_order_three_levels(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.assertEqual('[ 10, 15, 20, 25, 30, 35, 40 ]',self.__BST.in_order())

    def test_pre_order_three_levels(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.assertEqual('[ 25, 15, 10, 20, 35, 30, 40 ]',
        self.__BST.pre_order())

    def test_post_order_three_levels(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.assertEqual('[ 10, 20, 15, 30, 40, 35, 25 ]',
        self.__BST.post_order())

    def test_in_order_root_and_left_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 5, 10 ]',self.__BST.in_order())

    def test_pre_order_root_and_left_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 10, 5 ]',self.__BST.pre_order())

    def test_post_order_root_and_left_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.assertEqual('[ 5, 10 ]',self.__BST.post_order())

    def test_in_order_root_and_right_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.assertEqual('[ 10, 15 ]',self.__BST.in_order())

    def test_pre_order_root_and_right_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.assertEqual('[ 10, 15 ]',self.__BST.pre_order())

    def test_post_order_root_and_right_child(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(15)
        self.assertEqual('[ 15, 10 ]',self.__BST.post_order())

    def test_in_order_with_left_grandchildren(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.assertEqual('[ 5, 10, 15, 20 ]',self.__BST.in_order())

    def test_pre_order_with_left_grandchildren(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.assertEqual('[ 20, 10, 5, 15 ]',self.__BST.pre_order())

    def test_post_order_with_left_grandchildren(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(15)
        self.assertEqual('[ 5, 15, 10, 20 ]',self.__BST.post_order())

    def test_in_order_with_right_grandchildren(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40)
        self.assertEqual('[ 20, 25, 30, 40 ]',self.__BST.in_order())

    def test_pre_order_with_right_grandchildren(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40)
        self.assertEqual('[ 20, 30, 25, 40 ]',self.__BST.pre_order())

    def test_post_order_with_right_grandchildren(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(30)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40)
        self.assertEqual('[ 25, 40, 30, 20 ]',self.__BST.post_order())

    def test_in_order_missing_one_node(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35) #35 has no left child
        self.__BST.insert_element(40)
        self.assertEqual('[ 10, 15, 20, 25, 35, 40 ]',self.__BST.in_order())

    def test_pre_order_missing_one_node(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.assertEqual('[ 25, 15, 10, 20, 35, 40 ]',self.__BST.pre_order())

    def test_post_order_missing_one_node(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.assertEqual('[ 10, 20, 15, 40, 35, 25 ]',self.__BST.post_order())

    def test_in_order_after_one_child_removal(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.remove_element(2)
        self.assertEqual('[ 1, 3 ]',self.__BST.in_order())

    def test_pre_order_after_one_child_removal(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.remove_element(2)
        self.assertEqual('[ 1, 3 ]',self.__BST.pre_order())

    def test_post_order_after_one_child_removal(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.remove_element(2)
        self.assertEqual('[ 3, 1 ]',self.__BST.post_order())

    def test_in_order_after_removal_with_two_children(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(2)
        self.__BST.insert_element(8)
        self.__BST.remove_element(5)
        self.assertEqual('[ 2, 8, 10 ]',self.__BST.in_order())

    def test_pre_order_after_removal_with_two_children(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(2)
        self.__BST.insert_element(8)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 8, 2 ]',self.__BST.pre_order())

    def test_post_order_after_removal_with_two_children(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(2)
        self.__BST.insert_element(8)
        self.__BST.remove_element(5)
        self.assertEqual('[ 2, 8, 10 ]',self.__BST.post_order())

    def test__in_order_removal_replaces_with_smallest_in_right_subtree(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(2)
        self.__BST.insert_element(8)
        self.__BST.insert_element(7)
        self.__BST.remove_element(5)
        self.assertEqual('[ 2, 7, 8, 10 ]',self.__BST.in_order())

    def test__pre_order_removal_replaces_with_smallest_in_right_subtree(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(2)
        self.__BST.insert_element(8)
        self.__BST.insert_element(7)
        self.__BST.remove_element(5)
        self.assertEqual('[ 10, 7, 2, 8 ]',self.__BST.pre_order())

    def test_post_order_removal_replaces_with_smallest_in_right_subtree(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(5)
        self.__BST.insert_element(2)
        self.__BST.insert_element(8)
        self.__BST.insert_element(7)
        self.__BST.remove_element(5)
        self.assertEqual('[ 2, 8, 7, 10 ]',self.__BST.post_order())

    def test_in_order_to_check_root_after_removal(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.__BST.remove_element(25)
        self.assertEqual('[ 10, 15, 20, 30, 35, 40 ]',self.__BST.in_order())

    def test_post_order_to_check_root_after_removal(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.__BST.remove_element(25)
        self.assertEqual('[ 10, 20, 15, 40, 35, 30 ]',self.__BST.post_order())

    def test_pre_order_to_check_root_after_removal(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(15)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.__BST.insert_element(35)
        self.__BST.insert_element(30)
        self.__BST.insert_element(40)
        self.__BST.remove_element(25)
        self.assertEqual('[ 30, 15, 10, 20, 35, 40 ]',self.__BST.pre_order())

    def test_in_order_insert_increasing(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.insert_element(4)
        self.__BST.insert_element(5)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]',self.__BST.in_order())

    def test_pre_order_insert_increasing(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.insert_element(4)
        self.__BST.insert_element(5)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]',self.__BST.pre_order())

    def test_post_order_insert_increasing(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.insert_element(4)
        self.__BST.insert_element(5)
        self.assertEqual('[ 5, 4, 3, 2, 1 ]',self.__BST.post_order())

    def test_in_order_insert_decreasing(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(4)
        self.__BST.insert_element(3)
        self.__BST.insert_element(2)
        self.__BST.insert_element(1)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]',self.__BST.in_order())

    def test_pre_order_insert_decreasing(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(4)
        self.__BST.insert_element(3)
        self.__BST.insert_element(2)
        self.__BST.insert_element(1)
        self.assertEqual('[ 5, 4, 3, 2, 1 ]',self.__BST.pre_order())

    def test_post_order_insert_decreasing(self):
        self.__BST.insert_element(5)
        self.__BST.insert_element(4)
        self.__BST.insert_element(3)
        self.__BST.insert_element(2)
        self.__BST.insert_element(1)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]',self.__BST.post_order())

if __name__ == '__main__':
    unittest.main()
