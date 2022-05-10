import base64
import zlib

class BlueprintDecoder:
    def __init__(self, bp_string):
        vers = bp_string[0]
        bp_string = bp_string[1:]
        inflated = base64.b64decode(bp_string)
        deflated = zlib.decompress(inflated).decode('utf-8')
        with open('test.json', 'w') as f:
            f.write(deflated)
        
