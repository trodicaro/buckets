import unittest
import os.path
from solution import sort_buckets

# test for a very specific purchase record that it gets assigned to the specific bucket
  # eg: 99680,8193774926972,PEARSON,SNA,7,10_day,2017-07-10 07:07:11.587228 => "Pearson,7,10_day"
  # edge case when name includes dash
  # edge case when name includes space
  # edge case when name has lower and upper
  # edge case repeated bucket
# test for duration specific:
  # eg: 98835,6544295182149,MACMILLAN,CLE,4,40_day,2017-01-10 14:08:55.562501 => "Macmillan,*,40_day"
# test for price specific:
  # eg: 98795,9277080469051,MCGRAW-HILL,MSP,6,120_day,2017-04-02 11:05:31.561470 => "McGraw-Hill,6,*"
# test for only publisher specific:
  # =>
# test for catch-all bucket

class BucketTest(unittest.TestCase):

    def test_results_file_creation(self):
        "Tests that a result file is generated"
        self.assertTrue(os.path.isfile(TESTDATA_FILENAME))

    # def test_keys(self):
    #     "Test that generic bucket was created"
    #     self.assertIn("*,*,*", results_file)

if __name__ == '__main__':
    sort_buckets('min_buckets.csv', 'min_purchases.csv')
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'min_results.json')
    unittest.main()
