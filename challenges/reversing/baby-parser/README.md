# Baby-Parser [1-5]

Baby-Parser is a series of 5 static challenges that involves an understanding of skills and techniques required to parse unknown binary formats.

# Learning Objective

After completing the challenges, participants will have a good understanding on how to approach proprietary binary formats, as well as the common tricks that developers use to discourage extracting and modifying files packed in a container format.

# Description (public)

## Baby-Parser 1
```
A friend has told me of this new webserver software published by WhiteHacks Inc. that does not need installation nor configuration to work. Instead, it utilizes a new file format with a .wh file extension.

P.S. You do not need to reverse engineer the executable to solve the challenge. All `O`s in the flag are zero `0`.
```

## Baby-Parser 2
```
Following concerns that the .wh files does not offer a filesize advantage to the likes of apache and nginx webservers, version 2 is supposed to consume less disk space while serving the same files. WhiteHacks Inc. proudly stands by its space saving algorithms.

P.S. You do not need to reverse engineer the executable to solve the challenge. All `O`s in the flag are zero `0`.
```

## Baby-Parser 3
```
It has come to the developers of the webserver that v1 and v2 of the .wh format is too easy to reverse engineer. Following that revelation, WhiteHacks Inc. have announced version 3 of the format, which will solve the issue of easy decoding of files on-disk. 

P.S. All `O`s in the flag are zero `0`.
```

## Baby-Parser 4
```
REDACTED
```

## Baby-Parser 5
```
REDACTED
```

# Setup Guide

1. Run `make` to build the bin files and the executables available in the `./build` directory.
2. Use the `docker-compose.yml` in the parent directory to deploy the service at port 11002

# Flags

## Baby-Parser 1

`WH2020{whO_ne3ds_bin@ry_when_1_cAn_f!l3_CaRv3}`

## Baby-Parser 2

`WH2020{ZliB_d035nt_m@kE_TH1ng5_b3tt3r}`

## Baby-Parser 3

`WH2020{whY_R3_wh3N_y0u_C@N_ju5t_DuMp}`

## Baby-Parser 4

`REDACTED`

## Baby-Parser 5

`REDACTED`

# Solution

## Using a declarative binary format parsing language such as kaitai-struct to read the bin files

The .ksy specification files are available in `./solution/*.ksy`.

* If `kaitai-struct-visualizer` is installed, run `ksv ./build/whitehacksvX.wh ./solution/whX.ksy`
* Else you can also generate a python parser class by running `ksc -t python ./solution/whX.ksy`
    * Parse a local file and get structure in memory with `data = WhitehacksvX.from_file("path/to/local/file.wh")`
    * Access the magic header with `print(data.magic)`

## Using other tools to read the bin files

* Baby-Parser 1
    * Running a file carving tool such as `foremost` will do the trick.
* Baby-Parser 2
    * Extract the zlib files, and decompress them using the DEFLATE algorithm.
* Baby-Parser 3
    * Perform a memory dump of the running webserver process, then extract the zlib files, and decompress them.
* Baby-Parser 4
    * REDACTED
* Baby-Parser 5
    * REDACTED
