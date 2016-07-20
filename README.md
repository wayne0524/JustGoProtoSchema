Simple usage
============
###Generating source files without installing protobuf
The output files will be in java/, python/, swift/
```
sh generate-all.sh
```
If the swift compiler is not setup, try
```
brew install protobuf-swift
```

Complete setup
==============

###Generating Java protobuf source file:
**Compile command**
```
export SRC_DIR=./justgo
export DST_DIR=./java/
export FILE_NAME=${proto_file_name}

protoc -I=$SRC_DIR --java_out=$DST_DIR $SRC_DIR/$FILE_NAME
```
###Generating Python protobuf source file:
**Compile command**
```
export SRC_DIR=./justgo
export DST_DIR=./python/
export FILE_NAME=${proto_file_name}

protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/$FILE_NAME
```
###Generating Swift protobuf source file:
**Install the Swift compiler**
To compile the code into Swift, follow the instructions to setup swift compiler:
  https://github.com/alexeyxo/protobuf-swift
**Compile command**
```
export SRC_DIR=./justgo
export DST_DIR=./swift/
export FILE_NAME=${proto_file_name}

protoc -I=$SRC_DIR --swift_out=$DST_DIR $SRC_DIR/$FILE_NAME
```


For further information:
[Protocol Buffers](https://developers.google.com/protocol-buffers/) - Google's data interchange format
Copyright 2008 Google Inc.

This package contains a precompiled Win32 binary version of the protocol buffer
compiler (protoc).  This binary is intended for Windows users who want to
use Protocol Buffers in Java or Python but do not want to compile protoc
themselves.  To install, simply place this binary somewhere in your PATH.

This binary was built using MinGW, but the output is the same regardless of
the C++ compiler used.

You will still need to download the source code package in order to obtain the
Java or Python runtime libraries.  Get it from:
  https://github.com/google/protobuf/releases/
