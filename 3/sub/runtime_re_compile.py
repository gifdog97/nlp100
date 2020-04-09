import time
import re

start = time.time()

for i in range(1000000):
    re.match(r'[a-z]*', 'hoge')

print("no-compile", time.time() - start)

start = time.time()

pat = re.compile(r'[a-z]*')

for i in range(1000000):
    pat.match('hoge')

print("compile", time.time() - start)

