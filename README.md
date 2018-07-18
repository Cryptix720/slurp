# SLURP
This tool allows subdomains from a HTTP(S) website in a few seconds.  
How it works? SLURP does not use neither dictionary attack nor brute-force, it just abuses of Certificate Transparency logs.  
For more information about CT logs, check www.certificate-transparency.org and [crt.sh](https://crt.sh/).



### Pre-requisites
Make sure you have installed the following tools:
```
Python 3.0 or later.
pip3 (sudo apt-get install python3-pip).
```

### Installing
```bash
$ git clone https://github.com/Cryptix720/slurp.git
$ cd slurp
$ pip3 install -r requirements.txt
```

### Running
```bash
$ python3 slurp.py --help

```


## Usage
Parameters and examples of use.

### Parameters
```
-d --domain [target_domain] (required)
-o --output [output_file] (optional)
```

### Examples
```bash
$ python3 slurp.py -d carforsales.com
```
```bash
$ python3 slurp.py -d twitter.com -o /home/desktop/subdomains_tw.txt
```


### Good to know!

$ Works great with Python 2.7.x.

$ If python3 doesn't prompt, remove number (3)

```




