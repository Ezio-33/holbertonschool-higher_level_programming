#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_liste_vide(self):
        self.assertIsNone(max_integer([]))

    def test_liste_un_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_nombres_positifs(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_nombres_negatifs(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_nombres_melanges(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_nombres_dupliques(self):
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)

    def test_grands_nombres(self):
        self.assertEqual(max_integer([10**10, 10**11, 10**12]), 10**12)
