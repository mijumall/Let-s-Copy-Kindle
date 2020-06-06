import pyautogui as auto
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
from PyPDF2 import PdfFileMerger

x=1

title=input('Type the book\'s name: ')
pages=input('Type the amount of pages: ')
save_directry=input('Type the relative path of directry you want to save your book in: ')

pages=int(pages)

save_path='{}{}_page0{}.png'.format(save_directry,title,x)

print('I will wait for 10 secnds.')
time.sleep(10)


while x<=pages:
    save_path='{}{}_page0{}.png'.format(save_directry,title,x)

    auto.screenshot(save_path)
    auto.press('right')
    time.sleep(2)
    x+=1



x=1
while x<=pages:
    save_path='{}{}_page0{}.png'.format(save_directry,title,x)

    infile=save_path
    outfile=save_path

    img=Image.open(infile)
    width,height=img.size

    cropsize=(90,160,width-50,height-60)

    cropped=img.crop(cropsize)
    cropped.save(outfile)
    x+=1


x=1
while x<=pages:
    save_path='{}{}_page0{}.png'.format(save_directry,title,x)
    divided_save_path='{}divided_{}_page0{}-1.png'.format(save_directry,title,x)

    infile=save_path
    outfile=divided_save_path

    img=Image.open(infile)
    width,height=img.size

    cropsize=(0,0,width-550,height-0)

    cropped=img.crop(cropsize)
    cropped.save(outfile)


    divided_save_path='{}divided_{}_page0{}-2.png'.format(save_directry,title,x)
    
    infile=save_path
    outfile=divided_save_path

    img=Image.open(infile)
    width,height=img.size

    cropsize=(550,0,width-0,height-0)

    cropped=img.crop(cropsize)
    cropped.save(outfile)
    x+=1


pdf_files=[]

x=1
while x<=pages:
    divided_save_path='{}divided_{}_page0{}-1.png'.format(save_directry,title,x)
    im=Image.open(divided_save_path)
    if im.mode == 'RGBA':
        im = im.convert('RGB')
    new_divided_save_path ='{}new_divided_{}_page0{}-1.pdf'.format(save_directry,title,x)
    im.save(new_divided_save_path,'PDF',resolution=100.0)

    pdf_files.append(new_divided_save_path)

    divided_save_path='{}divided_{}_page0{}-2.png'.format(save_directry,title,x)
    im=Image.open(divided_save_path)
    if im.mode == 'RGBA':
        im = im.convert('RGB')
    new_divided_save_path ='{}new_divided_{}_page0{}-2.pdf'.format(save_directry,title,x)
    im.save(new_divided_save_path,'PDF',resolution=100.0)

    pdf_files.append(new_divided_save_path)
    
    x+=1



merger = PdfFileMerger()
for files in pdf_files:
    merger.append(files)

merger.write(save_directry+title+'.pdf')
merger.close()
