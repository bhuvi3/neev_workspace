#!/usr/bin/env python

"""
Unit 2 assignment - Fisherfaces

Implement the Fisherfaces algorithm and test its efficacy on the Shonit WBC dataset.

Details can be found in this folder:

https://drive.google.com/open?id=0B1kGue54dxG7cVAwWWlkT2Q2YUU:

Linear Algebra Unit 2 assignment
In this folder, you will find two files:
 - A list of training images and their corresponding labels
 - A list of validation images and their corresponding labels

The assignment:
 - Implement the Fisherfaces algorithm in a way which will make it scale as the number of images increase (i.e. N >> n)
 - Create a Fisherfaces eigenvectors database using the training images (or a subset of them)
 - Invoke the evaluation module on the validation images and publish the accuracy

As in the Unit 1 assignment, please share the link to your github directory containing the code and a README.md file. Publish the accuracy numbers in the same file.

"""

import argparse
import math
import numpy as np
import pickle

def get_args():
    """
    Parse the command line arguments.

    """
    parser = argparse.ArgumentParser(description="Implement the Fisherfaces algorithm.")
    parser.add_argument('--train_data_file',
                        help='Specify the path to the text file containing the image names and labels for the train set.')
    parser.add_argument('--val_data_file',
                        help='Specify the path to the text file containing the image names and labels for the validation set.')
    parser.add_argument('--channel_type',
                        default='avg',
                        help='Specify the channel to pick from the image. Supported types: avg, r, g, b.')
    parser.add_argument('--rescale',
                        action='store_true',
                        help='Specify if the image matrix needs to be normalized by rescaling i.e., dividing each element by 255.')
    parser.add_argument('--eigenvector_db_path',
                        default=None,
                        help='Specify the path to where the eigenvector db needs to be serialized using pickle.')
    args = parser.parse_args()
    return args


def fisher_faces(train_data, val_data):
    """
    The Fisherfaces algorithm. It trains on the train_data and evaluates the accuracy on the val_data.
    It creates the eigenvectors database using the training samples.

    """
    train_x, train_y = train_data
    val_x, val_y     = val_data
    pass


def _get_image(image_name, channel_type='avg', rescale=False):
    """
    Returns the numpy image matrix corresponding to the image_name.

    """
    pass


def _fetch_image_data(annotation_file, label_map, channel_type='avg', rescale=False):
    x = []
    y = []
    with open(annotation_file) as fp:
        for line in fp:
            line = line.strip()
            image_name, label = line.split(",")
            image_matrix = _get_image(image_name, channel_type=channel_type, rescale=rescale)
            x.append(image_matrix)
            y.append(label_map[label])

    return (x, y)


def _get_label_map(annotation_file):
    unique_labels = set()
    with open(annotation_file) as fp:
        for line in fp:
            line = line.strip()
            label = line.split(",")[1]
            unique_labels.add(label)

    label_map = {}
    for label, i in enumerate(sorted(unique_labels)):
        label_map[label] = i

    return label_map


if __name__ == "__main__":
    args = get_args()

    label_map  = _get_label_map(args.train_data_file)
    train_data = _fetch_image_data(args.train_data_file, label_map, channel_type=args.channel_type, rescale=args.rescale)
    val_data   = _fetch_image_data(args.val_data_file, label_map, channel_type=args.channel_type, rescale=args.rescale)

    eigenvector_db = fisher_faces(train_data, val_data)
    if args.eigenvector_db_path:
        pickle.dump(eigenvector_db, open(args.eigenvector_db_path, "w"))
        print "The eigenvector_db has been written to %s" % args.eigenvector_db_path
