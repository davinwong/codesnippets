# Resources:
# Graphite's Example - https://github.com/graphite-project/graphite-web/blob/master/examples/example-client.py

# Notes:
# example line: """232.46.23.125 - - [27/Jan/2013:06:40:30 +0000] "PUT /resource HTTP/1.1" 201 8804 114055 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22"""
# example line: """72.188.198.89 - - [28/Jan/2013:11:57:50 +0000] "GET /index.php HTTP/1.1" 200 207 496054 "http://www.google.com/?q=request" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22"""
#
# Currently this script creates a large array and sends it all to carbon. Depending on size, it may be better
# to break this array and send data to carbon in batches.

# Next Steps:
# Improve speed of reading initial log data
# Finish functionality to skip already read lines

import sys
import time
import datetime
import re
from socket import socket


### Connection Setup ###

# carbon credentials
CARBON_SERVER = 'ec2-50-19-203-254.compute-1.amazonaws.com'
CARBON_PORT = 2003
DELAY = 15  # Delay in seconds before sending new log data to carbon/graph

# connect to carbon
sock = socket()
try:
    sock.connect((CARBON_SERVER, CARBON_PORT))
except:
    print "Couldn't connect to %(server)s on port %(port)d, is carbon-agent.py running?" % {'server': CARBON_SERVER, 'port': CARBON_PORT}
    sys.exit(1)

# log file containing apache-like data to be parsed
http_log_path = '/var/log/challenge/example.log'

month_conversion = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}

### Functions ###


# parses 1 line of log, returns http status code category and timestamp
def parse_log_line(line):
    line_data = {}
    # line = http_log.readline()
    print "line"
    print line

    # if empty string returned, reached end of log file.
    if line == '':
        return ''

    if line == None:
        return ''

    # parse line
    regex = re.compile(r""" \d*\.\d*\.\d*\.\d* # ip address
                            \s\-\s\-\s # spaces, dashes
                            \[(?P<day>.*?) \/ (?P<month>.*?) \/ (?P<year>.*?) # day, month, year
                            :(?P<hour>.*?):(?P<minute>.*?):(?P<second>.*?) #  hour, minute, second
                            \s\+\d*\]\s # +0000
                            ".*?" # quoted text
                            \s(?P<status>.*?)\s # http status code
                            (?P<statustwo>.*?)\s # possible second status code
                            .* # remaining
                        """, re.VERBOSE)

    match = re.match(regex, line)

    # save datetime parameters, status code
    day = int(match.group("day"))
    month = month_conversion[match.group("month")]
    year = int(match.group("year"))
    hour = int(match.group("hour"))
    minute = int(match.group("minute"))
    second = int(match.group("second"))
    status = int(match.group("status"))
    statustwo = int(match.group("statustwo"))

    timestamp_datetime = datetime.datetime(year, month, day, hour, minute, second)  # put parameters in datetime
    timestamp = time.mktime(timestamp_datetime.timetuple())  # convert datetime object to time object
    status_category = (status / 100) * 100  # convert status code into 100, 200, 300, etc to show category

    # see if second number is a status code
    if statustwo < 600 and statustwo >= 100:
        status_category2 = (statustwo / 100) * 100  # convert status code into 100, 200, 300, etc to show category
    else:
        status_category2 = None

    line_data['timestamp'] = timestamp
    line_data['status_category'] = status_category
    line_data['status_category2'] = status_category2

    return line_data


# parses all new log entries
def get_new_data(line_count):

    # data to be sent to carbon in update
    carbon_data = []

    # loop through each log line

    with open(http_log_path, 'r') as http_log:

        # skip already read lines: This implementation is not finished - need to skip lines
        # http_log.seek(line_count['n'], 0)

        # loop through new lines
        for line in http_log:

            # parse line
            line_data = parse_log_line(line)

            # increment count of read lines
            line_count['n'] += 1

            # if empty string returned, reached end of log file.
            if line_data == '':
                break

            status_category = line_data['status_category']
            status_category2 = line_data['status_category2']
            timestamp = line_data['timestamp']

            status_count[str(status_category)] += 1

            if status_category2:
                status_count[str(status_category2)] += 1

            print status_count['100']
            print status_count['200']
            print status_count['300']
            print status_count['400']
            print status_count['500']

            # save result in carbon_data. format: "<select graph> <current count> <time>"
            carbon_data.append("system.http_response_graph_%s %s %d" % (status_category, status_count[str(status_category)], timestamp))

            if status_category2:
                carbon_data.append("system.http_response_graph_%s %s %d" % (status_category2, status_count[str(status_category2)], timestamp))

    return carbon_data


### Variables ###

# remember lines of log read. skip already read lines.
line_count = {}
line_count['n'] = 0

# status category occurrence counts
status_count = {}
status_count['100'] = 0
status_count['200'] = 0
status_count['300'] = 0
status_count['400'] = 0
status_count['500'] = 0

### Action ###

# continuous loop to keep updating graph
while True:

    # update carbon
    carbon_data = get_new_data(line_count)
    message = '\n'.join(carbon_data) + '\n'
    sock.sendall(message)
    print message
    print "LINE COUNT"
    print line_count['n']

    time.sleep(DELAY)
