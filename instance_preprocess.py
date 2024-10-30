#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from dataloader.dataset import SemKITTI

if __name__ == '__main__':
    # instance preprocessing
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-d', '--data_path', default='data')
    parser.add_argument('-o', '--out_path', default='data')
    parser.add_argument('-c', '--config_path', default='semantic-kitti.yaml')

    args = parser.parse_args()

    train_pt_dataset = SemKITTI(args.data_path + '/sequences/', imageset = 'train', return_ref = True, config_path=args.config_path)
    train_pt_dataset.save_instance(args.out_path)
    print('instance preprocessing finished.')