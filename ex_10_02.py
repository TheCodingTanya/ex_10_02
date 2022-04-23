name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hc = dict()                   # creat empty dictionary
hli =[]                       # creat empty list

for line in handle:
    if line.startswith("From "):         # extract lines startswith "From "
        hr = line.split()[5].split(":")  # pull out hour (5th position) and split string with colon (":")
        hc[hr[0]] = hc.get(hr[0],0) + 1  # add count for each hour
    else:
        continue

for k, v in hc.items():                  # key = k = hour; value = v = count
    hli.append((k, v))                   # use append function to add tuples to list
hli.sort()                               # sort list by key/hour

for k,v in hli:                          # for loop of tuples in the list
  print(k, v)                            # print out counts which sorted by key/hour
