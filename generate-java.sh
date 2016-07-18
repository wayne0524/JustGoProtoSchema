export SRC_DIR=./justgo
export DST_DIR=./java/
export FILE_NAME=userinfo.proto

protoc -I=$SRC_DIR --java_out=$DST_DIR $SRC_DIR/$FILE_NAME