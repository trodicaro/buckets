# read buckets files
  # make a hash with keys a combo of capitalized name, price, capitalized duration
  # eg: MCGRAW-HILL540_DAY, MCGRAW-HILL3*, MCGRAW-HILL**,*220DAY
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

# purchases_file = open('purchase_data.csv')
# for line in purchases_file:
#     records = line.split(",")
#     most_specific_key =  "".join([records[2],records[4],records[5]]).upper()
#     duration_specific_key = "".join([records[2],"*",records[5]]).upper()
#     price_specific_key = "".join([records[2],records[4],"*"]).upper()
#     publisher_specific_key = "".join([records[2],"*","*"]).upper()

#     print most_specific_key
#     print duration_specific_key
#     print price_specific_key
#     print publisher_specific_key

    # matches = re.search("^([^,]*),\d{13},([^,]*),[^,]*,(.*,.*)(?=,\d{4})", line)
    # print matches.group(0)
    # print matches.group(1)
    # print matches.group(2)
    # print matches.group(3)
# purchases_file.close

buckets = OrderedDict()
results = []

with open('purchase_buckets.csv') as buckets_file:
    readCSV = csv.reader(buckets_file)
    for row in readCSV:
        bucket = ",".join([row[0],row[1],row[2]])
        buckets[bucket] = []


for bucket, content in buckets.items():
    print bucket
    current_group = {}
    current_group["bucket"] = bucket
    current_group["purchases"] = content
    results.append(current_group)

print results

with open('purchase_data.csv') as purchases_file:
    readCSV = csv.reader(purchases_file)
    for row in readCSV:
        order_id = row[0]
        publisher = row[2]
        price = row[4]
        duration = row[5]
        key = ",".join([order_id, publisher, price, duration])
        # if  results[key.lower()]:
        #     print "Exists"
        #     print key.lower()


json_format = json.dumps(results)

results_file = open('results.json', 'w')
results_file.write(json.dumps(results, indent = 4, sort_keys = True))
results_file.close()


