import unittest
import os.path
from bucket_collection import Bucket
from bucket_collection import BucketCollection

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

import json

class BucketTest(unittest.TestCase):

    def test_results_file_creation(self):
        "Tests that a result file is generated"
        self.assertTrue(os.path.isfile(results_filepath))

    def test_generic_bucket_existence(self):
        "Test that generic bucket was created"
        self.assertIn("*,*,*", results_file_content)

    def test_bucket_assignments(self):
        "Most specific"
        self.assertIn(
'''
    {
        "bucket": "Pearson,7,10_day",
        "purchases": [
            "99680,8193774926972,PEARSON,SNA,7,10_day,2017-07-10 07:07:11.587228"
        ]
    }
''', results_file_content)

if __name__ == "__main__":
    # don't think I should test the big files
    # buckets_file_name = "purchase_buckets.csv"
    # purchases_file_name = "purchase_data.csv"
    # results_filename = "results.json"

    buckets_file_name = "min_buckets.csv"
    purchases_file_name = "min_purchases.csv"
    results_filename = "min_results.json"

    bucket_collection = BucketCollection(buckets_file_name)
    bucket_collection.populate_buckets(purchases_file_name)
    # tried to test if values in JSON, but I'd do too much digging; checkig if text in file
    # results_json = bucket_collection.to_json()
    bucket_collection.to_file(results_filename)

    results_filepath = os.path.join(os.path.dirname(__file__), results_filename)
    results_file =  open(results_filepath, 'r')
    results_file_content = results_file.read()
    unittest.main()
    results_file.close()
