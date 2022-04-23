name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hc = dict()
hli =[]

for line in handle:
    if line.startswith("From "):
        hr = line.split()[5].split(":")
        hc[hr[0]] = hc.get(hr[0],0) + 1
    else:
        continue

for k, v in hc.items():
    hli.append((k, v))
hli.sort()

for k,v in hli:
  print(k, v)
