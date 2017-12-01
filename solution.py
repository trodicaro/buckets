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

# fout = open('etl.txt', 'w')
# line1 = "This here's the wattle, \n"
# fout.write(line1)
# fout.close()



purchases_file = open('purchase_data.csv')
for line in purchases_file:
    records = line.split(",")
    most_specific_key =  "".join([records[2],records[4],records[5]]).upper()
    duration_specific_key = "".join([records[2],"*",records[5]]).upper()
    price_specific_key = "".join([records[2],records[4],"*"]).upper()
    publisher_specific_key = "".join([records[2],"*","*"]).upper()

    print most_specific_key
    print duration_specific_key
    print price_specific_key
    print publisher_specific_key

    # matches = re.search("^([^,]*),\d{13},([^,]*),[^,]*,(.*,.*)(?=,\d{4})", line)
    # print matches.group(0)
    # print matches.group(1)
    # print matches.group(2)
    # print matches.group(3)
purchases_file.close

try:
    buckets_file = open('purchase_buckets.csv')
    buckets = {}
    for line in buckets_file:
        key = "".join(line.rstrip().strip(','))
        buckets[key] = []
    buckets_file.close()
    print buckets
except IOError:
    print 'Something went wrong and could not open the buckets file'
