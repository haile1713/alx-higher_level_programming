#!/usr/bin/python3
"""tests made for rectangles"""


import unittest
import contextlib
import importlib
import models.base
import models.rectangle


Rect = models.rectangle.Rectangle


class rectangle_tests(unittest.TestCase):
        """yay, rectangle testing"""
            def setUp(self):
                        """refresh for each test"""
                                importlib.reload(models.base)
                                        importlib.reload(models.rectangle)

                                            def test_TooFewArgs(self):
                                                        """Test too few args"""
                                                                err = "missing heigt arg fool"
                                                                        with self.assertRaises(TypeError, msg=err):
                                                                                        Rect(1)

                                                                                            def def test_TooManyArgs(self):
                                                                                                        """Test too many args"""
                                                                                                                err = "too many arguments man"
                                                                                                                        with self.assertRaises(TypeError, msg=err):
                                                                                                                                        Rect(1, 1, 1, 1, 1, 1)

                                                                                                                                            def test_Area(self):
                                                                                                                                                        """check if area is working"""
                                                                                                                                                                testrect = Rect(7, 6)
                                                                                                                                                                        with self.subTest():
                                                                                                                                                                                        self.assertEqual(testrect.area(), 42)
                                                                                                                                                                                                testrect.width = 4
                                                                                                                                                                                                        testrect.height = 5
                                                                                                                                                                                                                with self.subTest():
                                                                                                                                                                                                                                self.assertEqual(testrect.area(), 20)
