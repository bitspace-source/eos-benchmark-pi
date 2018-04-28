# eos-benchmark-pi
this repo contains a primitive compute benchmark for the eos blockhain that repeatedly calculates pi

## requirements

```cleos``` and ```eosiocpp``` and a node running localy

## Initialize

### run per session

```cleos wallet open``` 

```cleos wallet unlock```

make sure to have keys for the user you use!

### run per chain

```sh compile&upload.sh <user>```

## Use

### run 

```python3 benchmark.py [<account> [<iterations> [<difficulty> [<precision> ]]]]```
