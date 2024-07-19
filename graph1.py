from PIL import Image,ImageDraw,ImageFont
from math import *
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import sounddevice as sd
import soundfile as sf
import soundcard as sc
# import parser

def run(func):
    size = 600

    image = Image.new("RGB", (size,size), "white")
    draw = ImageDraw.Draw(image)

    xmin = -10
    ymin = -10
    xmax = 10
    ymax = 10

    code = func

    xrange = xmax - xmin
    yrange = ymax - ymin

    step_s = xrange/20000

    cartx = 20
    carty = 20

    def act_to_im(x,y):
        i = size/xrange
        j = size/yrange
        ax = (x*i)+size//2
        ay = size//2-(y*j)
        return ax,ay

    for i in range(cartx):
        x = (i/cartx)*size
        clr = "#CCCCFF"
        if i == 10:
            clr = "#FF9999"
        draw.line([(x,0),(x,size)],fill=clr,width = 1)

    for i in range(carty):
        x = (i/carty)*size
        clr = "#CCCCFF"
        if i == 10:
            clr = "#FF9999"
        draw.line([(0,x),(size,x)],fill=clr,width = 1)

    outputs = []
    y_vals = []

    print(int((xrange*(1/step_s))//1))
    for i in range(int((xrange*(1/step_s))//1)):
        i = i*step_s
        acx = i-(xrange//2)
        x = acx
        try:
            acy = eval(code)
        except:
            pass
        else:
            px,py = act_to_im(acx,acy)
            y_vals.append(acy)
            outputs.append((px,py))

    draw.line(outputs,fill = 'red',width = 1)

    image.save("static/graph.png")

    symin = min(y_vals)
    symax = max(y_vals)
    srange = symin - symax

    s_array = np.array([])

    freq = -1

    for i in range(len(y_vals)):
        if srange != 0:
            sound_val = freq*(y_vals[i]/srange)
        else:
            sound_val = 1
        sound_val = int(sound_val)
        s_array = np.append(s_array,sound_val)
        if i!=len(y_vals)-1:
            k = y_vals[i+1] - y_vals[i]
            if srange != 0:
                s_array = np.append(s_array,[freq*((y_vals[i]+(k*0.1))/srange),
                                     freq*((y_vals[i]+(k*0.2))/srange),
                                     freq*((y_vals[i]+(k*0.3))/srange),
                                     freq*((y_vals[i]+(k*0.4))/srange),
                                     freq*((y_vals[i]+(k*0.5))/srange),
                                     freq*((y_vals[i]+(k*0.6))/srange),
                                     freq*((y_vals[i]+(k*0.7))/srange),
                                     freq*((y_vals[i]+(k*0.8))/srange),
                                     freq*((y_vals[i]+(k*0.9))/srange)])
                                     
    print(np.max(s_array),np.min(s_array))
    print(s_array)

    fs = 24100
    record_duration = 15

    sd.play(s_array,fs)
    sd.wait()

# func = input()
# run("2*x+8")