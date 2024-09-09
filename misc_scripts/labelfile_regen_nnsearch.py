import os
import numpy as np
import open3d as o3d
import numpy as np
import argparse


if __name__=="__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--original-pcd-dir", "-opdir", type=str, required=True, help="directory containing original carla pcd")
    arg_parser.add_argument("--original-labeltxt-dir", "-olabtdir", type=str, required=True, help="directory containing original carla label txt format file")
    arg_parser.add_argument("--unordered-pcd-dir", "-updir", type=str, required=True, help="directory containing unordered pcds")
    arg_parser.add_argument("--output-dir", "-o", type=str, required=True, help="directory where label bin files will be saved by creating a labels directory inside")

    args = arg_parser.parse_args()

    for filename in os.listdir(args.original_pcd_dir):
        pcd_comp = o3d.io.read_point_cloud(os.path.join(args.unordered_pcd_dir, filename))
        pcd_orig = o3d.io.read_point_cloud(os.path.join(args.original_pcd_dir, filename))

        label_orig = []
        label_comp = []

        file_bname = os.path.basename(filename).split(".")[0]
        # print(os.path.join(args.unordered_pcd_dir, filename), os.path.join(args.original_pcd_dir, filename), os.path.join(args.original_labeltxt_dir, file_bname + ".txt"))
        with open(os.path.join(args.original_labeltxt_dir, file_bname + ".txt")) as file:
            # assuming only one . is in filename to split name and extension
            file_bname = os.path.basename(filename).split(".")[0]
            lines = file.readlines()
            labels = []
            for line in lines:
                number = int(line.split(',')[0]) 
                lower_half, upper_half = map(int, line.split(','))  # Extract the two columns
                label = (upper_half << 16) | lower_half   # Combine the upper and lower halves into a 32-bit label
                label_orig.append(label)

        # Convert point clouds to numpy arrays
        points_orig = np.asarray(pcd_orig.points)
        points_comp = np.asarray(pcd_comp.points)

        # Create KDTree for the original point cloud
        kdtree = o3d.geometry.KDTreeFlann(pcd_orig)

        # Find the nearest neighbor for each point in pcd_comp relative to pcd_orig
        for _, point in enumerate(pcd_comp.points):
            _, idx, _ = kdtree.search_knn_vector_3d(point, 1)
            # put that label in compressed pcd's label
            label_comp.append(label_orig[idx[0]])

        labels_array = np.array(label_comp, dtype=np.uint32)  # Assuming 32-bit labels
        labels_array.tofile(os.path.join(args.output_dir, file_bname + ".label"))
