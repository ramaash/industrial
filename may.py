import csv

with open('april.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('INTERFACE', 'STATUS', 'PROTOCOL', 'DESCRIPTION'))
        writer.writerows(lines)
