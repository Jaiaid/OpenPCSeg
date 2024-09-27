#!/bin/bash

ROOT_DIR=`pwd`
DATAROOT_DIR=2
PCD2BIN_CONVERTER_EXEC=$ROOT_DIR/pcd2bin
LABEL_CONVERSION_SCRIPT=$ROOT_DIR/misc_scripts/semlabel_conversion.py

pushd $DATAROOT_DIR

# convert the label txt to semantickitti label format files
mkdir labels
python3 $LABEL_CONVERSION_SCRIPT --dir labels_txt -o labels > stat.txt
mv labels $ROOT_DIR/$DATAROOT_DIR/model_feed_data/
exit

# convert the original data to bin
mkdir velodyne
$PCD2BIN_CONVERTER_EXEC pcds velodyne
mv velodyne $ROOT_DIR/$DATAROOT_DIR/model_feed_data/

# go insider each method's gained data
for METHOD in kdtree-only draco octree;
do
    pushd $METHOD
    mkdir $ROOT_DIR/$DATAROOT_DIR/model_feed_data/$METHOD
    # travarse through different parameter gained compression
    for dir in `ls .`;
    do
        # convert decompressed pcd to velodyne from each parameter gained compression
        pushd $dir
        mkdir velodyne
        $PCD2BIN_CONVERTER_EXEC decompressed velodyne
        mkdir $ROOT_DIR/$DATAROOT_DIR/model_feed_data/$METHOD/$dir
        mv velodyne $ROOT_DIR/$DATAROOT_DIR/model_feed_data/$METHOD/$dir
        popd
    done
    popd
done

# our directory structure is different
pushd our
mkdir $ROOT_DIR/$DATAROOT_DIR/model_feed_data/our
for POINT_DUPLICACY_TYPE in `ls .`;
do
    pushd $POINT_DUPLICACY_TYPE
    mkdir $ROOT_DIR/$DATAROOT_DIR/model_feed_data/our/$POINT_DUPLICACY_TYPE
    # travarse through different parameter gained compression
    for dir in `ls .`;
    do
        mkdir $ROOT_DIR/$DATAROOT_DIR/model_feed_data/our/$POINT_DUPLICACY_TYPE/$dir
        # convert decompressed pcd to velodyne from each parameter gained compression
        pushd $dir
        mkdir velodyne
        $PCD2BIN_CONVERTER_EXEC decompressed velodyne
        mv velodyne $ROOT_DIR/$DATAROOT_DIR/model_feed_data/our/$POINT_DUPLICACY_TYPE/$dir/
        popd
    done
    popd
done
popd

popd
