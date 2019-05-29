import torch
import torch.nn as nn
import torchvision.models as models
from torch.autograd import Variable
import os
from PIL import Image
import torchvision.transforms.functional as TF
import h5py
import numpy as np

features_array = np.array([])

resnet152 = models.resnet152(pretrained=True)
# print(resnet152)
modules = list(resnet152.children())[:-2]
resnet152 = nn.Sequential(*modules)
for p in resnet152.parameters():
    p.requires_grad = False

# Get resnet features for random image_
images_path = 'D:\\Yulia\\frames\\2\\'
print(images_path)
for filename in os.listdir(images_path):
    if (filename.endswith(".jpg")):  # or .avi, .mpeg, whatever.
        img_name = os.path.join(images_path, filename)
        # print(img_name)
        image = Image.open(img_name)
        tensor_image = TF.to_tensor(image)
        img = torch.unsqueeze(tensor_image, 0)  # Add dimension 0 to tensor
        img_var = Variable(img)  # assign it to a variable
        features_var = resnet152(img_var)  # get the output from the last hidden layer of the pretrained resnet
        features = features_var.data  # get the tensor out of the variable
        # print(features.data.numpy())
        features_array = np.append(features_array, features.data.numpy())
        # features_array.append(np.array(features))
        # print(np.array(features))
    else:
        continue

print(features_array)

f = h5py.File("RESNET.hdf5", "w")
f.create_dataset('default', data=features_array)
f.close()

# to read dataset:
# hf = h5py.File('C:\\Users\\22649731\\PycharmProjects\\RESNET.hdf5', 'r')
# data = hf['default']
#
# print(data[:10])