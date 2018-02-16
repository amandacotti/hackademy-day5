import unittest
import production

class TestProduction(unittest.TestCase):
    def test_remove_duplicate(self):
        input = [1,1,2,2]
        output =[1,2]
        self.assertListEqual(output,production.remove_duplicate(input))

if __name__ == '__main__':
    unittest.main()
