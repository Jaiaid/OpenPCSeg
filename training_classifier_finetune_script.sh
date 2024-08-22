#!/bin/bash

python3 train.py --pretrained_model ~/Downloads/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth \
--ckp ~/Downloads/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth \
--cfg_file tools/cfgs/voxel/semantic_kitti/train_classifier_finetune_36_50epoch.yaml \
--epochs 50 --finetune --workers 0 | tee training`date`.log

