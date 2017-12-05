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

buckets = OrderedDict()

# create a buckets dictionary; keep original key as first item in values
with open('purchase_buckets.csv') as buckets_file:
    readCSV = csv.reader(buckets_file)
    for row in readCSV:
        original_key = ",".join([row[0],row[1],row[2]])
        upcased_key = original_key.upper()
        buckets[upcased_key] = [original_key]

# iterate through purchases, build key and find match in buckets
with open('purchase_data.csv') as purchases_file:
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

        key_list = [complete_key, publisher_duration_key, publisher_price_key, publisher_only,
                    price_duration_key, duration_only_key, price_only_key, catch_all_key]

        for key in key_list:
            if key in buckets:
                stringified_record = ",".join(map(str, row))
                buckets[key].append(stringified_record)
                break

results = []

for bucket, content in buckets.items():
    current_group = {}
    current_group["bucket"] = content[0]
    current_group["purchases"] = content[1:]
    results.append(current_group)

results_file = open('results.json', 'w')
results_file.write(json.dumps(results, indent = 4, sort_keys = True))
results_file.close()


