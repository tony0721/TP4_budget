import os
import sys
badHash = sys.argv[1]
goodHash = sys.argv[2]
os.system(f'git bisect start {badHash} {goodHash}')
os.system('git bisect run python manage.py test')
