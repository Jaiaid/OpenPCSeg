<img src="docs/figs/pcseg_logo.png" align="right" width="30%">

# OpenPCSeg: An Open Source Point Cloud Segmentation Codebase
[![License](https://img.shields.io/static/v1?label=License&message=Apache-2.0&color=yellow)]()
[![open issues](https://isitmaintained.com/badge/open/PJLab-ADG/PCSeg.svg)](https://github.com/PJLab-ADG/PCSeg/issues)
[![GitHub forks](https://img.shields.io/github/forks/PJLab-ADG/PCSeg.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/PJLab-ADG/PCSeg)

`OpenPCSeg` is an open-source point cloud segmentation toolbox based on [PyTorch](https://pytorch.org/), heading towards the unification and thriving of 3D scene understanding and its related areas. With the help of `OpenPCSeg`, we benchmark methods in a way that pursues fairness, efficiency, and effectiveness, on prevailing large-scale point cloud datasets. At this moment, `OpenPCSeg` focuses on outdoor point cloud segmentation for autonomous driving.

**This project is developed and maintained by Autonomous Driving Group [at] [Shanghai AI Laboratory](https://www.shlab.org.cn/) (ADLab).**


| <img src="./docs/figs/demo-bev-1.gif" align="middle"> | <img src="./docs/figs/demo-bev-2.gif" align="middle"> | <img src="./docs/figs/demo-bev-3.gif" align="middle"> |
| :-: | :-: | :-: |
| <img src="./docs/figs/demo-rv-1.gif" align="middle"> | <img src="./docs/figs/demo-rv-2.gif" align="middle"> | <img src="./docs/figs/demo-rv-3.gif" align="middle"> |


### Highlight
- 🌈 **Comprehensive:** We support the full spectrum of point cloud scene understanding tasks on standard large-scale benchmarks, with backbones across various 2D & 3D modalities.
- ⚖️ **Fair & Reproducible:** We unify the training, validation, and testing configurations, resulting in directly comparable 3D segmentation performance.
- 🚀 **Fast & Accurate:** Our implementations yield much better segmentation accuracy as well as training and inference speed than the originally reported results.


### Supported Task

| # | Task | Emphasis | Dataset | Method |
| :-: | :-: | :-: | :-: | :-: |
| :red_car: | Fully-Supervised LiDAR Segmentation | Accuracy | 2 | 4 |


## Changelog
- \[2023.4\] - Support sequence-wise `OpenPCSeg` inference and visualization on Waymo Open Dataset.
- \[2023.3\] - Initial release of `OpenPCSeg v1.0`.


## Upcoming Features
- Support NuScenes Dataset
- Add implementations of range-view algorithms
- Add toolbox for competition submission
- Add visualiztion of 3D segmentation results


## Outline

- [Supported Methods](#supported-methods)
- [Supported Benchmark](#supported-benchmark)
- [Model Zoo](#model-zoo)
- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Getting Started](#getting-started)
- [Visualization](#visualization)
- [Citation](#citation)
- [Authors](#authors)
- [License](#license)
- [Contact](#contact)

## Supported Methods

- [x] **[MinkowskiNet](https://github.com/NVIDIA/MinkowskiEngine)**
- [x] **[Cylinder3D](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhu_Cylindrical_and_Asymmetrical_3D_Convolution_Networks_for_LiDAR_Segmentation_CVPR_2021_paper.pdf)**
- [x] **[SPVCNN](https://arxiv.org/abs/2007.16100)**
- [x] **[RPVNet](https://openaccess.thecvf.com/content/ICCV2021/papers/Xu_RPVNet_A_Deep_and_Efficient_Range-Point-Voxel_Fusion_Network_for_LiDAR_ICCV_2021_paper.pdf)**
- [ ] More to come...

## Supported Benchmark

#### LiDAR Semantic Segmentation (5)

- [x] **[SemanticKITTI](http://www.semantic-kitti.org/tasks.html#semseg)**
- [x] **[ScribbleKITTI](https://paperswithcode.com/dataset/scribblekitti)**
- [x] **[Waymo Open](https://waymo.com/open/)**
- [ ] **[A2D2](https://www.a2d2.audi/a2d2/en.html)** (coming soon)
- [ ] **[nuScenes](https://www.nuscenes.org/nuscenes)** (coming soon)

#### LiDAR Panoptic Segmentation (3)

- [ ] **[Panoptic nuScenes](https://www.nuscenes.org/panoptic)** (coming soon)
- [ ] **[Panoptic SemanticKITTI](http://www.semantic-kitti.org/tasks.html#panseg)** (coming soon)
- [ ] **[4D Panoptic SemanticKITTI](http://www.semantic-kitti.org/tasks.html#panseg4d)** (coming soon)


## Model Zoo

### SemanticKITTI Dataset Representative Models
Selected supported methods are shown in the below table. The results are mean IoU performance of moderate difficulty on the *val* set of SemanticKITTI dataset.
* All LiDAR-based models are trained with 2 A100 GPUs and are available for download.
* The training and validation are executed with CUDA 11.3 and PyTorch 1.10.
* All models are trained with *merely train split* of SemanticKITTI Dataset.
* Prediction from our models are directly used for evaluation, without employing any Test Time Augmentation or ensembling.

|                                             | training time |   mIoU   |  download  | 
|---------------------------------------------|--------------:|:--------:|:----------:|
| [MinkowskiNet](tools/cfgs/voxel/semantic_kitti/minkunet_mk34_cr10.yaml) | ~12.0 hours | 70.04 | [model-737M](https://www.dropbox.com/s/a9gjxeziy6rbiui/semkitti_minkunet_mk34_cr16_checkpoint_epoch_36.pth?dl=0) | 
| [Cylinder3D](tools/cfgs/voxel/semantic_kitti/cylinder_cy480_cr10.yaml)  |  ~8.7 hours | 66.07 | [model-56M](https://www.dropbox.com/s/imtcmn9z4qldc2h/semkitti_cylinder_cy480_cr10_checkpoint_epoch_35.pth?dl=0) |
| [SPVCNN](tools/cfgs/fusion/semantic_kitti/spvcnn_mk18_cr10.yaml)        | ~13.1 hours | 68.58 | [model-166M](https://www.dropbox.com/s/94j8rxkxlo2j924/semkitti_spvcnn_mk18_cr10_checkpoint_epoch_36.pth?dl=0) |
| [RPVNet](tools/cfgs/fusion/semantic_kitti/rpvnet_mk34_cr17_5.yaml)      | ~14.5 hours | 68.86 | [model-980M](https://www.dropbox.com/s/sf71far59ij8i3c/semkitti_rpvnet_mk34_cr175_checkpoint_epoch_36.pth?dl=0) |


### Waymo Open Dataset Representative Models
We are not supposed to provide pre-trained weights due to [Waymo Dataset License Agreement](https://waymo.com/open/terms/), but you can easily achieve similar performance by training according to the default configs.

|                                             | training time |   mIoU   |
|---------------------------------------------|--------------:|:--------:|
| [MinkowskiNet](tools/cfgs/voxel/waymo/minkunet_mk34_cr16.yaml) | ~25.0 hours | 69.20 |
| [Cylinder3D](tools/cfgs/voxel/waymo/cylinder_cy480_cr10.yaml)  | ~19.2 hours | 66.42 |
| [SPVCNN](tools/cfgs/fusion/waymo/spvcnn_mk34_cr16.yaml)        | ~28.0 hours | 69.37 |


## Installation
Please refer to [INSTALL.md](docs/INSTALL.md) for the installation details.


## Data Preparation

```
└── data_root 
    └── nuscenes
    └── semantickitti
    └── scribblekitti
    └── waymo_open
```

Please refer to [DATA_PREPARE.md](docs/DATA_PREPARE.md) for the details to prepare the [nuScenes](https://www.nuscenes.org/nuscenes), [SemanticKITTI](http://www.semantic-kitti.org/tasks.html#semseg), [ScribbleKITTI](https://arxiv.org/abs/2203.08537), and [Waymo Open](https://waymo.com/open/) datasets.


## Getting Started
Please refer to [GET_STARTED.md](docs/GET_STARTED.md) to learn more usage about this codebase.


## Visualization
We recently supported a OpenPCSeg visualization tool for Waymo Open Dataset, please check [INFER_WAYMO.md](docs/INFER_WAYMO.md).

Here are some inference & visualization results:
<img src="docs/figs/wod_vis_01.png" align="center" width="70%">
<img src="docs/figs/wod_vis_02.png" align="center" width="70%">

## Citation
If you find this work helpful, please kindly consider citing:
```bib
@misc{openpcseg2023,
    title={OpenPCSeg: An Open Source Point Cloud Segmentation Codebase},
    author={Liu Youquan, Bai Yeqi, Kong Lingdong, Chen Runnan, Hou Yuenan, Shi Botian, Li Yikang},
    howpublished = {\url{https://github.com/PJLab-ADG/PCSeg}},
    year={2023}
}
```

## Authors
Liu Youquan, Bai Yeqi†, Kong Lingdong, Chen Runnan, Hou Yuenan, Shi Botian, Li Yikang

†Project Lead

## License
OpenPCSeg is released under the **Apache 2.0 license**, while some specific operations in this codebase might be with other licenses. Please refer to [LICENSE](docs/LICENSE) for a more careful check, if you are using our code for commercial matters.

## Contact
If you have questions about this repo, please contact Bai Yeqi (baiyeqi@pjlab.org.cn) or Shi Botian (shibotian@pjlab.org.cn).

## Acknowledgement
The overall structure of this repo is derived from [OpenPCDet](https://github.com/open-mmlab/OpenPCDet). 

Part of our implementation uses code from repositories below:
* [1] https://github.com/xinge008/Cylinder3D
* [2] https://github.com/mit-han-lab/spvnas
* [3] https://github.com/TiagoCortinhal/SalsaNext
* [4] https://github.com/open-mmlab/OpenPCDet
* [5] https://github.com/mit-han-lab/torchsparse

Thank the authors for their great work!


# "carla_modification" Branch Description

This branch contains the semantic segmentation training and evaluation scripts and corresponding Python code. The target dataset is 3d point cloud dataset generated by Carla simulator's semantic segmentation LiDAR. We have done training only on a subset of the instances offered by Carla semantic segmentation LiDAR.
#### Assumptions
* We assume the parent dir of repository directory contains a venv named `venv_2dpass`. You may need to modify bash scripts venv activation line, if not.


### Workflow Summary
1. Transform Carla dataset (.pcd and .txt for label) to SemanticKITTI format (velodyne .bin format from .pcd and .label from .txt)
2. Structure the dataset like following
   <a name="tds">For training, </a>
    ```
    <data root dir>
    |--00
    |   |-labels
    |   |-velodyne
    |--08
        |-labels
        |-velodyne
    ```
    `labels` folder contains the label files `velodyne` contains the PCD data files. Each PCD and corresponding labels have same basename with `.bin` and `.label` suffix. `00` folder is for training data, `08` is for validation.
  
    For evaluation/testing
    ```
    <data root dir>
    |-labels
    |-velodyne
    ```
3. Update provided configuration (`.cfg`) file with appropriate data path (root dir) according to task (training/test)
4. run training using `training_randomizeddata_stage4_classifier_finetune_script.sh`
5. run testing using `semantickitti_carla_eval.sh` (it's bulk evaluation for multiple different method generated dataset but they are separated and should be easy yto identify)

### Training Dataset Preparation
#### Train-Val split
1. Run `misc_scripts/dataset_randomizer.py`
    ```
    python3 misc_scripts/dataset_randomizer.py --dir <directory with pcd and labels directory containing pcd and label files> --output-dir <directory where label and pcd files will be saved in train and eval folder>
    ```
   Note that, the generated folder name will be `train`, `eval` not `00`, `08`. To change the split ratio modify `TRAIN_EVAL_SPLIT_OUT_OF10` and select some integer from [0,10]. Currently it's 80% (every 8 out of 10 is placed in train).

#### SemanticKITTI Conversion
<a name="skconversion"></a>
**All commands are to be run from repository root**
1. Build `misc_scripts\pcd2bin.cpp` (taken and modified from https://github.com/leofansq/Tools_RosBag2KITTI repository). Place it in repository root directory.
    ```
    g++ misc_scripts/pcd2bin.cpp -o pcd2bin
    ```
2. To convert pcd to velodyne bin of SemanticKITTI format
    ```
    ./pcd2bin <directory containing the pcds> <directory where the bin files will be put>
    ```
    To convert `.txt` label to `.label` run
    ```
    python3 misc_scripts/semlabel_conversion.py --dir <directory with label files in txt format> --output-dir <directory where label bin files will be saved>
    ```
3. Structure the training data as mentioned in [Workflow Summary](#tds). 

### Training
**All commands are to be run from repository root**

1. Download MinkowskiNet (model-737M) as instructed [here](https://github.com/Jaiaid/OpenPCSeg/tree/master?tab=readme-ov-file#semantickitti-dataset-representative-models) here. This will be our pretrained model which will be finetuned.
2. Edit `tools/cfgs/voxel/semantic_kitti/train_randomized_stage4_classifier_finetune_36_236_epoch.yaml` and put the dataset folder path (the folder which has `00` and `08` directory) by editing `DATA_PATH` variable.
    ```
    DATA_PATH:  # hint: customize your data path
    ```
3. Run the script to run training in 2-GPU machine (trained on machine with two RTX-A4000 each with ~16GiB memory). May need to edit some path after `--ckp` and `--cfg` argument. `--ckp` is for pretrained model checkpoint which in current script is taken from ~\Downloads. The script will run for 200 more epoch over already 36epoch trained pretrained model.
    ```
    bash training_randomizeddata_stage4classifier_finetune_script.sh
    ```
**Note**: The script is for distributed training. For single GPU training comment out line [3,6] and set `IF_DIST` to `False` in `tools/cfgs/voxel/semantic_kitti/train_randomized_stage4_classifier_finetune_36_236_epoch.yaml`

### Testing

#### Convert to SemanticKITTI
The dataset conversion is principally same as what is done in [training](#skconversion)

We provide a script to run inference on dataset and generate the prediction in bulk (multiple method generated compression and corresponding decompressed PCDs).  We assume the decompressed PCDs are in a folder in repository root folder named `model_feed_data`

```
    model_feed_data
    |--draco
    |   |--<param1>
    |       |-labels
    |       |-velodyne
    .   .
    .   .
    .   .
    |--kdtree-only
    |   |--<param1>
    |       |-labels
    |       |-velodyne
    .   .
    .   .
    .   .
    |--our
    |   |- original
        |   |--<param1>
        |       |-labels
        |       |-velodyne
        .   .
        .   .
        .   .
        |   |- with_dublicate_points
        |   |--<param1>
        |       |-labels
        |       |-velodyne
        .   .
        .   .
        .   .
    |--labels
    |--velodyne
```
`labels` and `velodyne` contains the ground truth of original data which was compressed.
Initially each directory of method and parameter contained a folder `decompressed` containing the PCDs. To conver all in one go, run
```
bash misc_scripts/semantickitti_conversion.sh
```

#### Eval. Run
For evaluation run (assuming same structure data),
```
bash semantickitti_carla_eval.sh eval_randomized_stage4_classifier_finetune_36_236_epoch.yaml checkpoint_epoch_220_best.pth 
```
`checkpoint_epoch_220_best.pth` was our trained model on our data which can be downloaded from [here](https://drive.google.com/file/d/1iRjMpquRVBHqPzxcdUWue63LwxCh2yq_/view?usp=drive_link)

#### Unordered Label File Handling
If any decompression method scrambles the original PCD point order the label provided by Carla won't work. To cicumvent the issue we provide a script which does a nearest neighbor search to map each point of new PCD to original and create a new label file (.txt format).

```
python3 misc_scripts\labelfile_regen_nnsearch.py -opdir <orignal PCD dir> -olabtdir <original label text dir> -updir <unordered PCD dir> -o <output label(.txt) file dir>
```

A bash script for bulk conversion is provided
```
bash misc_scripts/semantickitti_labelfile_regen_nnsearch.sh
```

### Instance Label Map/Ignore

To map a semantic label to a name, to a color or to another semantic label when doing training/evaluation modify `pcseg/data/dataset/semantickitti/semantickitti_utils_carla.py`. To map to another label, modify `LEARNING_MAP`. To know a label's id check `LABEL_NAME_MAPPING`.

The number of unique class names is determined by a variable inside `SemkittiCarlaVoxelDataset` class `__init__` in file `pcseg/data/dataset/semantickitti/semantickitti_carla_voxel.py`.

### Visualization
We have modified original provided visualization script to visualize any data sample in SemanticKITTI format
```
python3 tools/visualizer/vis_SemanticKITTI.py --velodyne-file <velodyne bin file> --velodyne-label <velodyne label file> --yaml-file <yaml file containing color information>
```

For yaml file sample, see `tools/visualizer/semantic-kitti.yaml`