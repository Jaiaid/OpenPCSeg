# {9(Vegetation): 20515729, 5(Pole): 11339131, 1(Building): 131037169, 19(Static): 3374154, 
# 16(RailTrack): 8271591, 2(Fence): 2619296, 11(Wall): 14042911, 20(Dynamic): 1374545, 
# 10(Vehicles): 27410280, 22(Terrain): 3667327, 14(Ground): 11840571, 7(Road): 129189173, 21(Water): 533757,
# 8(SideWalk): 46935548, 6(RoadLine): 617391, 12(TrafficSign): 3412}
# 412771985

LABEL_NAME_MAPPING = {
    0: 'Unlabeled',
    1: 'Building',
    2: 'Fence',
    3: 'Other',
    4: 'Pedestrian',
    5: 'Pole',
    6: 'RoadLine',
    7: 'Road',
    8: 'SideWalk',
    9: 'Vegetation',
    10: 'Vehicles',
    11: 'Wall',
    12: 'TrafficSign',
    13: 'Sky',
    14: 'Ground',
    15: 'Bridge',
    16: 'RailTrack',
    17: 'GuardRail',
    18: 'TrafficLight',
    19: 'Static',
    20: 'Dynamic',
    21: 'Water',
    22: 'Terrain',
    23: 'Other2',
    24: 'Other3',
    25: 'Other4',
    26: 'Other5',
    27: 'Other6',
    28: 'Other7'
}

color_map = {
  0 : [0, 0, 0],
  1 : [128, 64, 128],
  2: [244, 35, 232],
  3: [70, 70, 70],
  4: [102, 102, 156],
  5: [190, 153, 153],
  6: [153, 153, 153],
  7: [250, 170, 30],
  8: [220, 220, 0],
  9: [107, 142, 35],
  10: [152, 251, 152],
  11: [70, 130, 180],
  12: [220, 20, 60],
  13: [255, 0, 0],
  14: [0, 0, 142],
  15: [0, 0, 70],
  16: [0, 60, 100],
  17: [0, 60, 100],
  18: [0, 0, 230],
  19: [119, 11, 32],
  20: [110, 190, 160],
  21: [170, 120, 50],
  22: [55, 90, 80],
  23: [45, 60, 150],
  24: [157, 234, 50],
  25: [81, 0, 81],
  26: [150, 100, 100],
  27: [230, 150, 140],
  28: [180, 165, 180]
}

LEARNING_MAP = {
    0: 0,  # "unlabeled"
    1: 1,  # "building"
    2: 9,  # "fence" mapped to "vegetation"
    3: 3,  # "other"
    4: 4,  # "pedestrian"
    5: 5,  # "pole"
    6: 7,  # "roadline" mapped to "road" ---------------------mapped
    7: 7,  # "road"
    8: 8,  # "sidewalk"
    9: 9,  # "vegetation"
    10: 10,  # "vehicles"
    11: 11,  # "wall"
    12: 5,  # "trafficsign" mapped to "pole"
    13: 3,  # "sky" mapped to "other"
    14: 8,  # "ground" mapped to "sidewalk"
    15: 15,  # "bridge"
    16: 16,  # "railtrack"
    17: 11,  # "guardrail" mapped to "wall"
    18: 18,  # "trafficlight"
    19: 1,  # "static" to "building"
    20: 20,  # "dynamic"
    21: 8,  # "water" mapped to "sidewalk"
    22: 8,  # "terrain" mapped to "sidewalk"
    23: 3,  # "other2" mapped to "other"
    24: 3,  # "other3" mapped to "other"
    25: 3,  # "other4" mapped to "other"
    26: 3,  # "other5" mapped to "other"
    27: 3,  # "other6" mapped to "other"
    28: 3,  # "other7" mapped to "other"
}

LEARNING_MAP_INV = {  # inverse of previous map
    0: 0,  # "unlabeled"
    1: 1,  # "outlier" mapped to "unlabeled" --------------------------mapped
    2: 2,  # "car"
    3: 3,  # "bicycle"
    4: 4,  # "bus" mapped to "other-vehicle" --------------------------mapped
    5: 5,  # "motorcycle"
    6: 6,  # "on-rails" mapped to "other-vehicle" ---------------------mapped
    7: 7,  # "truck"
    8: 8,  # "other-vehicle"
    9: 9,  # "person"
    10: 10,  # "bicyclist"
    11: 11,  # "motorcyclist"
    12: 12,  # "road"
    13: 13,  # "parking"
    14: 14,  # "sidewalk"
    15: 15,  # "other-ground"
    16: 16,  # "building"
    17: 97,  # "fence"
    18: 18,  # "other-structure" mapped to "unlabeled" ------------------mapped
    19: 19,  # "lane-marking" to "road" ---------------------------------mapped
    20: 20,  # "vegetation"
    21: 21,  # "trunk"
    22: 22,  # "terrain"
    23: 23,  # "pole"
    24: 24,  # "traffic-sign"
    25: 25,  # "other-object" to "unlabeled" ----------------------------mapped
    26: 26,  # "moving-car" to "car" ------------------------------------mapped
    27: 27,  # "moving-bicyclist" to "bicyclist" ------------------------mapped
    28: 28,  # "moving-person" to "person" ------------------------------mapped
}
LEARNING_IGNORE = {  # Ignore classes
    0: True,  # "unlabeled"
    1: False,  # "outlier" mapped to "unlabeled" --------------------------mapped
    2: False,  # "car"
    3: False,  # "bicycle"
    4: False,  # "bus" mapped to "other-vehicle" --------------------------mapped
    5: False,  # "motorcycle"
    6: False,  # "on-rails" mapped to "other-vehicle" ---------------------mapped
    7: False,  # "truck"
    8: False,  # "other-vehicle"
    9: False,  # "person"
    10: False,  # "bicyclist"
    11: False,  # "motorcyclist"
    12: False,  # "road"
    13: False,  # "parking"
    14: False,  # "sidewalk"
    15: False,  # "other-ground"
    16: False,  # "building"
    17: False,  # "fence"
    18: False,  # "other-structure" mapped to "unlabeled" ------------------mapped
    19: False,  # "lane-marking" to "road" ---------------------------------mapped
    20: False,  # "vegetation"
    21: False,  # "trunk"
    22: False,
    23: False,  # "trunk"
    24: False,  # "trunk"
    25: False,  # "trunk"
    26: False,  # "trunk"
    27: False,  # "trunk"
    28: False,  # "trunk"
}

#{9: 20515729, 5: 11339131, 1: 131037169, 19: 3374154, 16: 8271591, 2: 2619296, 11: 14042911, 20: 1374545, 10: 27410280, 22: 3667327, 14: 11840571, 7: 129189173, 21: 533757, 8: 46935548, 6: 617391, 12: 3412}
# 412771985
