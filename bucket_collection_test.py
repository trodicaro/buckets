import unittest
import os.path
import json
from bucket_collection import Bucket
from bucket_collection import BucketCollection

class BucketTest(unittest.TestCase):

    def test_results_file_creation(self):
        "Tests that a result file is generated"
        self.assertTrue(os.path.isfile(results_filepath))

    def test_generic_bucket_existence(self):
        "Test that generic bucket was created"
        self.assertIn("*,*,*", results_file_content)

    def test_file_content_is_valid_json(self):
        print(results_json.__len__())

    @unittest.skip("pending")
    def buckets_generate_in_desired_order(self):
        pass
        # check *,*,* is last bucket
        # check first bucket in file is  first in results

    def test_a_purchase_is_found_only_once(self):
        pass
        # going through all json content and ensure no repeats

    def test_purchases_ordered_by_order_id(self):
        pass
        # in a specific bucket check that the order_id's are going up

    def test_publisher_price_duration_bucket(self):
        pass
        # "Most specific"
        # eg: 99680,8193774926972,PEARSON,SNA,7,10_day,2017-07-10 07:07:11.587228 => "Pearson,7,10_day"

    def test_publisher_duration_bucket(self):
        pass
        # eg: 98835,6544295182149,MACMILLAN,CLE,4,40_day,2017-01-10 14:08:55.562501 => "Macmillan,*,40_day"

    def test_publisher_price_bucket(self):
        pass
       # eg: 98795,9277080469051,MCGRAW-HILL,MSP,6,120_day,2017-04-02 11:05:31.561470 =>   "McGraw-Hill,6,*"

    def test_price_duration_bucket(self):
        pass
        # eg: 98819,9793386372887,PENGUIN RANDOMHOUSE,DTW,3,90_day,2017-07-14 14:06:01.562089 => "*,3,90_day"

    def test_publisher_only_bucket(self):
        pass
        # eg: 98771,1899596499745,PEARSON,MIA,3,110_day,2017-05-23 09:16:43.560846 => "Pearson,*,*"

    def test_publisher_only_bucket_with_upper_lower_letters(self):
        pass
      # eg: 98775,7192583653601,SCIPUB,BOS,8,140_day,2017-08-03 14:02:28.560950 => "SciPub,*,*"

    def test_publisher_only_bucket_with_dash(self):
        pass
        # eg: => "McGraw-Hill,6,*"

    def test_publisher_only_bucket_with_space(self):
        pass
        # eg: 99191,7848537371773,PENGUIN RANDOMHOUSE,MIA,4,30_day,2017-05-21 10:01:19.571428 => "Penguin Randomhouse,*,30_day"

    def test_duration_only_bucket(self):
        pass
        # eg: 98819,9793386372887,PENGUIN RANDOMHOUSE,DTW,3,90_day,2017-07-14 14:06:01.562089 => "*,*,110_day"

    def test_price_only_bucket(self):
        pass
        # made up eg: 99999,9999999999999,SCIPUB,MIA,3,110_day,2017-05-23 09:16:43.560846=> *,10,*"

    def test_catch_all_bucket(self):
        pass
        # eg: 98765,0862728122370,OPENSTAX,CLT,5,150_day,2017-05-31 14:21:29.560404 => "*,*,*"

    def test_edge_case_repeated_bucket(self):
        pass
        # eg: SciPub,*,*, only first bucket has purchases, second bucket has no purchases


if __name__ == "__main__":
    # don't think I should test the big files - too hairy
    # buckets_file_name = "purchase_buckets.csv"
    # purchases_file_name = "purchase_data.csv"
    # results_filename = "results.json"

    buckets_file_name = "min_buckets.csv"
    purchases_file_name = "min_purchases.csv"
    results_filename = "min_results.json"

    bucket_collection = BucketCollection(buckets_file_name, purchases_file_name)
    bucket_collection.to_file(results_filename)

    results_filepath = os.path.join(os.path.dirname(__file__), results_filename)
    results_file =  open(results_filepath, 'r')
    results_file_content = results_file.read()
    results_json = json.loads(results_file_content)
    unittest.main()
    results_file.close()
