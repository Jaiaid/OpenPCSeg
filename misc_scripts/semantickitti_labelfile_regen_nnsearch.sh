#!/bin/bash

ROOT_DIR=`pwd`
DATAROOT_DIR=~/data/
LABEL_CONVERSION_SCRIPT=$ROOT_DIR/misc_scripts/labelfile_regen_nnsearch.py

# activate venv for open3d
source ~/Desktop/autonomous_vehicle_datacompression/sementic_segmentation/venv_2dpass/bin/activate

pushd $DATAROOT_DIR

# go insider each method's gained data
for METHOD in kdtree-only; #draco octree;
do
    pushd $METHOD
    mkdir $DATAROOT_DIR/model_feed_data/$METHOD
    # travarse through different parameter gained compression
    for dir in `ls .`;
    do
        # convert decompressed pcd to velodyne from each parameter gained compression
        pushd $dir
        mkdir labels
        python3 $LABEL_CONVERSION_SCRIPT -opdir $DATAROOT_DIR/pcds -olabtdir $DATAROOT_DIR/labels_txt -updir decompressed/ -o labels
        mv labels $DATAROOT_DIR/model_feed_data/$METHOD/$dir
        popd
    done
    popd
done

# our directory structure is different
pushd our
mkdir $DATAROOT_DIR/model_feed_data/with_dublicate_points
for POINT_DUPLICACY_TYPE in `ls .`;
do
    pushd $POINT_DUPLICACY_TYPE
    mkdir $DATAROOT_DIR/model_feed_data/with_dublicate_points/$POINT_DUPLICACY_TYPE
    # travarse through different parameter gained compression
    for dir in `ls .`;
    do
        # convert decompressed pcd to velodyne from each parameter gained compression
        pushd $dir
        mkdir labels
        python3 $LABEL_CONVERSION_SCRIPT -opdir $DATAROOT_DIR/pcds -olabtdir $DATAROOT_DIR/labels_txt -updir decompressed/ -o labels
        mv labels $DATAROOT_DIR/model_feed_data/with_dublicate_points/$POINT_DUPLICACY_TYPE/$dir
        popd
    done
    popd
done
popd

popd
