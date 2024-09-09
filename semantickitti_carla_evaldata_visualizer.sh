#!/bin/bash

set -x

ROOT_DIR=`pwd`
DATAROOT_ABS_PATH=~/data/dataset/semantickitti/semantic_eval/2/model_feed_data
PYTHON_SCRIPT_PATH=$ROOT_DIR/tools/visualizer/carlamatplotlib_pngcreator.py

FILE_INDEX=$1
OUTPUT_DIR=$ROOT_DIR/$2
echo $OUTPUT_DIR

# making a directory to contain the output
mkdir $OUTPUT_DIR

# activate venv
source $ROOT_DIR/../venv_2dpass/bin/activate

pushd $DATAROOT_ABS_PATH

# for original data
python3 $PYTHON_SCRIPT_PATH -bin velodyne/$FILE_INDEX.bin -label labels/$FILE_INDEX.label \
-yaml $ROOT_DIR/tools/visualizer/semantic-kitti.yaml \
-o $OUTPUT_DIR/original_$FILE_INDEX.png

# go insider each method's gained data
# create the label link
# run the eval
for METHOD in kdtree-only draco octree;
do
    pushd $METHOD
    # travarse through different parameter gained compression
    for dir in `ls .`;
    do
        pushd $dir
        # create link as named 08 for repository dataloader to find
        python3 $PYTHON_SCRIPT_PATH -bin velodyne/$FILE_INDEX.bin -label labels/$FILE_INDEX.label \
        -yaml $ROOT_DIR/tools/visualizer/semantic-kitti.yaml \
        -o $OUTPUT_DIR/${METHOD}_${dir}_${FILE_INDEX}.png
        popd
    done
    popd
done

# our directory structure is different
pushd our
for METHOD in `ls .`;
do
    pushd $METHOD
    # travarse through different parameter gained compression
    for dir in `ls .`;
    do
        pushd $dir
        # create link as named 08 for repository dataloader to find
        python3 $PYTHON_SCRIPT_PATH -bin velodyne/$FILE_INDEX.bin -label labels/$FILE_INDEX.label \
        -yaml $ROOT_DIR/tools/visualizer/semantic-kitti.yaml \
        -o $OUTPUT_DIR/${METHOD}_${dir}_${FILE_INDEX}.png
        popd
    done
    popd
done
popd 

popd

set +x