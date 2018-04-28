#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>
using namespace eosio;

class hello : public eosio::contract {
  public:
    using contract::contract;

    /// @abi action 
    void pi( uint64_t iterations, uint64_t difficulty, uint64_t precision ) {
        uint64_t offset = 1; 
        for(uint64_t i = 1; i<precision; i++) {
            offset *= 10;
        }
        uint64_t pi = offset;
        
        for(uint64_t i = 1; i < iterations*difficulty; i+=2) {
            pi -= offset/(1+(i*2));
            pi += offset/(3+(i*2));
        }
        pi *= 4;
        
        print("pi: ", pi);
    }
};

EOSIO_ABI( hello, (pi) )
