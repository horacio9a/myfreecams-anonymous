# MFC Anonymous All Modes Recorder v.1.0.9 by horacio9a for Python 2.7.14

import sys,os,urllib,re,json,time,datetime,random,requests,command,websocket
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.cfg')

init()
print(colored("\n => START <=", "yellow", "on_blue"))

vs_str = {}
vs_str[0] = 'PUBLIC'
vs_str[2] = 'AWAY'
vs_str[12] = 'PRIVATE'
vs_str[13] = 'GROUP'
vs_str[90] = 'CAM-OFF'
vs_str[127] = 'OFFLINE'

def fc_decode_json(m):
   try:
      return json.loads(m[m.find('{'):].decode('utf-8','ignore'))
   except:
      print (colored("\n => Error reply ... check your entry ({}) <=", "white", "on_red")).format(model)
      time.sleep(6)
      print(colored("\n => END <=", "yellow","on_blue"))
      time.sleep(1)
      sys.exit()

def read_model_data(m):
   global model
   global server
   global cid
   global vs
   msg = fc_decode_json(m)
   model = msg['nm']
   cid = msg['uid'] + 100000000
   vs = msg['vs']
   if vs == 127:
      print (colored("\n => Model ({}) is OFFLINE <=", "white", "on_red")).format(model)
      time.sleep(3)
      print(colored("\n => END <=", 'yellow','on_blue'))
      time.sleep(1)
      sys.exit()
   m_info = msg['m']
   u_info = msg['u']
   flags = m_info['flags']
   camscore = int(m_info['camscore'])
   continent = m_info['continent']
   ethnic = u_info['ethnic']
   new_model = m_info['new_model']
   if new_model == 0:
      newmodel = 'No'
   if new_model == 1:
      newmodel = 'Yes'

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
      topic = urllib.unquote(m_info['topic'])
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
   except:
      pass

   try:
      if flags == 15400:
         buf = '(TRUEPVT)'
      else:
         buf = '('+vs_str[vs]+')'
   except:
      pass

   print (colored("\n => ({}) * {} * ({}) * Server: {} * Flags: {} * Score: {} <=", "white", "on_blue")).format(model,buf,cserver,server,flags,camscore)
   print (colored("\n => Continent: {} * Location: {}-{} * Age: {} * Ethnic: {} <=", "yellow", "on_blue")).format(continent,city,country,age,ethnic)
   print (colored("\n => Occupation: {} * New: {} * Viewers: {} * Blurb: {} <=", "yellow", "on_blue")).format(occupation,newmodel,rc,blurb)
   print (colored("\n => Topic => {} <=", "blue", "on_white")).format(topic)
   # print (colored("\n => (MODEL DATA) => {} <=", "white", "on_blue")).format(mdata)

if __name__ == '__main__':
   if len(sys.argv) > 1:
      model = sys.argv[1]
   else:
      while True:
         try:
            modellist = open(config.get('files', 'model_list'),'r')
            for (num,value) in enumerate(modellist):
               print " =>",(num+1),value[:-1]
            print
            cgn = int(raw_input(colored(" => Select MFC Model => ", "yellow", "on_blue")))
            break
         except ValueError:
            print(colored("\n => Input must be a number <=", "white", "on_red"))
      model = open(config.get('files', 'model_list'), 'r').readlines()[cgn-1][:-1]
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
      cserver = '{}'.format(random.choice(cservers))
      ws_host = 'ws://{}.myfreecams.com:8080/fcsl'.format(cserver)
      ws = websocket.WebSocket()
      ws.connect(ws_host, sslopt={"check_hostname": False})
      # ws.connect(ws_host, http_proxy_host='159.203.126.11', http_proxy_port=8080, sslopt={"check_hostname": False})

      send_msg_hello = 'hello fcserver\n\0'
      send_msg_login = '1 0 0 20071025 0 guest:guest\n\0'
      send_msg_ping = '1 0 0 0 0\n\0'
      send_msg_keep_alive = '0 0 0 1 0\n\0'
      send_msg_model = '10 0 0 20 0 {}\n\0'.format(model)
      send_msg_logout = '99 0 0 0 0'

      ws.send(send_msg_hello)
      ws.send(send_msg_login)

   except:
      print (colored("\n => {} server is busy ... Try again <=", "white", "on_red")).format(cserver)
      time.sleep(3)
      print(colored("\n => END <=", "yellow","on_blue"))
      time.sleep(1)
      sys.exit()

   rembuf = ''
   quitting = 0
   while quitting == 0:
      sock_buf =  ws.recv()
      sock_buf = rembuf+sock_buf
      rembuf = ''
      while True:
         hdr = re.search (r'(\w+) (\w+) (\w+) (\w+) (\w+)', sock_buf)
         if bool(hdr) == 0:
            break
         fc = hdr.group(1)
         mlen = int(fc[0:4])
         fc_type = int(fc[4:])
         mdata = sock_buf[4:4+mlen]
         if len(mdata) < mlen:
            rembuf = ''.join(sock_buf)
            break
         mdata = urllib.unquote(mdata)
         if fc_type == 1:
            ws.send(send_msg_model)
         elif fc_type == 10:
            read_model_data(mdata)
            quitting = 1
         sock_buf = sock_buf[4+mlen:]
         if len(sock_buf) == 0:
            break
   # ws.send(send_msg_logout)
   ws.close()

   if vs == 0:
      if server != 0:
         while True:
             try:
                mode = int(raw_input(colored("\n => Mode => Exit(6) => URL(5) => YTDL(4) => SL(3) => LS(2) => FFMPEG(1) => FFPLAY(0) => ", "white", "on_green")))
                break
             except ValueError:
                print(colored("\n => Input must be a number <=", "white", "on_red"))
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
            mod = 'URL'
         if mode == 6:
            mod = 'EXIT'

         hlsurl = 'http://video{}.myfreecams.com:1935/NxServer/ngrp:mfc_{}.f4v_mobile/playlist.m3u8'.format(server,cid)
         timestamp = str(time.strftime('%d%m%Y-%H%M%S'))
         stime = str(time.strftime('%H:%M:%S'))
         path = config.get('folders', 'output_folder')
         fn = model + '_MFC_' + timestamp
         fn1 = model + '_MFC_' + timestamp + '.flv'
         fn2 = model + '_MFC_' + timestamp + '.mp4'
         fn3 = model + '_MFC_' + timestamp + '.ts'
         fn4 = model + '_MFC_' + timestamp + '.txt'
         pf1 = (path + fn1)
         pf2 = (path + fn2)
         pf3 = (path + fn3)
         pf4 = (path + fn4)
         ffmpeg = config.get('files', 'ffmpeg')
         ffplay = config.get('files', 'ffplay')
         livestreamer = config.get('files', 'livestreamer')
         streamlink = config.get('files', 'streamlink')
         youtube = config.get('files', 'youtube')

         if mod == 'FFPLAY':
            print (colored("\n => FFPLAY => {} <=", "yellow", "on_magenta")).format(fn)
            command = '{} -hide_banner -loglevel panic -i {} -infbuf -autoexit -x 640 -y 480 -window_title "{} * {} * {} * {}"'.format(ffplay,hlsurl,model,stime,cserver,cgn)
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
            command = '{} hlsvariant://"{}" best -Q -o "{}"'.format(livestreamer,hlsurl,pf2)
            os.system(command)
            print(colored(" => END <= ", 'yellow','on_blue'))

         if mod == 'SL':
            print (colored('\n => SL-REC >>> {} <<<', 'yellow', 'on_red')).format(fn2)
            print
            command = '{} hls://"{}" best -Q -o "{}"'.format(streamlink,hlsurl,pf2)
            os.system(command)
            print(colored(" => END <= ", 'yellow','on_blue'))

         if mod == 'YTDL':
            print (colored('\n => YTDL-REC => {} <=', 'yellow', 'on_red')).format(fn3)
            command = '{} --hls-use-mpegts --no-part -q {} -o {}'.format(youtube,hlsurl,pf3)
            os.system(command)
            print(colored("\n => END <= ", 'yellow','on_blue'))

         if mod == 'URL':
            print (colored("\n => URL => {} <=", "white", "on_green")).format(fn4)
            file=open(pf4,'wb')
            file.write(hlsurl)
            file.close()
            raw_input(colored("\n => Press Enter to exit <=", "yellow", "on_blue"))
            print(colored("\n => END <=", "yellow","on_blue"))
            time.sleep(1)
            sys.exit()

         if mod == 'EXIT':
            print(colored("\n => END <= ", 'yellow','on_blue'))
            time.sleep(3)
            sys.exit()

      else:
         print (colored("\n => ({}) is 'NO MOBILE FEED' model who isn't supported yet <=", "white", "on_red")).format(model)
         raw_input(colored("\n => Press Enter to exit <=", "yellow", "on_blue"))
         print(colored("\n => END <=", "yellow","on_blue"))
         time.sleep(1)
         sys.exit()

   else:
      print (colored("\n => ({}) video stream can't be recorded now <=", "white", "on_red")).format(model)
      raw_input(colored("\n => Press Enter to exit <=", "yellow", "on_blue"))
      print(colored("\n => END <=", "yellow","on_blue"))
      time.sleep(1)
      sys.exit()
