import PIL.Image
import torchvision.transforms
import torch.nn

import pywebio
from io import BytesIO

from data.myModel_import2 import *


@pywebio.config(title="卷积神经网络Demo", description="基于CIFAR10数据集的图像分类")
def page1():
    train_set_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    graph_img = PIL.Image.open("./data/net_graph.png")

    def show_info():
        pywebio.output.put_markdown("# 基于CIFAR10数据集的图像分类")
        pywebio.output.put_table([
            [pywebio.output.span('数据集', row=1), pywebio.output.span('支持类别', col=2)],
            ['CIFAR10', train_set_classes]
        ])
        pywebio.output.put_text("contact:21010078@mail.ecust.edu.cn")

    show_net=[pywebio.output.put_text('net'),
              pywebio.output.put_image(graph_img)]
    def popup_window():
        pywebio.output.popup(title='网络结构', content=show_net)


    show_info()
    pywebio.output.put_buttons(['点击查看网络结构'], [lambda: popup_window()])
    # pywebio.output.put_buttons(['点击查看网络结构'], [popup_window])
    pywebio.output.put_html("</br></br></br>")
    inpic = pywebio.input.file_upload(label="上传图片 please upload a image")



    # img_path = "./pic2/102.png"
    img = PIL.Image.open(BytesIO(inpic['content']))
    img = img.convert("RGB")
    # print(img.size)
    transform01 = torchvision.transforms.Compose([
        torchvision.transforms.Resize((32, 32)),
        torchvision.transforms.ToTensor()
    ])
    img = transform01(img)
    img = torch.reshape(img, (1, 3, 32, 32))
    # print(img.shape)



    model = torch.load("data/myModel_46.pth", map_location=torch.device('cpu'))
    # print(model)

    # model.eval()
    with torch.no_grad():
        output = model(img)
    # print(output)
    # print(output.argmax(1))
    # print(train_set.classes[output.argmax(1).item()])
    # pywebio.output.put_text(train_set.classes[output.argmax(1).item()])
    pywebio.output.popup(title='识别结果',
                         content=[pywebio.output.put_markdown("人工智障表示，这是：\n # " + train_set_classes[output.argmax(1).item()])])


    img = torch.reshape(img, (3, 32, 32))
    transform2 = torchvision.transforms.Compose([
        torchvision.transforms.Resize((160, 160)),
        torchvision.transforms.ToPILImage()
    ])
    img = transform2(img)

    img_bytes = BytesIO()
    img.save(img_bytes, format="JPEG")
    img = img_bytes.getvalue()
    pywebio.output.put_image(img, height="512", width="512")

    pywebio.output.put_image(inpic['content'], height="512", width="512")


if __name__ == "__main__":
    # page1()
    pywebio.start_server(
        applications=[page1, ],
        debug=False,
        auto_open_webbrowser=False,
        remote_access=False,
        port=6006
    )

