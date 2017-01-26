from sense_hat import SenseHat
import time
import os
from evdev import InputDevice, ecodes,list_devices
from select import select
sense=SenseHat()

devices=[InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name== "Raspberry Pi Sense HAT Joystick":
        js=dev



p=(204,0,204) #pink
g=(0,102,102) #dark greed
w=(200,200,200) #white
y=(204,204,0) #yellow
e=(0,0,0) #empty
b=(0,0,200)
r=(200,0,0)

wash1= [
    e,b,e,e,b,e,e,b,
    p,e,e,e,e,e,e,e,
    e,p,b,e,p,b,p,e,
    e,p,g,g,p,y,y,e,
    e,g,g,g,y,w,y,g,
    e,g,g,g,g,y,y,e,
    e,g,e,g,e,g,e,e,
    e,e,e,e,e,e,e,e
       ]

wash2= [
    e,b,e,e,b,e,e,b,
    p,e,e,e,e,e,e,e,
    e,p,b,e,p,b,p,e,
    e,p,g,g,p,y,y,e,
    b,g,g,b,y,w,b,g,
    e,g,g,g,g,y,y,e,
    e,b,e,g,b,g,e,b,
    e,e,e,e,e,e,e,e
       ]

wash3= [
    e,e,e,e,e,e,e,e,
    p,e,e,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,e,
    e,g,g,g,y,w,y,g,
    b,g,g,b,g,y,b,e,
    e,g,e,g,e,g,e,e,
    e,b,e,e,b,e,e,e
       ]

play1= [
    e,e,e,e,e,e,e,e,
    e,e,r,e,e,e,e,e,
    e,e,e,p,e,e,e,e,
    p,e,e,y,y,e,e,e,
    e,g,g,g,e,e,e,e,
    e,g,e,g,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

play2= [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,r,e,e,
    e,e,e,p,e,e,e,e,
    p,e,e,y,y,e,e,e,
    e,g,g,g,e,e,e,e,
    e,g,e,g,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

play3= [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,r,
    e,e,e,e,p,e,y,e,
    e,e,e,e,e,y,e,e,
    e,e,e,p,g,g,e,e,
    e,e,e,g,e,g,e,e,
    e,e,e,g,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

love1= [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

love2= [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,r,r,r,r,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

love3= [
    e,e,e,e,e,e,e,e,
    e,r,r,e,e,r,r,e,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    e,r,r,r,r,r,r,e,
    e,e,r,r,r,r,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

dead1= [
    e,p,e,e,e,e,p,e,
    p,p,r,r,r,r,p,p,
    e,r,r,r,r,r,r,e,
    e,r,w,r,r,w,r,e,
    e,e,r,r,r,r,e,e,
    e,e,r,r,r,r,e,e,
    p,p,r,r,r,r,p,p,
    e,p,e,e,e,e,p,e,
    ]

dead2= [
    e,r,e,e,e,e,r,e,
    r,r,p,p,p,p,r,r,
    e,p,p,p,p,p,p,e,
    r,p,w,p,p,w,p,e,
    e,e,p,p,p,p,e,e,
    e,e,p,p,p,p,e,e,
    r,r,p,p,p,p,r,r,
    e,r,e,e,e,e,r,e,
    ]

pet1= [
    e,e,e,e,e,e,e,e,
    p,e,e,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,e,
    e,g,g,g,y,w,y,g,
    e,g,g,g,g,y,y,e,
    e,g,e,g,e,g,e,e,
    e,e,e,e,e,e,e,e
       ]

pet2= [
    e,e,e,e,e,e,e,e,
    e,e,p,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,e,
    e,g,g,g,y,w,y,g,
    e,g,g,g,g,y,y,e,
    e,e,g,e,g,e,e,e,
    e,e,e,e,e,e,e,e
    ]

feed1= [
    e,e,e,e,e,e,e,e,
    p,e,e,p,e,e,e,e,
    p,y,y,y,e,e,e,e,
    y,y,w,y,e,e,e,g,
    y,y,y,y,y,g,e,e,
    y,y,y,e,e,e,e,e,
    y,y,y,y,y,e,e,e,
    e,e,e,e,e,e,e,e
    ]

feed2= [
    e,e,e,e,e,e,e,e,
    p,e,e,p,e,e,e,e,
    p,y,y,y,e,e,e,e,
    y,y,w,y,e,e,e,e,
    y,y,y,y,y,g,e,e,
    y,y,y,e,e,e,g,e,
    y,y,y,y,y,e,e,e,
    e,e,e,e,e,e,e,e
    ]

feed3= [
    e,e,e,e,e,e,e,e,
    p,e,e,p,e,e,e,e,
    p,y,y,y,e,e,e,e,
    y,y,w,y,e,e,e,e,
    y,y,y,y,y,g,e,e,
    y,y,y,g,e,e,e,e,
    y,y,y,y,y,e,e,e,
    e,e,e,e,e,e,e,e
    ]

feed4= [
    e,e,e,e,e,e,e,e,
    p,e,e,p,e,e,e,e,
    p,y,y,y,e,e,e,e,
    y,y,w,y,e,e,e,e,
    y,y,y,y,y,g,e,e,
    y,y,y,y,y,e,e,e,
    y,y,y,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

feed5= [
    e,e,e,e,e,e,e,e,
    p,e,e,p,e,e,e,e,
    p,y,y,y,e,e,e,e,
    y,y,w,y,e,e,e,e,
    y,y,y,y,y,g,e,e,
    y,y,y,y,e,e,e,e,
    y,y,y,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]
while 1==1:
    hungerzahler=0
    hunger=0
    hungerprint="0"
    
    funzahler=0
    fun=100
    funprint="100"

    lovezahler=0
    love=100
    loveprint="100" 
    
    dreckzahler=0
    dreck=0
    dreckprint="0"
  
    pic=1
    alive=1
    deathcause="none"
    while alive==1:
        r, w, x = select([dev.fd], [], [], 0.01)
        for fd in r:
            for event in dev.read():
                if event.type == ecodes.EV_KEY and event.value ==1:
                    if event.code == ecodes.KEY_ENTER:
                        sense.show_message("HNGR")
                        sense.show_message(hungerprint)
                        sense.show_message("DRCK")
                        sense.show_message(dreckprint)
                        sense.show_message("FUN")
                        sense.show_message(funprint)
                        sense.show_message("LOVE")
                        sense.show_message(loveprint)
                        
                        r, w, x = select([dev.fd], [], [], 0.01)
                        for fd in r:
                            for event in dev.read():
                                if event.type == ecodes.EV_KEY and event.value ==1:
                                    if event.code == ecodes.KEY_UP:
                                        r, w, x = select([dev.fd], [], [], 0.01)
                                        for fd in r:
                                            for event in dev.read():
                                                if event.type == ecodes.EV_KEY and event.value ==1:
                                                    if event.code == ecodes.KEY_LEFT:
                                                        r, w, x = select([dev.fd], [], [], 0.01)
                                                        for fd in r:
                                                            for event in dev.read():
                                                                if event.type == ecodes.EV_KEY and event.value ==1:
                                                                    if event.code == ecodes.KEY_DOWN:
                                                                        r, w, x = select([dev.fd], [], [], 0.01)
                                                                        for fd in r:
                                                                            for event in dev.read():
                                                                                if event.type == ecodes.EV_KEY and event.value ==1:
                                                                                    if event.code == ecodes.KEY_RIGHT:
                                                                                        r, w, x = select([dev.fd], [], [], 0.01)
                                                                                        for fd in r:
                                                                                            for event in dev.read():
                                                                                                if event.type == ecodes.EV_KEY and event.value ==1:
                                                                                                    if event.code == ecodes.KEY_ENTER:
                                                                                                        os.system("sudo shutdown -h 0")
                       




                    elif event.code == ecodes.KEY_DOWN:
                        sense.set_pixels(feed1)
                        time.sleep(0.5)
                        sense.set_pixels(feed2)
                        time.sleep(0.5)
                        sense.set_pixels(feed3)
                        time.sleep(0.5)
                        sense.set_pixels(feed4)
                        time.sleep(0.5)
                        sense.set_pixels(feed5)
                        time.sleep(0.5)
                        sense.set_pixels(feed4)
                        time.sleep(0.5)
                    
                        if hunger >= 30:
                            hunger=hunger-30
                        if hunger < 30:
                            hunger=0
                        hungerprint="%s" % (hunger)
                        hungerzahler=0
                    elif event.code == ecodes.KEY_UP:
                        sense.set_pixels(love1)
                        time.sleep(0.5)
                        sense.set_pixels(love2)
                        time.sleep(0.5)
                        sense.set_pixels(love3)
                        time.sleep(0.5)
                        if love<=75:
                            love= love+25
                        if love>75:
                            love=100
                        loveprint="%s" % (love)
                        lovezahler=0
                    elif event.code == ecodes.KEY_RIGHT:
                        sense.set_pixels(play1)
                        time.sleep(0.5)
                        sense.set_pixels(play2)
                        time.sleep(0.5)
                        sense.set_pixels(play3)
                        time.sleep(0.7)
                        if fun<= 80:
                            fun=fun+20
                        if fun >  80:
                            fun=100
                        funprint="%s" % (fun)
                        funzahler=0
                    elif event.code == ecodes.KEY_LEFT:
                        sense.set_pixels(wash1)
                        time.sleep(0.5)
                        sense.set_pixels(wash2)
                        time.sleep(0.5)
                        sense.set_pixels(wash3)
                        time.sleep(0.7)
                        if dreck>=30:
                            dreck=dreck-30
                        if dreck<30:
                            dreck=0
                        dreckprint="%s" % (dreck)
                        dreckzahler=0
                                                
                    
        hungerzahler= hungerzahler+1
        lovezahler= lovezahler+1
        funzahler= funzahler+1
        dreckzahler= dreckzahler+1
 
        if funzahler == 300:
            fun= fun-1
            funzahler=0
            funprint="%s" % (fun)

        if hungerzahler == 100:
            hunger = hunger+1
            hungerzahler=0
            hungerprint="%s" % (hunger)

        if lovezahler == 400:
            love= love-1
            lovezahler=0
            loveprint="%s" % (love)
        
        if dreckzahler == 130:
            dreck=dreck+1
            dreckzahler=0
            dreckprint="%s" % (dreck)
        
        if hunger==100:
            alive=0
            deathcause="Hunger"

        if love == 0:
            alive = 0
            deathcause= "Liebe"
        
        if fun == 0:
            alive = 0
            deathcause= "Fun"
     
        if dreck == 100:
            alive=0
            deathcause= "Dreck"

        if pic == 1:
            sense.set_pixels(pet1)
            time.sleep(0.5)
            pic = 2
        
        elif pic == 2:
             sense.set_pixels(pet2)
             time.sleep(0.5)
             pic=1

    while alive==0:

        if pic == 1:
            sense.set_pixels(dead1)
            time.sleep(0.5)
            pic=2

        if pic == 2:
            sense.set_pixels(dead2)
            time.sleep(0.5)
            pic=1

        r, w, x = select([dev.fd], [], [], 0.01)
        for fd in r:
             for event in dev.read():
                 if event.type == ecodes.EV_KEY and event.value ==1:
                     if event.code == ecodes.KEY_ENTER:
                         alive=1
                         sense.show_message("Gestorben wegen")
                         sense.show_message(deathcause)
