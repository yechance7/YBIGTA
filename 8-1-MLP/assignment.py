import numpytorch as npt
from numpytorch import Tensor, nn
from numpytorch import reshape


"""
Example model.
If you want to see how main.py works (before you finish the assignment),
try running it through this model.

class MNISTClassificationModel(nn.Module):
    def __init__(self) -> None:
        self.seq = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 10, bias=False)
        )

    def forward(self, x: Tensor) -> Tensor:
        x = reshape(x, (x.shape[0], -1))
        logits = self.seq(x)
        return logits

Your model!

class Conv2d(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int) -> None:
        pass

    def forward(self, x: Tensor) -> Tensor:
        pass


class MaxPool2d(nn.Module):
    def __init__(self, kernel_size: int, stride: int) -> None:
        pass

    def forward(self, x: Tensor):
        pass


class MNISTClassificationModel(nn.Module):
    def __init__(self) -> None:
        pass

    def forward(self, x: Tensor) -> Tensor:
        # Input shape: (batch_size, 1, 28, 28)
        # Return shape: (batch_size, 10)
        pass
"""


import numpy as np

class Conv2d(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int, stride: int = 1, padding: int = 0) -> None:
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.weight = Tensor(np.random.randn(out_channels, in_channels, kernel_size, kernel_size) * np.sqrt(1. / in_channels))
        self.bias = Tensor(np.zeros(out_channels))

    def forward(self, x: Tensor) -> Tensor:
        batch_size, _, height, width = x.shape
        out_height = (height + 2 * self.padding - self.kernel_size) // self.stride + 1
        out_width = (width + 2 * self.padding - self.kernel_size) // self.stride + 1
        
        x_padded = np.pad(x.arr, ((0,), (0,), (self.padding,), (self.padding,)), mode='constant')
        
        output = np.zeros((batch_size, self.out_channels, out_height, out_width))

        for i in range(out_height):
            for j in range(out_width):
                region = x_padded[:, :, i*self.stride:i*self.stride+self.kernel_size, j*self.stride:j*self.stride+self.kernel_size]
                output[:, :, i, j] = np.tensordot(region, self.weight.arr, axes=([1, 2, 3], [1, 2, 3])) + self.bias.arr

        return Tensor(output)

class MaxPool2d(nn.Module):
    def __init__(self, kernel_size: int, stride: int) -> None:
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride

    def forward(self, x: Tensor) -> Tensor:
        batch_size, channels, height, width = x.shape
        out_height = (height - self.kernel_size) // self.stride + 1
        out_width = (width - self.kernel_size) // self.stride + 1

        output = np.zeros((batch_size, channels, out_height, out_width))

        for i in range(out_height):
            for j in range(out_width):
                region = x.arr[:, :, i*self.stride:i*self.stride+self.kernel_size, j*self.stride:j*self.stride+self.kernel_size]
                output[:, :, i, j] = np.max(region, axis=(2, 3))

        return Tensor(output)


class MNISTClassificationModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = Conv2d(1, 16, 3)  # 28x28 -> 26x26
        self.pool = MaxPool2d(2, 2)    # 26x26 -> 13x13
        self.conv2 = Conv2d(16, 32, 3) # 13x13 -> 11x11
        self.fc1 = nn.Linear(32 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x: Tensor) -> Tensor:
        x = self.pool(self.conv1(x))
        x = self.pool(self.conv2(x))
        
        # Convert Tensor to NumPy array to reshape it
        x_np = x.arr
        x_np = x_np.reshape(-1, 32 * 5 * 5)  # Reshape using NumPy

        # Convert NumPy array back to Tensor
        x = Tensor(x_np)
        
        x = nn.relu(self.fc1(x))
        x = nn.relu(self.fc2(x))
        x = self.fc3(x)
        return x
