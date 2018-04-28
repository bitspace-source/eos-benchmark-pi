# eos-benchmark-pi
a compute benchmark of pi on eos-node

## requirements

```cleos``` and ```eosiocpp``` compiled with eos and a node running localy

## Initialize

#### run per session

```cleos wallet open``` 

```cleos wallet unlock```

make sure to have keys for the user you use!

### run per chain

```sh compile&upload.sh <user>```

## Use

### run 

```python3 benchmark.py [<account> [<iterations> [<difficulty> [<precision> ]]]]```
