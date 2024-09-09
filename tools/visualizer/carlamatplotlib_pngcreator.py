import yaml
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import argparse


def save_rawdata_as_png(args):
    # raw_data = np.load(path)
    raw_data = np.fromfile(args.velodyne_file, dtype=np.float32).reshape((-1, 4))
    raw_label = np.fromfile(args.velodyne_label, dtype=np.uint32).reshape((-1, 1))
    with open(args.yaml_file, 'r') as stream:
        CFG = yaml.safe_load(stream)
    learning_map = CFG['learning_map']

    color_dict = CFG["color_map"]
    learning_map_inv = CFG["learning_map_inv"]

    color_dict_mapped = dict()
    for cls in range(29):
        color_dict_mapped[cls] = color_dict[learning_map[cls]]

    # color_dict_mapped[7] = [0, 128, 128]  # bicyclist
    # color_dict_mapped[12] = [128, 128, 128]  # other-ground
    # color_dict_mapped[14] = [212, 242, 231]  # fence
    # color_dict_mapped[19] = [218, 165, 32]  # traffic-sign

    raw_label = raw_label & 0xFFFF  # delete high 16 digits binary
    raw_label = np.vectorize(learning_map.__getitem__)(raw_label).reshape((-1,1))

    colors = []
    for label in raw_label[:, -1]:
        colors.append(color_dict_mapped[label][::-1])

    colors = np.vstack(colors)
    if raw_data.shape[1] == 4:
        points = raw_data[:, 0:3]
    else:
        points = raw_data[:, 3:6]

    color_points = np.concatenate((points, colors), axis=1)
    
    # Normalize the point cloud coordinates to fit them into image space
    # Example: Scale the Z coordinate to represent depth for a depth image
    # z_values = color_points [:, 2]
    # z_min, z_max = z_values.min(), z_values.max()
    # normalized_depth = (z_values - z_min) / (z_max - z_min) * 255.0  # Normalize to 0-255

    # Reshape or project the 3D points into a 2D grid if necessary
    # Example: Create a scatter plot for depth visualization
    # print(color_points.shape)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(color_points[:, 0], color_points[:, 1], c=color_points[:, 3:6]/255.0)
    # plt.colorbar(label="Depth")
    plt.title("Point Cloud 2d projection")
    plt.axis('equal')

    # Save the 2D image as a PNG file
    plt.savefig(args.output_path)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(color_points[:, 0], color_points[:, 1], color_points[:, 2], c=color_points[:, 3:6]/255.0)
    # plt.colorbar(label="Depth")
    plt.title("Point Cloud 3d Map")

    # Save the 2D image as a PNG file
    plt.savefig(args.output_path[0:-4] + "_3d.png")


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--velodyne-file", "-bin", type=str, help="velodyne bin file")
    argparser.add_argument("--velodyne-label", "-label", type=str, help="velodyne label file")
    argparser.add_argument("--yaml-file", "-yaml", type=str, help="yaml file containing color information", default="semantic-kitti.yaml")
    argparser.add_argument("--output-path", "-o", type=str, help="output path of birds eye view of pcd")

    args = argparser.parse_args()
    assert args.output_path[-4:] == ".png", "{0} does not ends with .png extension".format(args.output_path)

    save_rawdata_as_png(args)
