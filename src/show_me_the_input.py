import sys
import base64

lines = ["output\n", sys.version, "\n\n"]

for i in range(1, len(sys.argv)):
    lines.append("======== START OF sys.argv%s===========\n" % i)
    with open(sys.argv[i]) as fobj:
        for line in fobj:
            lines.append(line.decode('utf-8'))
    lines.append("================================== END OF sys.argv%s==========================\n" % i)        
lines.append("===================== ALL DONE =======================")
s = base64.encodestring("".join(lines))
raise Exception(s)