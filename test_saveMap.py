import json
import unittest


class ChallengeMapBuilder(unittest.TestCase):
    def saveMap(self):
        mapData = {
            'name': "Suhaimi",
            'map': [
                    1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1
                    ],
            'start': [0, 0],
            'end': [2, 2],
            'index': 1
        }
        mapData = json.dumps(mapData)
        result = flask1.saveMap(mapData)
        self.assertEqual(result, "Map saved successfully")


if __name__ == '__main__':
    unittest.main()
