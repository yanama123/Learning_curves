#! /usr/bin/python
import sys
from datetime import datetime
d_format = "%Y-%m-%d"

try:
    start = datetime.strptime(sys.argv[1], d_format)
    end = datetime.strptime(sys.argv[2], d_format)
except (TypeError, IndexError):
    sys.stderr.write("Example: grep-date-range.py 2011-03-25 2011-04-02 \n")

for line in sys.stdin:
    try:
        date = datetime.strptime(line.split()[0], d_format)
        # suit the <=, <, comparisons bellow to your needs:
        if start <= date < end:
            sys.stdout.write(line)
    except (ValueError, IndexError):
        pass