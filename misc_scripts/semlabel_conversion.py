import os
import numpy as np
import argparse


if __name__=="__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--dir", "-dir", type=str, required=True, help="directory with label files in txt format")
    arg_parser.add_argument("--output-dir", "-o", type=str, required=True, help="directory where label bin files will be saved")

    args = arg_parser.parse_args()
    dataroot = args.dir

    label_dict = {}
    for filename in os.listdir(dataroot):
        with open(os.path.join(dataroot, filename)) as file:
            # assuming only one . is in filename to split name and extension
            file_bname = os.path.basename(filename).split(".")[0]
            lines = file.readlines()
            labels = []
            for line in lines:
                number = int(line.split(',')[0]) 
                if number not in label_dict:
                    label_dict[number] = 1
                label_dict[number] += 1
                lower_half, upper_half = map(int, line.split(','))  # Extract the two columns
                label = (upper_half << 16) | lower_half   # Combine the upper and lower halves into a 32-bit label
                labels.append(label)

            labels_array = np.array(labels, dtype=np.uint32)  # Assuming 32-bit labels
            labels_array.tofile(os.path.join(args.output_dir, file_bname + ".label"))
    print(label_dict, len(label_dict))
    sum = 0
    for i in label_dict:
        sum += label_dict[i]
    print(sum)

    for i in label_dict:
        print(i, label_dict[i]*100/sum)

