# #!/usr/bin/env python

# # This script is written in Python2

# from __future__ import print_function

# import argparse
# from datetime import datetime
# import json
# import os
# import sys
# import tempfile
# import urllib
# # import urllib2

# def get_serving_servers(servergroup_id, api_server):
#     query_string = urllib.urlencode({
#         'deleted': 0,
#         'servergroup_id': servergroup_id,
#         'service_status': 7, # servicing
#         'fields': "server_name",
#         'server_name__contains' : "ev.abhagat"
#     })
#     url = "https://%s/api/V3/server/?%s" % (api_server, query_string)
#     res = urllib.urlopen(url)
#     return json.loads(res.read())
# print(get_serving_servers(34934, "api.jopsdb.ops.yahoo.co.jp"))

colos=["ssk","kks"]
server_list = ['a.ssk.d', 'a.kks', 'abssk.ssk.d', 'a.ssk.kksde', 'a.kksde', 'a.ssb.d', 'a.ssb']

def is_valid_server(server_name, colo):
    print(colo + " and " + server_name)
    if ".%s." % (colo) in server_name:
        print("valid")
    elif server_name[-4:] == ".%s" % (colo):
        print("valid")
    else:
        print("invalid")

for colo in colos:
    for server_name in server_list:
        is_valid_server(server_name, colo)