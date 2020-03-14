#!/usr/bin/env python

from __future__ import print_function
import sys
import datetime


def write_stdout(message):
    sys.stdout.write(message)
    sys.stdout.flush()

def get_timestamp_to_milliseconds():
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S.%f')
    return timestamp[:-3]

def main():
    while True:
        # transition from ACKNOWLEDGED to READY
        write_stdout('READY\n')

        # read header line from stdin
        line = sys.stdin.readline()
        headers = dict([x.split(':') for x in line.split()])

        # read the event payload
        data = sys.stdin.read(int(headers['len']))

        # transition from READY to ACKNOWLEDGED
        write_stdout('RESULT %s\n%s' % (len(data.encode('utf-8')), data))

def event_handler(event, response):
    """
    Prefixes each line of the response message with a timestamp and then
    prints the message to stdout.
    """
    content, data = response.split(b'\n', 1)
    headers = dict([x.split(b':') for x in content.split()])
    lines = data.split(b'\n')
    timestamp = get_timestamp_to_milliseconds()
    prefix = b'%s %s %s | ' % (timestamp, headers[b'processname'], headers[b'channel'])
    print(b'\n'.join([prefix + line for line in lines if line]).decode('utf-8'))


if __name__ == '__main__':
    main()
