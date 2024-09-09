import random
import os
import shutil
import numpy as np
import argparse

SEED = 3400
TRAIN_EVAL_SPLIT_OUT_OF10 = 8

if __name__=="__main__":
    random.seed(SEED)

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--dir", "-dir", type=str, required=True, help="directory with pcd directory containing pcd files, assumed contain labels in labels folder")
    arg_parser.add_argument("--output-dir", "-o", type=str, required=True, help="directory where label and pcd files will be saved in train and val folder")

    args = arg_parser.parse_args()

    dataroot = args.dir
    outdir = args.output_dir
    os.makedirs(os.path.join(outdir, "train"), exist_ok=True)
    os.makedirs(os.path.join(outdir, "eval"), exist_ok=True)
    os.makedirs(os.path.join(os.path.join(outdir, "train"), "labels"), exist_ok=True)
    os.makedirs(os.path.join(os.path.join(outdir, "eval"), "labels"), exist_ok=True)
    os.makedirs(os.path.join(os.path.join(outdir, "train"), "pcds"), exist_ok=True)
    os.makedirs(os.path.join(os.path.join(outdir, "eval"), "pcds"), exist_ok=True)

    label_dict = {}
    filelist = list(os.listdir(os.path.join(dataroot, "pcds")))
    # take each 10
    for i in range(0, len(filelist), 10):
        part_filelist = filelist[i:i+10]
        random.shuffle(part_filelist)

        for idx, filename in enumerate(part_filelist):
            file_bname = os.path.basename(filename).split(".")[0]

            with open(os.path.join(os.path.join(dataroot, "labels"), file_bname+".txt")) as file:
                # assuming only one . is in filename to split name and extension
                lines = file.readlines()
                labels = []
                for line in lines:
                    number = int(line.split(',')[0])
                    if idx >= 0:
                       if number not in label_dict:
                          label_dict[number] = 0
                       label_dict[number] += 1
                    lower_half, upper_half = map(int, line.split(','))  # Extract the two columns
                    label = (upper_half << 16) | lower_half   # Combine the upper and lower halves into a 32-bit label
                    labels.append(label)

            pcd_filepath = os.path.join(os.path.join(dataroot, "pcds"), file_bname+".pcd")

            if idx < TRAIN_EVAL_SPLIT_OUT_OF10:
                datatype = "train"
            else:
                datatype = "eval"

            labelfile_outpath = os.path.join(os.path.join(os.path.join(outdir, datatype), "labels"), file_bname + ".label") 
            pcdfile_outpath = os.path.join(os.path.join(os.path.join(outdir, datatype), "pcds"), file_bname + ".pcd")

            # create the label file
            #labels_array = np.array(labels, dtype=np.uint32)  # Assuming 32-bit labels
            #labels_array.tofile(labelfile_outpath)
            # copy the pcd file
            # print(pcd_filepath, pcdfile_outpath)
            #shutil.copy(pcd_filepath, pcdfile_outpath)
    print(label_dict)
