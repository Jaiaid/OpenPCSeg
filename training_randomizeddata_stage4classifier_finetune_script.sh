#!/bin/bash

python3 train.py  --pretrained_model ~/Downloads/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth \
--ckp ~/Downloads/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth \
--cfg_file tools/cfgs/voxel/semantic_kitti/train_randomized_stage4_classifier_finetune_36_236_epoch.yaml \
--epochs 236 --finetune --workers 0 --local_rank 1 --tcp_port 45000 --launcher pytorch > training1.log &

python3 train.py  --pretrained_model ~/Downloads/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth \
--ckp ~/Downloads/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth \
--cfg_file tools/cfgs/voxel/semantic_kitti/train_randomized_stage4_classifier_finetune_36_236_epoch.yaml \
--epochs 236 --finetune --workers 0 --local_rank 0 --tcp_port 46000  --launcher pytorch | tee training_randomizeddata_rank0.log

# --pretrained_model ~/Downloads/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth \
# --ckp ~/Downloads/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth \
