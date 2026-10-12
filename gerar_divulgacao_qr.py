import sys
sys.path.insert(0, '.qr-deps')
import qrcode, cv2
from PIL import Image, ImageDraw, ImageFont

URL = 'https://maxuel82.github.io/FestaPrimaveraIBC2026/'
W, H = 1600, 2200
im = Image.new('RGB', (W, H), '#faf6ec')
d = ImageDraw.Draw(im)
green = '#285b40'
def font(size, bold=False):
    return ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf' if bold else 'C:/Windows/Fonts/segoeui.ttf', size)
def center(text, y, size, color=green, bold=False):
    f = font(size, bold)
    box = d.textbbox((0,0), text, font=f)
    d.text(((W-(box[2]-box[0]))/2,y), text, font=f, fill=color)
def flower(x,y,r,color):
    import math
    for i in range(8):
        a=i*math.pi/4
        px=x+math.cos(a)*r*.8; py=y+math.sin(a)*r*.8
        d.ellipse((px-r*.48,py-r*.48,px+r*.48,py+r*.48),fill=color)
    d.ellipse((x-r*.35,y-r*.35,x+r*.35,y+r*.35),fill='#efb843')

d.rounded_rectangle((70,70,W-70,H-70),radius=55,outline='#d7dfcd',width=4)
flower(150,175,58,'#e9a9bc'); flower(1450,175,58,'#ebbd66')
center('FESTA DA PRIMAVERA',140,52,bold=True)
center('Para sua comodidade,',255,48)
center('simule suas compras aqui!',325,78,bold=True)
center('Escolha com calma o que você e sua família',455,43)
center('querem aproveitar na festa.',515,43)

qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=20,border=4)
qr.add_data(URL); qr.make(fit=True)
qrim=qr.make_image(fill_color='black',back_color='white').convert('RGB')
qx=(W-qrim.width)//2; qy=635
d.rounded_rectangle((qx-25,qy-25,qx+qrim.width+25,qy+qrim.height+25),radius=30,fill='white',outline='#d7dfcd',width=3)
im.paste(qrim,(qx,qy))
center('Aponte a câmera do celular para o QR Code',qy+qrim.height+48,38,bold=True)
ty=qy+qrim.height+145
steps = [
    ('1', 'Simule suas compras', 'Escolha seus itens e confira o total.'),
    ('2', 'Vá ao caixa', 'Adquira esse valor em dinheirinho da festa.'),
    ('3', 'Aproveite as barracas!', 'Use o dinheirinho para comprar suas escolhas.'),
]
for i, (number, title, description) in enumerate(steps):
    y = ty - 15 + i * 115
    d.ellipse((170,y+5,240,y+75),fill=green)
    d.text((191,y+8),number,font=font(40,True),fill='white')
    d.text((270,y),title,font=font(43,True),fill=green)
    d.text((270,y+58),description,font=font(31),fill=green)
center('No caixa: dinheiro, cartão ou Pix.',ty+340,35)
d.line((250,ty+400,1350,ty+400),fill='#d7dfcd',width=3)
center('É uma simulação: não envia pedidos nem reserva produtos.',ty+425,28,color='#647167')
center('maxuel82.github.io/FestaPrimaveraIBC2026/',ty+470,30)
flower(150,H-170,52,'#ebbd66'); flower(1450,H-170,52,'#e9a9bc')
im.save('QRCodeFestaPrimaveraDivulgacao.png',dpi=(200,200))
im.save('QRCodeFestaPrimaveraDivulgacao.pdf','PDF',resolution=200)
decoded,_,_=cv2.QRCodeDetector().detectAndDecode(cv2.imread('QRCodeFestaPrimaveraDivulgacao.png'))
assert decoded==URL, 'Falha na validação do QR Code'
print('Arte PNG e PDF criados. QR Code validado:',decoded)
