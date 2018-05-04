# eos-benchmark-pi
This repo contains a primitive compute benchmark for the eos blockhain that repeatedly calculates pi.

## Requirements

```cleos```, ```eosiocpp``` and a user on the chain.

## Initialize

### run per session

```cleos wallet open``` 

```cleos wallet unlock```

Make sure to have keys for the user you use in your wallet!

### run per chain

```sh compile&upload.sh <user>```

## Use

### run 

```python3 benchmark.py [<account> [<iterations> [<difficulty> [<precision> ]]]]```
