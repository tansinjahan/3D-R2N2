
import os
import sys
if (sys.version_info < (3, 0)):
    raise Exception("Please follow the installation instruction on 'https://github.com/chrischoy/3D-R2N2'")

import shutil
import numpy as np
from subprocess import call
import subprocess
import time
import tensorflow as tf

#from PIL import Image
from models import load_model
from lib.config import cfg, cfg_from_list
from lib.solver import Solver
from lib.voxel import voxel2obj

def interpolationBetnLatentSpace(z1, z2):
    mx = 100
    mn = 0
    for t in range(mn,mx,0.1):
        new_z = (1 - t) * z1

    return new_z

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a,b)
writer = tf.summary.FileWriter('./graphs',tf.get_default_graph())

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    print(sess.run(x))

writer.close()