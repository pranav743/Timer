import threading
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.button import Button
import time
import playsound
Builder.load_file('.//alarm_by_pranav.kv')
Window.size=(550,550)

# def timer(hours,mins,secs):
#    print("Started")
#    t=int(hours)*60*60+int(mins)*60+int(secs)
#    while (t):
#       if event.is_set():
         
#          break
#       h=t//(60*60)
#       m=(t%(60*60))//60
#       s=t-(h*60*60)-(m*60)
      
#       timer='{:02d}:{:02d}:{:02d}'.format(h,m,s)
#       print(timer,end='\r')
#       time.sleep(1)      
#       t=t-1



class Alarm_by_PranavWidget(Widget):
    event=threading.Event()

    def sound(self):
        playsound.playsound('C:\Pranav\VS Code\python 1\.dist\GUI\Alarm_Sound.mp3')

    def timer(self):
        try:
            hours=self.ids.I_hr.text
            
            hours=int(hours)*60*60
            if hours>(23*60*60):
                hours=(23*60*60)
            
        except: hours=0    
        try:
            mins=self.ids.I_min.text
            mins=int(mins)*60
            if mins>(59*60):
                mins=(59*60)
        except: mins=0    
        try:
            secs=self.ids.I_sec.text
            secs=int(secs)
            if secs>(60):
                secs=(60)
        except: secs=0    

        t=hours+mins+secs
        
    
        while (t):
            if Alarm_by_PranavWidget.event.is_set():
                self.ids.time_display.text=f""
                Alarm_by_PranavWidget.event.clear()
                break

            h=t//(60*60)
            m=(t%(60*60))//60
            s=t-(h*60*60)-(m*60)
            
            timer='{:02d}:{:02d}:{:02d}'.format(h,m,s)
            # print(timer,end='\r')
            self.ids.time_display.text=f"{timer}"
            time.sleep(1)      
            t=t-1
            if t==1:
                alarm=threading.Thread(target=self.sound) 
                alarm.start()  
        self.ids.time_display.text=f"" 
        self.ids.initiation.text="START"  
        self.ids.status.text="OFF" 
        self.ids.status.color=(99/255, 9/255, 9/255)
         
    def start_alarm(self):
        
        try:
            hours=self.ids.I_hr.text
            hours=int(hours)*60*60
            
        except: hours=0    
        try:
            mins=self.ids.I_min.text
            mins=int(mins)*60
        except: mins=0    
        try:
            secs=self.ids.I_sec.text
            secs=int(secs)
        except: secs=0    

        total_time=hours+mins+secs

        if total_time==0:
            pass
        elif total_time>0:
            if self.ids.status.text=="ON":
                Alarm_by_PranavWidget.event.set()
                
                self.ids.status.text=f"OFF"
                self.ids.status.color=(99/255, 9/255, 9/255)
                

            else:
                
                self.ids.status.text=f"ON"
                thread=threading.Thread(target=self.timer, daemon=True)
                thread.start()
                
                self.ids.status.color=(23/255, 99/255, 9/255)
            

            if self.ids.initiation.text=="START":
                self.ids.initiation.text=f"STOP"
            
                

            else:
                self.ids.initiation.text=f"START"
      
        print(hours,":",mins,":",secs)
        
     
        
        



    


class Alaram_by_PranavApp(App):

    def build(self):
        self.title="  Alarm - by Pranav"
        
        return Alarm_by_PranavWidget()




if __name__=='__main__':
    Alaram_by_PranavApp().run()
