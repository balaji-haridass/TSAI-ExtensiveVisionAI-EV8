# -*- coding: utf-8 -*-

from enum import Enum

class NormType(Enum):  
  BATCH_NORM = 1
  LAYER_NORM = 2
  GROUP_NORM = 3

class RegularizerType(Enum):  
  NONE = 1
  L1 = 2
  L2 = 3