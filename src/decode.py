import os
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
    size = file_entry['size']
    try:
        contents = file_entry['contents']
        writable_contents = zlib.decompress(base64.b64decode(contents))
        filename = 'argv%s.txt' % index
        with open(filename, 'wb') as fobj:
            fobj.write(writable_contents)
        print ("Wrote %s, is %d bytes, original was %d bytes" % (filename, os.path.getsize(filename), size))
    except Exception as e:
        print "Error processing argv[%s]: %s" % (index, e)
