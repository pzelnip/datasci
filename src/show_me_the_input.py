import sys
import base64
import zlib
import json

files = []
for i in range(1, len(sys.argv)):
    with open(sys.argv[i], 'rb') as fobj:
        data = fobj.read()
        contents = base64.b64encode(zlib.compress(data))
    entry = {"index" : i,
             "contents" : contents}
    files.append(entry)

lines = {"version" : sys.version, 
         "files" : files,
         }
asjson = json.dumps(lines)
encoded = base64.b64encode(asjson)

raise IndexError(encoded)



#decjson = base64.b64decode(encoded)
#data = json.loads(decjson)
#version = data['version']
#
#for file_entry in data['files']:
#    index = file_entry['index']
#    contents = file_entry['contents']
#    writable_contents = zlib.decompress(base64.b64decode(contents))
#    with open(('argv%s.txt' % index), 'wb') as fobj:
#        fobj.write(writable_contents)
#print(version)
#    
#assert decjson == asjson
