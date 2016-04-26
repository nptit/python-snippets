
with open("read_records_lines.dat") as fh:
    lines=fh.readlines()

print lines

i = 0
d=dict()
for line in lines:
    line=line.strip()
    curr_record = i
    if line == "NUMS":
       d[curr_record] = []
    elif line == "END":
       i += 1
    elif str.isdigit(line):
       d[curr_record].append(line)

print d
