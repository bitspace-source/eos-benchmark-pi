if[$1 != ""];then
    user=$1
else
    user="bitspace"
fi

cd eos-benchmark
eosiocpp -o eos-benchmark.wast -g eos-benchmark.abi eos-benchmark.cpp

cleos set contract $user ../eos-benchmark -p $user
