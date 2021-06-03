import sys
import base64 as b
print(str(b.b64encode(str.encode(sys.argv[1])))[2:-1])