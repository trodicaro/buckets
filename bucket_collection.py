# read buckets files
  # make keys as concat of capitalized name, price, capitalized duration
  # eg: MCGRAW-HILL540_DAY, MCGRAW-HILL3*, MCGRAW-HILL**,*220DAY
  # later note: I decided to keep the comma in the key since that was the desired output bucket name
# for each purchase data line
  # extract the relevant chars from the string with a regex:
    # eg:7639,9781541920172,Pearson,ORD,2,1_day,2015-06-30 12:25:00
    # capture text between second and third comma, ignore before 4th comma,
  # check the hash  for key like so:
    # name, price, duration
    # name, *, duration
    # name, price, *
    # name, *, *
    # *, *, *

import csv
import json
from collections import OrderedDict
import inspect


class Bucket:
    def __init__(self, original_key = "", purchases = []):
        self.original_key = original_key
        self.key = original_key.upper()
        self.purchases = purchases

class BucketCollection:
    def __init__(self, buckets_file_name):
        self.buckets = OrderedDict()

        with open(buckets_file_name) as buckets_file:
            readCSV = csv.reader(buckets_file)
            for row in readCSV:
                original_key = ",".join([row[0],row[1],row[2]])
                bucket = Bucket(original_key)
                self.buckets[original_key.upper()] = bucket

        if "*,*,*" not in self.buckets.keys():
            self.buckets["*,*,*"] = Bucket("*,*,*")
            self.buckets.move_to_end("*,*,*", last = False)


    def populate_buckets(self, purchases_file_name):
        print(self.buckets.keys())
        with open(purchases_file_name) as purchases_file:
            readCSV = csv.reader(purchases_file)

            for row in readCSV:
                order_id = row[0]
                publisher = row[2]
                price = row[4]
                duration = row[5]
                key = ",".join([publisher, price, duration])

                complete_key = ",".join([publisher, price, duration]).upper()
                publisher_duration_key = ",".join([publisher, "*", duration]).upper()
                publisher_price_key = ",".join([publisher, price, "*"]).upper()
                publisher_only = ",".join([publisher, "*", "*"]).upper()
                price_duration_key = ",".join(["*", price, duration]).upper()
                duration_only_key = ",".join(["*", "*", duration]).upper()
                price_only_key = ",".join(["*", price, "*"]).upper()
                catch_all_key = ",".join(["*","*","*"]).upper()

                possible_keys = [complete_key, publisher_duration_key, publisher_price_key, publisher_only,
                            price_duration_key, duration_only_key, price_only_key, catch_all_key]

                print(possible_keys)

                for possible_key in possible_keys:
                    print(possible_key, possible_key in self.buckets.keys())
                    if possible_key in self.buckets.keys():
                        stringified_record = ",".join(map(str, row))
                        print(self.buckets[possible_key].purchases)
                        self.buckets[possible_key].purchases.append(stringified_record)
                        break

    def to_json(self):
        results = []

        for key, bucket in self.buckets.items():
              current_group = {}
              current_group["bucket"] =  bucket.original_key
              current_group["purchases"] =  bucket.purchases
              results.append(current_group)

        return results

    def to_file(self, result_file_name):
      results_file = open(result_file_name, 'w')
      results_file.write(json.dumps(self.to_json(), indent = 4, sort_keys = True))
      results_file.close()


# def main(buckets_file_name, purchases_file_name):
#     buckets = create_keys(buckets_file_name, purchases_file_name)
#     populated_buckets = populate_buckets(buckets)
#     results = generate_result(buckets)
#     print_to_json(results)
def run(buckets_file_name, purchases_file_name):
    bucket_collection = BucketCollection(buckets_file_name)
    bucket_collection.populate_buckets(purchases_file_name)
    bucket_collection.to_file("min_results.json")

