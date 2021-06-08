import unittest
from main import IcaoApp


class TestStringMethods(unittest.TestCase):

    def test_distance(self):

        lat1 = 39.91722222222222
        lon1 = 25.23638888888889

        lat2 = 40.2
        lon2 = 25.881666666666668
        self.assertEqual(IcaoApp.calc_dist(lat1, lat2, lon1, lon2), 34.169557849651135)


    def test_distance1(self):

        lat1 = 53.63038888888889 #53.630389
        lon1 = 9.988227777777777 #9.988228

        lat2 = 48.42515833333333 #48.425158
        lon2 = 10.931763888888888 #10.931764
        self.assertEqual(IcaoApp.calc_dist(lat1, lat2, lon1, lon2), 315)

if __name__ == '__main__':
    unittest.main()
