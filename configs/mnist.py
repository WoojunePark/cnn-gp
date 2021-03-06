import torchvision

from cnn_gp import Conv2d, ReLU, Sequential, resnet_block

train_range = range(50000)
validation_range = range(50000, 60000)
test_range = range(60000, 70000)

dataset_name = "MNIST"
model_name = "ResNet"
dataset = torchvision.datasets.MNIST
transforms = []
epochs = 0
in_channels = 1
out_channels = 10
initial_model = Sequential(
    Conv2d(kernel_size=3),

    # Big resnet block #1
    resnet_block(stride=1, projection_shortcut=True,  multiplier=1),
    resnet_block(stride=1, projection_shortcut=False, multiplier=1),
    resnet_block(stride=1, projection_shortcut=False, multiplier=1),
    resnet_block(stride=1, projection_shortcut=False, multiplier=1),
    resnet_block(stride=1, projection_shortcut=False, multiplier=1),

    # Big resnet block #2
    resnet_block(stride=2, projection_shortcut=True,  multiplier=2),
    resnet_block(stride=1, projection_shortcut=False, multiplier=2),
    resnet_block(stride=1, projection_shortcut=False, multiplier=2),
    resnet_block(stride=1, projection_shortcut=False, multiplier=2),
    resnet_block(stride=1, projection_shortcut=False, multiplier=2),

    # Big resnet block #3
    resnet_block(stride=2, projection_shortcut=True,  multiplier=4),
    resnet_block(stride=1, projection_shortcut=False, multiplier=4),
    resnet_block(stride=1, projection_shortcut=False, multiplier=4),
    resnet_block(stride=1, projection_shortcut=False, multiplier=4),
    resnet_block(stride=1, projection_shortcut=False, multiplier=4),

    # No nonlinearity here, the next Conv2d substitutes the average pooling
    Conv2d(kernel_size=7, padding=0, in_channel_multiplier=4,
           out_channel_multiplier=4),
    ReLU(),
    Conv2d(kernel_size=1, padding=0, in_channel_multiplier=4),
)
