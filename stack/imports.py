import os,pickle,random,re,shutil,sys,traceback,uuid,zlib

from collections.abc import Iterable
from configobj import ConfigObj
from contextlib import contextmanager
import datetime as dt
from datetime import datetime
from functools import partial, reduce
from pathlib import Path
import pathlib
from time import process_time
import warnings

import numpy as np
from fastcore.utils import L

import seaborn as sns
import matplotlib.pyplot as plt
import inflection

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.svm import SVC

from pickle import dump, load


# from labs.utilities.version_1.base import *
# from labs.utilities.version_1.types import *
