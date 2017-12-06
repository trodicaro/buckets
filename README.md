# Buckets
My first take at Python. Given a csv file with "buckets" and another csv file with purchase records, categorize the records into buckets based on some specificity rules.

**Assumptions**

 Assumed English words in UTF-8 in the files, thus didn't use any character decoding (https://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python). Seems like Python3 handles it though.

  For buckets with no publisher "*,10,*" - I assumed to use the specificity for the in either duration or price. Eg: "*,9,130_day".

  If the "\*,\*,\*" bucket does not exist in the purchase buckets, algorithm creates one at the beginning as per the example above.


**Design**

I initially wanted to use a regex to capture the data fields needed from the csv file, but it became too cryptic to read and switched to regular string methods. I also learned that reading from a csv can be done with pandas, but I suspect it's an overkill.

My solution started without using classes and object. Looking for the abstractions as I solved.

**Other Notes**

Must use python 3.6 or newer. I had a working version with OrderedDict (for lower versions of python, but decided to switch to the regular dictionary structure since ordering is supported starting python3.6).

Seems like the buckets in example output are sorted alphabetically and first bucket is the most generic one, but that's not the order of the 4 sample buckets. I have followed the instructions to keep the order per the purchase_buckets.csv file.
