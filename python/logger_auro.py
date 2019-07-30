import sys
import re


def check_job_start(line):
    matcher = re.match(
        r"(?P<time>.*M).*job\/(?P<jobname>[\w_]+)\/ #[\d]+.* Started by user (?P<username>[\w]+)", line)
    if (matcher != None):
        time = matcher.group("time")
        job = matcher.group("jobname")
        user = matcher.group("username")
        print("Hi " + user + ", Did you start the Job " +
              job + " at time " + time + "?")


def check_config_submit(line):
    matcher = re.match(
        r"(?P<time>.*M).*job\/(?P<jobname>[\w_]+)\/configSubmit by (?!.*timer)(?P<username>[\w]+)", line)
    if (matcher != None):
        time = matcher.group("time")
        job = matcher.group("jobname")
        user = matcher.group("username")
        print("Hi " + user + ", Did you submit config for Job " +
              job + " at time " + time + "?")


timestamp_file = open("./timestamp.txt", "r")
last_timestamp = timestamp_file.read()
logfile = open("./logfile.log", "r")
read_flag = False
last_line = ""
latest_timestamp = ""
for line in logfile:
    last_line = line
    if read_flag:
        check_job_start(line)
        check_config_submit(line)

    if re.match(last_timestamp, line):
        read_flag = True

if not read_flag:
    logfile = open("./logfile.log", "r")
    for line in logfile:
        check_job_start(line)
        check_config_submit(line)

latest_timestamp = re.match("(?P<time>.*M).*job.*", last_line).group("time")