import sys
import base64
import zlib
import json

if len(sys.argv) > 1: # we have an input file!
    inputfile = open(sys.argv[1])
else:
    inputfile = sys.stdin

with open(sys.argv[1], 'rb') as fobj:
    encoded = fobj.read()

decjson = base64.b64decode(encoded)
data = json.loads(decjson)
version = data['version']

print("System was running: %s" % version)

for file_entry in data['files']:
    index = file_entry['index']
    try:
        contents = file_entry['contents']
        writable_contents = zlib.decompress(base64.b64decode(contents))
        with open(('argv%s.txt' % index), 'wb') as fobj:
            fobj.write(writable_contents)
    except Exception as e:
        print "Error processing argv[%s]: %s" % (index, e)
