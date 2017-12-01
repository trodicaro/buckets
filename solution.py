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

# create a buckets dictionary
with open('purchase_buckets.csv') as buckets_file:
    readCSV = csv.reader(buckets_file)
    for row in readCSV:
        original_key = ",".join([row[0],row[1],row[2]])
        upcased_key = original_key.upper()
        buckets[upcased_key] = [original_key]

print buckets

# iterate through purchases, build key and find match in buckets
with open('purchase_data.csv') as purchases_file:
    readCSV = csv.reader(purchases_file)

    for row in readCSV:
        order_id = row[0]
        publisher = row[2]
        price = row[4]
        duration = row[5]
        key = ",".join([publisher, price, duration])

        most_specific_key =  ",".join([publisher, price, duration]).lower()
        duration_specific_key = ",".join([publisher, "*", duration]).lower()
        price_specific_key = ",".join([publisher, price, "*"]).lower()
        publisher_specific_key = ",".join([publisher, "*", "*"]).lower()
        most_generic_key = ",".join(["*","*","*"]).lower()

        key_list = [most_specific_key, duration_specific_key, price_specific_key,
                    publisher_specific_key, most_generic_key]

        # for index, key in enumerate(key_list):
        #     if key in buckets:
        #         print "Y %d %s" % (index, key)
        #         # print buckets.get(key)
        #     else:
        #         print "N %d %s" % (index, key)
        #         # print buckets.get(key)
        #     # break;
        #     # if key in buckets.keys()
        #       # buckets[key].append(row)

results = []

for bucket, content in buckets.items():
    current_group = {}
    current_group["bucket"] = bucket
    current_group["purchases"] = content
    results.append(current_group)

results_file = open('results.json', 'w')
results_file.write(json.dumps(results, indent = 4, sort_keys = True))
results_file.close()


