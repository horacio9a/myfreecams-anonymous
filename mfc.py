# MFC FFMPEG FLV Anonymous Player and Recorder v.1.0.4 by Horacio for Python 2.7.13

import os,sys,urllib,re,json,time,datetime,random,requests,command,websocket
from websocket import create_connection
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.cfg')

init()
print
print(colored(" => START <=", "yellow", "on_blue"))
print

vs_str = {}
vs_str[0] = "PUBLIC"
vs_str[2] = "AWAY"
vs_str[12] = "PVT"
vs_str[13] = "GROUP"
vs_str[90] = "CAM-OFF"
vs_str[127] = "OFFLINE"

def fc_decode_json(m):
        try:
           m = m.replace('\r', '\\r').replace('\n', '\\n')
           return json.loads(m[m.find("{"):].decode("utf-8","ignore"))
        except:
           return json.loads("{\"lv\":0}")

def read_model_data(m):
        global server
        global cid
        global uid
        global vs
        msg = fc_decode_json(m)
        try:
           sid = msg['sid']
           level = msg['lv']
        except:
           print(colored(" => Error reply ... check your entry <=", "yellow", "on_red"))
           print
           time.sleep(1)    # pause 1 second
           print(colored(" => END <=", "yellow","on_blue"))
           sys.exit()
        vs = msg['vs']
        if vs == 127:
           print(colored(" => Model is OFFLINE! <=", "yellow", "on_red"))
           print
           return
        usr = msg['nm']
        uid = msg['uid']
        cid = msg['uid'] + 100000000
        camservinfo = msg['m']
        flags = camservinfo['flags']
        u_info = msg['u']
        try:
           camserver = u_info['camserv']
           if camserver >= 840:
              server = camserver - 500
           if camserver < 839:
              server = 0
        except KeyError:
           server = 0
           print(colored(" => Something is wrong! <=", "yellow", "on_red"))
           print
        try:
           if flags == 15400:
              buf = '(TRUEPVT)'
           else:
              buf = "("+vs_str[vs]+")"
        except KeyError:
              pass
        print (colored(" => {} * SERVER: {} * FLAGS: {} * SID: {} * UID: {} <=", "yellow", "on_blue")).format(buf,server,flags,sid,uid)
        print
        print (colored(" => (MODEL DATA) => {} <=", "white", "on_blue")).format(msg)
        print

if __name__ == "__main__":
        if len(sys.argv) > 1:
           camgirl = sys.argv[1]
        else:
                while True:
                     try:
                         modellist = open(config.get('files', 'model_list'),'r')
                         for (num,value) in enumerate(modellist):
                            print " =>",(num+1),value[:-1]
                         print
                         cgn = int(raw_input(colored(" => Select MFC Model => ", "yellow", "on_blue")))
                         print
                         break
                     except ValueError:
                         print
                         print(colored(" => Input must be a number <=", "yellow", "on_red"))
                         print
                camgirl = open(config.get('files', 'model_list'), 'r').readlines()[cgn-1][:-1]
                print (colored(" => Selected MFC Model => {} <=", "yellow", "on_blue")).format(camgirl)
                print
        try:
                xchat = [22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,90,92,93,94,95]
                host = "ws://xchat"+str(random.choice(xchat)) + ".myfreecams.com:8080/fcsl"
                print (colored(" => Connecting to MFC Server => {} <=", "white", "on_blue")).format(host)
                print
                ws = create_connection(host)
                ws.send("hello fcserver\n\0")
                ws.send("1 0 0 20071025 0 guest:guest\n\0")
        except:
                print(colored(" => We're fucked <=", "yellow", "on_red"))
                sys.exit()
        rembuf = ""
        quitting = 0
        while quitting == 0:
                sock_buf =  ws.recv()
                sock_buf = rembuf+sock_buf
                rembuf = ""
                while True:
                   hdr = re.search (r"(\w+) (\w+) (\w+) (\w+) (\w+)", sock_buf)
                   if bool(hdr) == 0:
                      break
                   fc = hdr.group(1)
                   mlen = int(fc[0:4])
                   fc_type = int(fc[4:])
                   msg = sock_buf[4:4+mlen]
                   if len(msg) < mlen:
                      rembuf = ''.join(sock_buf)
                      break
                   msg = urllib.unquote(msg)
                   if fc_type == 1:
                      ws.send("10 0 0 20 0 %s\n\0" % camgirl)
                   elif fc_type == 10:
                      read_model_data(msg)
                      quitting = 1
                   sock_buf = sock_buf[4+mlen:]
                   if len(sock_buf) == 0:
                      break
        ws.close()

        if vs == 0:
         if server != 0:
           while True:
             try:
                mode = int(raw_input(colored(" => Select mode (1) REC or (0) PLAY => ", "yellow", "on_blue")))
                break
             except ValueError:
                print(colored("\n => Input must be a number <=", "yellow", "on_red"))
           if mode == 0:
                mod = 'PLAY'
           if mode == 1:
                mod = 'REC'
           else:
                mod = 'PLAY'

           if mod == 'PLAY':
                url = "http://video"+str(server)+".myfreecams.com:1935/NxServer/ngrp:mfc_"+str(cid)+".f4v_mobile/playlist.m3u8"
                timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
                filename = camgirl + "_MFC_" + timestamp + ".flv"
                print
                print (colored(" => Start ffplay => PLAY => {} <=", "yellow", "on_magenta")).format(filename)
                command = ('start ffplay -i {} -infbuf -autoexit -x 640 -y 480 -window_title "{} * {}"'.format(url,filename,cgn))
                os.system(command)
                print
                time.sleep(1)    # pause 1 second
                print(colored(" => END <=", "yellow","on_blue"))
                sys.exit()

           if mod == 'REC':
                url = "http://video"+str(server)+".myfreecams.com:1935/NxServer/ngrp:mfc_"+str(cid)+".f4v_mobile/playlist.m3u8"
                timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
                path = config.get('folders', 'output_folder')
                filename = camgirl + "_MFC_" + timestamp + ".flv"
                fn = path + filename
                print
                print (colored(" => Start ffplay => PLAY => {} <=", "white", "on_magenta")).format(filename)
                command = ('start ffplay -i {} -infbuf -autoexit -x 640 -y 480 -window_title "{} * {}"'.format(url,fn,cgn))
                os.system(command)
                print
                print (colored(" => Start ffmpeg => RECORD => {} <=", "yellow", "on_red")).format(filename)
                command = ('start ffmpeg -i {} -c:v copy -c:a aac -b:a 160k {}'.format(url,fn))
                os.system(command)
                print
                time.sleep(1)    # pause 1 second
                print(colored(" => END <=", "yellow","on_blue"))
                sys.exit()

         else:
                print(colored(" => 'NO MOBILE FEED' is not supported! <=", "yellow", "on_red"))
                print
                time.sleep(1)    # pause 1 second
                print(colored(" => END <=", "yellow","on_blue"))
                sys.exit()
        else:
                print(colored(" => This video stream can't be recorded! <=", "yellow", "on_red"))
                print
                time.sleep(1)    # pause 1 second
                print(colored(" => END <=", "yellow","on_blue"))
                sys.exit()
