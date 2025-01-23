import os

for f in os.listdir('names'):
    print(f.split('.txt')[0])