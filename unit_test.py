#!/usr/bin/env python
# coding=utf-8
'''
Author:Ayush Ishan
Date:Wed March 3 17:56 2022
Info:
'''

import os

import numpy as np
import matplotlib.pyplot as plt

DataLoaderTest = True

if DataLoaderTest:
    print("======CarlaH5Data test start======")
    from carla_loader import CarlaH5Data
    from torchvision.utils import make_grid

    base_path = "/home/ayush/carla_cil_dataset/AgentHuman"
    data = CarlaH5Data(
        train_folder=os.path.join(
            base_path,
            "chosen_weather_train/clearnoon_h5/"),
        eval_folder=os.path.join(
            base_path,
            "chosen_weather_test/clearnoon_h5/"),
        batch_size=128,
        num_workers=10)

    train_loader = data.loaders["train"]
    eval_loader = data.loaders["eval"]

    print(len(train_loader))
    print(len(eval_loader))

    for i, (img, speed, _, _) in enumerate(train_loader):
        show_img = make_grid(img)
        plt.imshow((np.transpose(
            show_img.numpy(),
            (1, 2, 0))*255).astype(np.uint8))
        plt.show()
        #print(one_hot)
        if i == 60:
            break