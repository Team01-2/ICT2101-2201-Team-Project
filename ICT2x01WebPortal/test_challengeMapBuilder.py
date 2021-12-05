import json
import unittest
import flask1
from modules import CRUDdbFunc


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


class ChallengeMapBuilder(unittest.TestCase):
    def test_saveMap(self):
        CRUDdbFunc.init_db()
        mapData1 = {
            'name': "Suhaimi1",
            'map': [],
            'start': [],
            'end': [],
            'index': 1
        }
        mapData2 = {
            'name': "Suhaimi2",
            'map': [],
            'start': [],
            'end': [],
            'index': 2
        }
        mapData3 = {
            'name': "Suhaimi3",
            'map': [],
            'start': [],
            'end': [],
            'index': 3
        }
        mapData4 = {
            'name': "Suhaimi4",
            'map': [],
            'start': [],
            'end': [],
            'index': 4
        }
        mapData1 = json.dumps(mapData1)
        mapData2 = json.dumps(mapData2)
        mapData3 = json.dumps(mapData3)
        mapData4 = json.dumps(mapData4)
        self.assertEqual(flask1.saveMap(mapData1), "Map saved successfully")
        self.assertEqual(flask1.saveMap(mapData2), "Map saved successfully")
        self.assertEqual(flask1.saveMap(mapData3), "Map saved successfully")
        self.assertEqual(flask1.saveMap(mapData4), "Map saved unsuccessfully")

    def test_loadMap(self):
        CRUDdbFunc.init_db()
        data = flask1.loadMap()
        self.assertEqual(validateJSON(data), True)


    def test_deleteMap(self):
        CRUDdbFunc.init_db()
        mapIndex1 = {
            'index': 1,
        }
        mapIndex2 = {
            'index': 2,
        }
        mapIndex3 = {
            'index': 3,
        }
        mapIndex4 = {
            'index': 4,
        }
        mapIndex1 = json.dumps(mapIndex1)
        mapIndex2 = json.dumps(mapIndex2)
        mapIndex3 = json.dumps(mapIndex3)
        mapIndex4 = json.dumps(mapIndex4)
        self.assertEqual(flask1.deleteMap(mapIndex1), "Map deleted successfully")
        self.assertEqual(flask1.deleteMap(mapIndex2), "Map deleted successfully")
        self.assertEqual(flask1.deleteMap(mapIndex3), "Map deleted successfully")
        self.assertEqual(flask1.deleteMap(mapIndex4), "Map deleted unsuccessfully")

    def test_createMap(self):
        CRUDdbFunc.init_db()
        mapData1 = {
            'name': "Suhaimi1",
            'map': [],
            'start': [],
            'end': [],
            'index': 1
        }
        mapData2 = {
            'name': "Suhaimi2",
            'map': [],
            'start': [],
            'end': [],
            'index': 2
        }
        mapData3 = {
            'name': "Suhaimi3",
            'map': [],
            'start': [],
            'end': [],
            'index': 3
        }
        mapData4 = {
            'name': "Suhaimi4",
            'map': [],
            'start': [],
            'end': [],
            'index': 4
        }
        self.assertEqual(flask1.createMap(1, mapData1), "Map created successfully")
        self.assertEqual(flask1.createMap(2, mapData2), "Map created successfully")
        self.assertEqual(flask1.createMap(3, mapData3), "Map created successfully")
        self.assertEqual(flask1.createMap(4, mapData4), "Map created unsuccessfully")


if __name__ == '__main__':
    unittest.main()