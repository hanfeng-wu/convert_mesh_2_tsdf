# configuration file to claim the data we used
# author: ynie
# date: Jan, 2020
import os

shapenet_categlory_pair = {
        "watercraft": "04530566",
        "rifle": "04090263",
        "display": "03211117",
        "lamp": "03636649",
        "speaker": "03691459",
        "cabinet": "02933112",
        "chair": "03001627",
        "bench": "02828884",
        "car": "02958343",
        "airplane": "02691156",
        "sofa": "04256520",
        "table": "04379243",
        "phone": "04401088"
}

our_categories = [
        "airplane",
        "bench",
        "cabinet",
        "car",
        "chair",
        "display",
        "lamp",
        "speaker",
        "rifle",
        "sofa",
        "table",
        "phone",
        "watercraft"
    ]
our_categories = [shapenet_categlory_pair[cat] for cat in our_categories]

shapenet_path = './datasets/ShapeNetCore.v1'
shapenet_normalized_path= './datasets/ShapeNetCore.v1_normalized'
shapenet_rendering_path = './datasets/ShapeNetRenderings'
camera_setting_path = './datasets/camera_settings'
model_view_path = './model_view_metadata/result.pkl'
watertight_mesh_path = './datasets/ShapeNetCore.v1_watertight'

shape_scale_padding = 0
total_view_nums = 20
