"""Draw the two interleaved bidding schedules from a rotating 3D camera."""

from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 800, 480
BG, PANEL = "#101b2e", "#192a43"
INK, MUTED = "#f0f6ff", "#bacee7"
MINT, AMBER, BLUE = "#80e8cf", "#ffc385", "#8ca9cc"


def font(name, size):
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default(size=size)


def project(x,y,z,angle):
    side=x*cos(angle)-y*sin(angle)
    toward=x*sin(angle)+y*cos(angle)
    up=z*cos(.43)+toward*sin(.43)
    depth=toward*cos(.43)-z*sin(.43)
    zoom=11/(11-depth)
    return 399+side*100*zoom,242-up*77*zoom,depth


def draw_frame(angle, fonts):
    title, label, node, exponent, strong=fonts
    image=Image.new("RGB",(WIDTH,HEIGHT),BG)
    draw=ImageDraw.Draw(image)
    draw.text((28,22),"A fair bit, two bidding schedules",font=title,fill=INK)
    draw.rounded_rectangle((26,90,774,365),14,fill=PANEL)
    draw.text((45,103),"Seed 0",font=label,fill=MINT)
    draw.text((169,103),"Seed 1",font=label,fill=AMBER)
    draw.text((753,103),"Target just above a^5",font=label,fill=INK,anchor="ra")
    colored=[]
    for seed,y in enumerate((1.16,-1.16)):
        color=(MINT,AMBER)[seed]
        bids=list(range(seed,8,2))
        points=[]
        for idx in bids:
            x=(idx-3.5)*.69
            level=.20 if idx>=6 else 0
            point=project(x,y,level,angle)
            points.append(point)
            colored.append((idx,point,color))
        draw.line([p[:2] for p in points],width=5,fill=color)
    barrier=(5.45-3.5)*.69
    for j in range(7):
        v0=-1.45+j*.44
        draw.line([project(barrier,v0,.05,angle)[:2],
                   project(barrier,v0+.22,.05,angle)[:2]],width=3,fill=INK)
    for idx,(x,y,_) ,color in sorted(colored,key=lambda item:item[1][2]):
        radius=22 if idx>=6 else 17
        fill=color if idx>=6 else PANEL
        draw.ellipse((x-radius,y-radius,x+radius,y+radius),fill=fill,outline=color,width=3)
        text_color=BG if idx>=6 else INK
        draw.text((x-3,y),"a",font=node,fill=text_color,anchor="mm")
        draw.text((x+7,y-6),str(idx),font=exponent,fill=text_color,anchor="mm")
    draw.text((45,321),"Filled bids are the two stopping bids.",font=label,fill=MUTED)
    draw.text((30,387),"6305/1944",font=strong,fill=MINT)
    draw.text((292,393),"right-limit ratio at a^5",font=label,fill=INK)
    draw.text((30,442),"At later breakpoints the ratio approaches 27/8.",font=label,fill=INK)
    return image


def main():
    fonts=(font("Arial Bold.ttf",42),font("Arial.ttf",27),
           font("Arial Bold.ttf",22),font("Arial Bold.ttf",14),font("Arial Bold.ttf",40))
    frames=[draw_frame(.30*sin(tau*i/72)-.16,fonts) for i in range(72)]
    frames[0].save(Path(__file__).with_name("interleaved-bids.gif"),save_all=True,
                   append_images=frames[1:],duration=84,loop=0,optimize=False)


if __name__=="__main__":
    main()
