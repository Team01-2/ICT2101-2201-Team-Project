import json
import unittest
from modules import CRUDdbFunc


def validateTuple(Data):
    if type(Data) is tuple:
        return True

def validateList(listData):
    if type(listData) is list:
        return True


class Database(unittest.TestCase):
    def test_insertMap(self):
        CRUDdbFunc.init_db()
        self.assertEqual(CRUDdbFunc.insert_cmap("a", [], [], []), "Inserted successfully")
        self.assertEqual(CRUDdbFunc.insert_cmap("a", [], [], []), "Inserted unsuccessfully") #same map name will throw an error

    def test_selectMap(self):
        CRUDdbFunc.init_db()
        self.assertEqual(validateTuple(CRUDdbFunc.select_cmap()), True)
        CRUDdbFunc.insert_cmap("b", [], [], [])
        CRUDdbFunc.insert_cmap("c", [], [], [])
        data = CRUDdbFunc.select_cmap()
        self.assertEqual(validateTuple(data), True)

    def test_insertCmdHistory(self):
        CRUDdbFunc.init_db()
        self.assertEqual(CRUDdbFunc.insert_comhist("Suhaimi", []), "Inserted successfully")

    def test_selectCmdHistory(self):
        CRUDdbFunc.init_db()
        CRUDdbFunc.select_comhist()
        self.assertEqual(validateList(CRUDdbFunc.select_comhist()), True)

    def test_deleteMap(self):
        CRUDdbFunc.init_db()
        self.assertEqual(CRUDdbFunc.delete_cmap("a"), "Deleted map successfully")

if __name__ == '__main__':
    unittest.main()