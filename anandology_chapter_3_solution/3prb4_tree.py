import os
import sys
starpath=sys.argv[1]
for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '|-------' * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '|-------' * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
