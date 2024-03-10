#!/usr/bin/python3
"""test for FileStorage"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8


class TestFileStorage(unittest.TestCase):
    """this will test the FileStorage"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """test all"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test new"""
        storage = FileStorage()
        obj = storage.all()
        bm = BaseModel()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        storage.new(bm)
        self.assertIsNotNone(obj[key])

    def test_save(self):
        """test save"""
        storage = FileStorage()
        bm = BaseModel()
        bm.save()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIsNotNone(storage.all()[key])

    def test_reload(self):
        """test reload"""
        storage = FileStorage()
        bm = BaseModel()
        bm.save()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        storage.reload()
        self.assertIsNotNone(storage.all()[key])

    def test_save_file(self):
        """test save file"""
        storage = FileStorage()
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_file(self):
        """test reload file"""
        storage = FileStorage()
        bm = BaseModel()
        bm.save()
        storage.reload()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIsNotNone(storage.all()[key])

    def test_reload_empty(self):
        """test reload empty"""
        storage = FileStorage()
        self.assertIsNone(storage.reload())

    def test_reload_no_file(self):
        """test reload no file"""
        storage = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        self.assertIsNone(storage.reload())


if __name__ == "__main__":
    unittest.main()
