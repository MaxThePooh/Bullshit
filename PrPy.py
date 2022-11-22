from PIL import Image, ImageDraw, ImageFont
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
    im.save('C:/Users/user/Desktop/Imgs/Image'+str(n)+'.jpg')

t=['Однажды',
  'Жила была\n толстая лягушка',
  'её все обзывали\n в школе',
  'лягуха-толстуха \n говорили они',
  'и тога она решила....',
  'покончить жизнь\n смоубийством',
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
