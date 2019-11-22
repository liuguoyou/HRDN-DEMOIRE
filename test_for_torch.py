import torch
import torch.nn as nn
import numpy as np

class scale_layer(nn.Module):
    def __init__(self):
        super(scale_layer, self).__init__()
        alpha = torch.randn((3, 3), requires_grad=True)
        self.scale_alpha = torch.nn.Parameter(alpha)
        self.register_parameter("scale_alpha", self.scale_alpha)

    def forward(self, x):
        return x


# @torch.no_grad()

if __name__ == '__main__':

    a = np.array([[[[1, 10, 2, 20],
                  [1, 1, 2, 2],
                  [3, 30, 4, 40],
                  [3, 3, 4, 4]],

                [[21, 10, 22, 20],
                 [21, 21, 22, 22],
                 [23, 30, 24, 40],
                 [23, 23, 24, 24]],

                [[31, 10, 32, 20],
                 [31, 31, 32, 32],
                 [33, 30, 34, 40],
                 [33, 33, 34, 34]]],
                  [[[1, 10, 2, 20],
                    [1, 1, 2, 2],
                    [3, 30, 4, 40],
                    [3, 3, 4, 4]],

                   [[21, 10, 22, 20],
                    [21, 21, 22, 22],
                    [23, 30, 24, 40],
                    [23, 23, 24, 24]],

                   [[31, 10, 32, 20],
                    [31, 31, 32, 32],
                    [33, 30, 34, 40],
                    [33, 33, 34, 34]]]],
                  dtype='float32')

    a = torch.from_numpy(a)
    a = a.reshape(2, 3, 4, 4)

    # Unshuffle = pixel_unshuffle(a)
    # print(Unshuffle.size())
