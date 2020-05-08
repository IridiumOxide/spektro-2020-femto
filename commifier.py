#!/usr/bin/python
import sys

if len(sys.argv) < 2:
    print("wtf")
    exit(1)

for filename in sys.argv[1:]:
    extensionless_filename = filename.split(".")[0]

    out_filename = "commified_" + extensionless_filename + ".csv"

    print("From " + filename + " to " + out_filename)

    with open(filename, 'r') as input_file:
        with open(out_filename, 'w') as output_file:
            data = input_file.read()
            output_file.write(data.replace(" ", ","))
