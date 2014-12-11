import unittest
import code_sample_2

class TestCodeSample2(unittest.TestCase):

    def testOutput(self):
        results = code_sample_2.run_overlap_report()
        expected = {
            1: 500400,
            2: 54971,
            3: 23726,
            4: 13045,
            5: 6216,
            6: 2754,
            7: 860,
            8: 566,
            9: 212,
            10: 119
        }

        self.assertEqual(expected[1], results[1])
        self.assertEqual(expected[2], results[2])
        self.assertEqual(expected[3], results[3])
        self.assertEqual(expected[4], results[4])
        self.assertEqual(expected[5], results[5])
        self.assertEqual(expected[6], results[6])
        self.assertEqual(expected[7], results[7])
        self.assertEqual(expected[8], results[8])
        self.assertEqual(expected[9], results[9])
        self.assertEqual(expected[10], results[10])

if __name__ == "__main__":
    unittest.main()
