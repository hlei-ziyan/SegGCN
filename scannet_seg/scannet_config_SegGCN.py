import numpy as np

num_input = 8192
num_cls = 21

mlp = 64
num_sample = [2048, 768, 384, 128]
print(num_sample)
radius = [0.1, 0.2, 0.4, 0.8]
nn_uplimit = [64, 64, 64, 64]
channels = [64, 128, 256, 512]
num_blocks = [2,2,2,2]

weight_decay = None

kernel=[8,4,1]
binSize = np.prod(kernel)+1

normalize = True
pool_method = 'max'
unpool_method = 'weighted'
nnsearch = 'sphere'
sample = 'FPS' #{'FPS','IDS','random'}

with_bn = True
with_bias = False