from visdom import Visdom

vis = Visdom()


def image(text, img):
    vis.image(img.transpose([2,0,1]),  win=text, opts={
        'caption': text
    })