# This script works for python 2

import sys
import re
import json
import requests
import argparse
from datetime import datetime

ROUTING_KEY = "126480f0d76449b484c878390548435e" # ENTER EVENTS V2 API INTEGRATION KEY HERE 

def trigger_incident(time, job, action, user):
    # Uses Events V2 API - documentation: https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2

    header = {
        "Content-Type": "application/json"
    }

    payload = {
        "routing_key": ROUTING_KEY, 
        "event_action": "trigger",
        "payload": {
            "summary": "SOME-SUMMARY",
            "source": "SOME-SOURCE",
            "severity": "critical",
            "custom_details": {
              "time": time,
              "jobname": job,
              "action": action,
              "username": user
            }
        }
    }
    print payload
    # response = requests.post('https://events.pagerduty.com/v2/enqueue', 
    #                         data=json.dumps(payload),
    #                         headers=header)
	
    # if response.json()["status"] == "success":
    #     print('Incident created with with dedup key (also known as incident / alert key) of ' + '"' + response.json()['dedup_key'] + '"') 
    # else:
    #     print(response.text) # print error message if not successful

def extract_fields(matcher):
        if (matcher != None):
            (time, job, action, user) = matcher.groups()
            trigger_incident(time, job, action, user)

def check_job_start(line):
    matcher = re.match(
        r"(?P<time>.*M).*job\/(?P<jobname>[\w-]+)\/ #[\d]+.*(?P<action>Started) by user (?P<username>[\w-]+)", line)
    extract_fields(matcher)

def check_config_submit(line):
    matcher = re.match(
        r"(?P<time>.*M).*job\/(?P<jobname>[\w_]+)\/(?P<action>configSubmit) by (?!.*timer)(?P<username>[\w]+)", line)
    extract_fields(matcher)

def parse_args():
    parser = argparse.ArgumentParser(description="Send alerts from Jenkins to PagerDuty")
    parser.add_argument("logfile", type=str, help="File comntaining audit logs for Jenkins server")
    parser.add_argument("--exec_time", default=datetime.now(), help="Process logs 1 hour before this time. Format : MMM DD, YYYY hh AM|PM. Example: Sep 20, 2019 5 PM")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    exec_time=args.exec_time
    with open(args.logfile,'r') as logfile:
        for line in logfile:
            line = line.rstrip("\n")
            log_time = datetime.strptime(re.match(r"(?P<time>.*(AM|PM))", line).group(), "%b %d, %Y %I:%M:%S %p")
            if exec_time.date() == log_time.date() and exec_time.hour - 1 == log_time.hour:
                check_job_start(line)
                check_config_submit(line)

# def test():

if __name__ == "__main__":
    main()