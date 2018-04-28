import os
import time
import sys

# cpu limit on linode - eos-test1: iterations":741,"difficulty":1000,"precision":15
iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
difficulty = int(sys.argv[2]) if len(sys.argv) > 2 else 100
precition  = int(sys.argv[3]) if len(sys.argv) > 3 else 15
user       =     sys.argv[4]  if len(sys.argv) > 4 else "bitspace"


start = time.time()
for i in range(iterations):
	os.system("cleos push action %s pi '[%i, %i, %i]' -p %s" % (user, i, difficulty, precition, user))
#
end = time.time()
print("iterations: %i, time %d" % (iterations, end-start))
