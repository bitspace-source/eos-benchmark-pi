cd eos-benchmark
eosiocpp -o eos-benchmark.wast eos-benchmark.cpp
eosiocpp -g eos-benchmark.abi eos-benchmark.cpp

cleos set contract $1 ../eos-benchmark -p $1
