# MFC Anonymous All Modes Recorder v.1.0.7 by horacio9a for Python 2.7.14

import sys,os,urllib,re,json,time,datetime,random,requests,command,websocket
reload(sys)
sys.setdefaultencoding('utf-8')
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
vs_str[12] = "PRIVATE"
vs_str[13] = "GROUP"
vs_str[90] = "CAM-OFF"
vs_str[127] = "OFFLINE"

def fc_decode_json(m):
   try:
      m = m.replace('\r', '\\r').replace('\n', '\\n')
      return json.loads(m[m.find('{'):].decode('utf-8','ignore'))
   except:
      return json.loads('{\'lv\':0}')

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
      print(colored(" => END <=", "yellow","on_blue"))
      time.sleep(6)
      sys.exit()
   vs = msg['vs']
   if vs == 127:
      print(colored(" => Model is OFFLINE! <=", "yellow", "on_red"))
      print(colored("\n => END <=", 'yellow','on_blue'))
      time.sleep(3)
      sys.exit()

   usr = msg['nm']
   uid = msg['uid']
   cid = msg['uid'] + 100000000
   m_info = msg['m']
   u_info = msg['u']
   flags = m_info['flags']
   camscore = int(m_info['camscore'])
   continent = m_info['continent']
   ethnic = u_info['ethnic']

   try:
      rc = m_info['rc']
   except:
      rc = '-'

   try:
      country = u_info['country']
   except:
      country = '-'

   try:
      city = u_info['city']
   except:
      city = '-'

   try:
      age = u_info['age']
   except:
      age = '-'

   try:
      occupation = u_info['occupation']
   except:
      occupation = '-'

   try:
      topic = urllib.unquote(m_info['topic']).decode('utf-8')
   except:
      topic = '-'

   try:
      blurb = u_info['blurb']
   except:
      blurb = '-'

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
   print (colored(" => ({}) * {} * ({}) * Server: {} * Score: {} * Viewers: {} <=", "yellow", "on_blue")).format(camgirl,buf,cserver,server,camscore,rc)
   print (colored("\n => Cont: {} * Location: {}-{} * Age: {} * Ethnic: {} * Job: {} <=", "yellow", "on_blue")).format(continent,city,country,age,ethnic,occupation)
   print (colored("\n => Topic => {} <=", "yellow", "on_blue")).format(topic)
   print (colored("\n => Blurb => {} <=\n", "yellow", "on_blue")).format(blurb)
#   print (colored(" => (MODEL DATA) => {} <=\n", "white", "on_blue")).format(msg)

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
   try:
      cservers = ["xchat107","xchat108","xchat61","xchat94","xchat109","xchat22","xchat47","xchat48","xchat49",
                 "xchat26","ychat30","ychat31","xchat95","xchat20","xchat111","xchat112","xchat113","xchat114",
                 "xchat115","xchat116","xchat118","xchat119","xchat41","xchat42","xchat43","xchat44","ychat32",
                 "xchat27","xchat45","xchat46","xchat39","ychat33","xchat120","xchat121","xchat122","xchat123",
                 "xchat124","xchat125","xchat126","xchat67","xchat66","xchat62","xchat63","xchat64","xchat65",
                 "xchat23","xchat24","xchat25","xchat69","xchat70","xchat71","xchat72","xchat73","xchat74","xchat75",
                 "xchat76","xchat77","xchat40","xchat80","xchat28","xchat29","xchat30","xchat31","xchat32","xchat33",
                 "xchat34","xchat35","xchat36","xchat90","xchat92","xchat93","xchat81","xchat83","xchat79","xchat68",
                 "xchat78","xchat84","xchat85","xchat86","xchat87","xchat88","xchat89","xchat96","xchat97","xchat98",
                 "xchat99","xchat100","xchat101","xchat102","xchat103","xchat104","xchat105","xchat106","xchat127"];
      cserver = str(random.choice(cservers))
      host = ('ws://{}.myfreecams.com:8080/fcsl'.format(cserver))
      ws = create_connection(host)
      ws.send("hello fcserver\n\0")
      ws.send("1 0 0 20071025 0 guest:guest\n\0")
   except:
      print(colored(" => This chat server is busy ... Try again <=", "yellow", "on_red"))
      time.sleep(6)
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
                mode = int(raw_input(colored(" => Mode => Exit(5) => YTDL(4) => SL(3) => LS(2) => FFMPEG(1) => FFPLAY(0) => ", "white", "on_green")))
                break
             except ValueError:
                print(colored("\n => Input must be a number <=\n", "yellow", "on_red"))
         if mode == 0:
            mod = 'FFPLAY'
         if mode == 1:
            mod = 'FFMPEG'
         if mode == 2:
             mod = 'LS'
         if mode == 3:
             mod = 'SL'
         if mode == 4:
             mod = 'YTDL'
         if mode == 5:
             mod = 'EXIT'

         hlsurl = "http://video"+str(server)+".myfreecams.com:1935/NxServer/ngrp:mfc_"+str(cid)+".f4v_mobile/playlist.m3u8"
         timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
         stime = str(time.strftime("%H:%M:%S"))
         path = config.get('folders', 'output_folder')
         fn = camgirl + '_MFC_' + timestamp
         fn1 = camgirl + '_MFC_' + timestamp + '.flv'
         fn2 = camgirl + '_MFC_' + timestamp + '.mp4'
         fn3 = camgirl + '_MFC_' + timestamp + '.ts'
         pf1 = (path + fn1)
         pf2 = (path + fn2)
         pf3 = (path + fn3)
         ffmpeg = config.get('files', 'ffmpeg')
         ffplay = config.get('files', 'ffplay')
         livestreamer = config.get('files', 'livestreamer')
         streamlink = config.get('files', 'streamlink')
         youtube = config.get('files', 'youtube')

         if mod == 'FFPLAY':
            print (colored("\n => FFPLAY => {} <=", "yellow", "on_magenta")).format(fn)
            command = ('{} -hide_banner -loglevel panic -i {} -infbuf -autoexit -x 640 -y 480 -window_title "{} * {} * {} * {}"'.format(ffplay,hlsurl,camgirl,stime,cserver,cgn))
            os.system(command)
            print(colored(" => END <= ", "yellow","on_blue"))

         if mod == 'FFMPEG':
            print (colored("\n => FFMPEG-REC => {} <=","yellow","on_red")).format(fn1)
            print
            command = ('{} -hide_banner -loglevel panic -i {} -c:v copy -c:a aac -b:a 160k {}'.format(ffmpeg,hlsurl,pf1))
            os.system(command)
            print(colored(" => END <= ", "yellow","on_blue"))

         if mod == 'LS':
            print (colored('\n => LS-REC >>> {} <<<', 'yellow', 'on_red')).format(fn2)
            print
            command = ('{} hlsvariant://"{}" best -Q -o "{}"'.format(livestreamer,hlsurl,pf2))
            os.system(command)
            print(colored(" => END <= ", 'yellow','on_blue'))

         if mod == 'SL':
            print (colored('\n => SL-REC >>> {} <<<', 'yellow', 'on_red')).format(fn2)
            print
            command = ('{} hls://"{}" best -Q -o "{}"'.format(streamlink,hlsurl,pf2))
            os.system(command)
            print(colored(" => END <= ", 'yellow','on_blue'))

         if mod == 'YTDL':
            print (colored('\n => YTDL-REC => {} <=', 'yellow', 'on_red')).format(fn3)
            command = ('{} --hls-use-mpegts --no-part -q {} -o {}'.format(youtube,hlsurl,pf3))
            os.system(command)
            print(colored("\n => END <= ", 'yellow','on_blue'))

         if mod == 'EXIT':
            print(colored("\n => END <= ", 'yellow','on_blue'))
            time.sleep(3)
            sys.exit()

      else:
         print(colored(" => 'NO MOBILE FEED' models is not supported. <=", "yellow", "on_red"))
         print(colored("\n => END <=\n", "yellow","on_blue"))
         raw_input(colored("Press Enter to exit", "yellow", "on_blue"))
         sys.exit()
   else:
      print(colored(" => This video stream can't be recorded. <=", "yellow", "on_red"))
      print(colored("\n => END <=\n", "yellow","on_blue"))
      raw_input(colored("Press Enter to exit", "yellow", "on_blue"))
      sys.exit()
