import torch.nn



class CIFAR10Classify01(torch.nn.Module):
    def __init__(self):
        super(CIFAR10Classify01, self).__init__()
        self.model1 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, padding=2, ),
            torch.nn.MaxPool2d(kernel_size=2),
            torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, padding=2, ),
            torch.nn.MaxPool2d(kernel_size=2),
            torch.nn.BatchNorm2d(32),
            torch.nn.Sigmoid(),
            torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, padding=2, ),
            torch.nn.MaxPool2d(2),
            torch.nn.Flatten(),
            # 第一个linear的in_features可以由print(x.shape)得到
            torch.nn.Linear(in_features=1024, out_features=64),
            torch.nn.Linear(in_features=64, out_features=10)
            # 分类问题的最终out_features和类数相同
        )

    def forward(self, x):
        x = self.model1(x)
        return x


if __name__ == "__main__":
    import torch.utils.tensorboard
    model = CIFAR10Classify01()
    test_tensor = torch.ones(64, 3, 32, 32)
    # 用形状和实际数据集相同的tenser测试网络是否可用
    output = model(test_tensor)
    print(output.shape)
    # output.shape[0]==batch_size, output.shape[1]==分类数量

    writer = torch.utils.tensorboard.SummaryWriter("logs_import")
    writer.add_graph(model, test_tensor)
    writer.close()

    import os
    os.system("tensorboard --logdir=logs_import --port=998")
