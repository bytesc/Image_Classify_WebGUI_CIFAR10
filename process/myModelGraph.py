import torch.nn
import torchvision.datasets
import torchvision.transforms
import torch.utils.tensorboard
from torch.utils.data import DataLoader

import sys
sys.path.append('..')
from data.myModel_import2 import *


# 用ones测试模型是否可用
model2 = CIFAR10Classify01()
print(model2)
iinput = torch.ones((64, 3, 32, 32))
output = model2(iinput)
print(output.shape)


writer = torch.utils.tensorboard.SummaryWriter("logs")
writer.add_graph(model2, iinput)
writer.close()

