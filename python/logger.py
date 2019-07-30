import sys
import re
import json
# import requests

# ROUTING_KEY = "" # ENTER EVENTS V2 API INTEGRATION KEY HERE 

# def trigger_incident():
#     # Triggers a PagerDuty incident without a previously generated incident key
#     # Uses Events V2 API - documentation: https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2

#     header = {
#         "Content-Type": "application/json"
#     }

#     payload = { # Payload is built with the least amount of fields required to trigger an incident
#         "routing_key": ROUTING_KEY, 
#         "event_action": "trigger",
#         "payload": {
#             "summary": "Example alert on host1.example.com",
#             "source": "monitoringtool:cloudvendor:central-region-dc-01:852559987:cluster/api-stats-prod-003",
#             "severity": "critical",
#             "custom details": {
#               "username":,
#               "jobname":
#             }
#         }
#     }

#     response = requests.post('https://events.pagerduty.com/v2/enqueue', 
#                             data=json.dumps(payload),
#                             headers=header)
	
#     if response.json()["status"] == "success":
#         print('Incident created with with dedup key (also known as incident / alert key) of ' + '"' + response.json()['dedup_key'] + '"') 
#     else:
#         print(response.text) # print error message if not successful


def check_job_start(line):
    matcher = re.match(
        r"(?P<time>.*M).*job\/(?P<jobname>[\w-]+)\/ #[\d]+.*Started by user (?P<username>[\w-]+)", line)
    if (matcher != None):
        time = matcher.group("time")
        job = matcher.group("jobname")
        user = matcher.group("username")
        # trigger_incident()
        print("Hi " + user + ", did start the Job " + job + " at time " + time)


def check_config_submit(line):
    matcher = re.match(
        r"(?P<time>.*M).*job\/(?P<jobname>[\w_]+)\/configSubmit by (?!.*timer)(?P<username>[\w]+)", line)
    if (matcher != None):
        time = matcher.group("time")
        job = matcher.group("jobname")
        user = matcher.group("username")
        # trigger_incident()
        print("Hi " + user + ", did submit config for Job " + job + " at time " + time)


with open("./timestamp.txt", "r") as timestamp_file:
    last_timestamp = timestamp_file.read()
print(last_timestamp)
read_flag = False
latest_timestamp = ""
with open("./logfile.log", "r") as logfile:
    for line in logfile:
        line = str(line.split("\n")[0])
        print(line)
        if re.match(last_timestamp, line):
            print("date matched")
            read_flag = True
            continue
        if read_flag:
            print(line)
            check_job_start(line)
            check_config_submit(line)

    latest_timestamp = re.match("(?P<time>.*M).*", line)
    with open("./timestamp.txt", "w+") as timestamp_file:
        timestamp_file.write(str(latest_timestamp.group("time")))