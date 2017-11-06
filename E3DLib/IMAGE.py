import pyscreenshot as ImageGrab
from PIL import Image


def AutoSave_Thumbnail():
    if __name__ == '__main__':
        img = ImageGrab.grab()
        basewidth = 512
        size = (512, 512)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS).convert('RGBA')
        eyecandy = Image.open('../bmp/HUD/SCRNBase.png').convert('RGBA')
        mask = Image.open('../bmp/HUD/SCRNAlpha.tga').convert('RGBA')
        if mask.mode in ('RGBA', 'LA') or (mask.mode == 'P' and 'transparency' in mask.info):
            mask = mask.convert('RGBA').split()[-1]
        eyecandy.paste(img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)), img)
        eyecandy.putalpha(mask)
        eyecandy.save('../bmp/HUD/overlays/Overlay35.tga')
