import os
import re
import matplotlib.pyplot as plot
import argparse

system_name_pattern = r"Method:\s*([\w-]+),\s*(.*)"
iou_report_pattern = r"^\|\s*(\w+)\s*\|\s*([\d\.]+)\s*\|$"

NAME_TO_LABEL_DICT = {"uncompressed": "original", "draco": "draco", "octree": "octree", "kdtree-only": "kdtree", "lidcom": "lidcom"}
COLOR_MAP = {"uncompressed": "r", "draco": "b", "octree": "g", "lidcom": "orange", "kdtree-only": "purple"}
LABEL_EXCLUDE_LIST = ["Wall", "All", "Fence", "Other", "Pedestrian", "RoadLine", "TrafficSign",
                      "Sky", "Ground", "Bridge", "GuardRail", "TrafficLight", "Static", "Terrain", "Other2",
                      "Other3", "Other4", "Other5", "Other6", "Other7"]

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--log-file", "-log", type=str, help="log file path containing val. iou information of multiple systems")

    args = argparser.parse_args()

    loss = []
    val_miou = []
    epoch = []
    epoch_valiou = []
    # no system detected
    cur_system_name = None
    system_param_name = None
    data_dict = {}
    plotdata_dict = {}
    with open(args.log_file) as fin:
        for logline in fin.readlines():
            result = re.search(system_name_pattern, logline)
            if result is not None:
                # summarize and add previous class data in dict
                # if class name is not None that means another class data was being collected
                if cur_system_name is not None:
                    print(cur_system_name)
                    mean = 0
                    for entry in data_dict[cur_system_name]:
                        mean += data_dict[cur_system_name][entry]
                    print(cur_system_name, data_dict[cur_system_name])
                    print(len(data_dict[cur_system_name]))
                    mean /= len(data_dict[cur_system_name])
                    plotdata_dict[cur_system_name] = (mean, COLOR_MAP[method_name], cur_system_name)
                # new system name found
                # collect the name, change state

                method_name = result.groups()[0]
                system_param_name = result.groups()[1]
                cur_system_name = method_name + "," + system_param_name
                if cur_system_name not in data_dict:
                    data_dict[cur_system_name] = {}

            result = re.search(iou_report_pattern, logline)
            if result is not None:
                class_name = result.groups()[0]
                if class_name not in LABEL_EXCLUDE_LIST:
                    # print(class_name, float(result.groups()[1]))
                    data_dict[cur_system_name][class_name] = float(result.groups()[1])
    # to summarize the last system got
    if cur_system_name is not None:
        print(cur_system_name)
        mean = 0
        for entry in data_dict[cur_system_name]:
            mean += data_dict[cur_system_name][entry]
#        print(cur_system_name, data_dict[cur_system_name])
        mean /= len(data_dict[cur_system_name])
        print(len(data_dict[cur_system_name]))
        plotdata_dict[cur_system_name] = (mean, COLOR_MAP[method_name], cur_system_name)

    fig, ax = plot.subplots()
    print(plotdata_dict.items())
    ax.bar(x=list(range(len(plotdata_dict))), height=[item[1][0] for item in plotdata_dict.items()], color=[item[1][1] for item in plotdata_dict.items()])
    ax.set_xticks(list(range(len(plotdata_dict))))
    ax.set_xticklabels([item[1][2] for item in plotdata_dict.items()], rotation=90)
    # title
    ax.set_ylabel("Mean IoU")

    fig.savefig("miou_system.png", dpi=600, bbox_inches="tight")


    for system in plotdata_dict.items():
        print(system[0], ":", system[1][0])
