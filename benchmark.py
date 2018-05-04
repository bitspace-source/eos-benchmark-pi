import os
import time
import sys

# cpu limit on linode - eos-test1: iterations":741,"difficulty":1000,"precision":15
user       =     sys.argv[1]  if len(sys.argv) > 1 else "bitspace"
iterations = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
difficulty = int(sys.argv[3]) if len(sys.argv) > 3 else 100

start = time.time()
for i in range(iterations):
	os.system("cleos push action %s pi '[%i, %i]' -p %s" % (user, i, difficulty, user))
#
end = time.time()
print("iterations: %i, time %d" % (iterations, end-start))
