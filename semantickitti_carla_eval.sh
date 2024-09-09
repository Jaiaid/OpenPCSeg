#!/bin/bash

set -x

ROOT_DIR=`pwd`
DATAROOT_ABS_PATH=$ROOT_DIR/model_feed_data

TEMPLATE_CFG_FILE=$1
CKP_PATH=$2

# activate venv
source $ROOT_DIR/../venv_openpcseg/bin/activate

echo "Evaluation using ckp $CKP_PATH" > eval_result.log

# eval the original collected data
rm -r $DATAROOT_ABS_PATH/predicted
mv $DATAROOT_ABS_PATH 08
ln -s 08 00
CUR_DIR=`pwd`
rm -r predicted
mkdir predicted
sed "s,DATA_PATH:,DATA_PATH: \'$CUR_DIR\',g" $TEMPLATE_CFG_FILE > tmp.cfg
echo "Method: uncompressed,original" >> eval_result.log
python3 train.py --eval --ckp $CKP_PATH --cfg_file tmp.cfg --workers 0 >> eval_result.log
rm 00
mv 08 $DATAROOT_ABS_PATH
mv predicted $DATAROOT_ABS_PATH/

pushd $DATAROOT_ABS_PATH
# go insider each method's gained data
# create the label link
# run the eval
for METHOD in kdtree-only draco octree;
do
    pushd $METHOD
    # travarse through different parameter gained compression
    for dir in `ls .`;
    do
        CUR_DIR=`pwd`
        # create link as named 08 for repository dataloader to find
        rm -r $dir/predicted
        mv $dir 08
        ln -s 08 00
        # convert decompressed pcd to velodyne from each parameter gained compression
        pushd $ROOT_DIR
        rm predicted
        mkdir predicted
        sed "s,DATA_PATH:,DATA_PATH: \'$CUR_DIR\',g" $TEMPLATE_CFG_FILE > tmp.cfg
        echo "Method: $METHOD,$dir" >> eval_result.log
        python3 train.py --eval --ckp $CKP_PATH --cfg_file tmp.cfg >> eval_result.log
        head tmp.cfg
        popd
        rm 00
        mv 08 $dir
        mv $ROOT_DIR/predicted $dir/
    done
    popd
done

# our directory structure is different
pushd our/original
for dir in `ls .`;
do
    CUR_DIR=`pwd`
    # create link as named 08 for repository dataloader to find
    rm -r $dir/predicted
    mv $dir 08
    ln -s 08 00
    pushd $ROOT_DIR
    rm predicted
    mkdir predicted
    sed "s,DATA_PATH:,DATA_PATH: \'$CUR_DIR\',g" $TEMPLATE_CFG_FILE > tmp.cfg
    echo "Method: lidcom,$dir" >> eval_result.log
    python3 train.py --eval --ckp $CKP_PATH --cfg_file tmp.cfg >> eval_result.log
    head tmp.cfg 
    popd
    mv 08 $dir
    rm 00
    mv $ROOT_DIR/predicted $dir/
done
popd

pushd our/with_dublicate_points
for dir in `ls .`;
do
    CUR_DIR=`pwd`
    # create link as named 08 for repository dataloader to find
    rm -r $dir/predicted
    mv $dir 08
    ln -s 08 00
    pushd $ROOT_DIR
    rm predicted
    mkdir predicted
    sed "s,DATA_PATH:,DATA_PATH: \'$CUR_DIR\',g" $TEMPLATE_CFG_FILE > tmp.cfg
    echo "Method: lidcom,dup_$dir" >> eval_result.log
    python3 train.py --eval --ckp $CKP_PATH --cfg_file tmp.cfg >> eval_result.log
    head tmp.cfg
    popd
    mv 08 $dir
    rm 00
    mv $ROOT_DIR/predicted $dir/
    break
done
popd

popd

set +x
