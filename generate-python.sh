export SRC_DIR=~/Documents/personalizedrecommender-python/proto/
export DST_DIR=~/Documents/personalizedrecommender-python/personalizedrecommender/
export FILE_NAME=hotel.proto

protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/$FILE_NAME