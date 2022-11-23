from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import os
def cracking():

    if os.path.exists('C:/23.11/Imgs'):
        directory = 'C:/23.11/Imgs'
    else:print('нет такой папки')

    files=os.listdir(directory)
    imges = list(filter(lambda x: x.endswith('.jpg'),files))
    clips = [ImageClip(m).set_duration(2) for m in imges]

    final_clip=concatenate_videoclips(clips, method='compose')
    final_clip.write_videofile('test.mp4' , fps=24)
    
def meretin(t,x,y,n):
    im = Image.new('RGB', (x,y), color=('#7B917B'))
    font = ImageFont.truetype(
        'C:/Windows/Fonts/times.ttf',
                          size=100)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (30,480),
        t,
        font=font,
        fill=('#1C0606')
        )
    #im.save('C:/Users/user/Desktop/Imgs/Image'+str(n)+'.jpg')
    if(n>9):
        im.save('C:/23.11/Imgs/Image'+str(n)+'.jpg')
    else:
        im.save('C:/23.11/Imgs/Image0'+str(n)+'.jpg')

t=['Однажды',
  'Жила была\n толстая лягушка',
  'её все обзывали\n в школе',
  'лягуха-толстуха \n говорили они',
  'и тога она решила....',
  'покончить жизнь\n самоубийством',
  'теплым осенним\n вечером',
  'она пришла на \nкоммунальный мост',
  'провожала последний\n свой закат',
  'и вот она уже\n собираетя прыгать',
  'откуда ни возьмись',
  'появился иваныч',
  'включил данзакудуро ',
  'и они начали\n танцевать',
  'лягушка выроса \n разбогатела и всё']

for i in range(15):
    meretin(t[i],1000,1000,i)
cracking()

    
