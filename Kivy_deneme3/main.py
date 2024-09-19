from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp,sp
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics import Rectangle,Color,Ellipse
from kivy.properties import Clock
import time,random
from kivy.core.audio import SoundLoader
from kivy.core.audio import Sound
sound = SoundLoader.load('lvbelC5.mp3')
sound.play()
sound.loop=True
hiz = 0

class MainWidget(Widget) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menuB= Button(text="Başla",on_press=self.start)
        self.menuI=Image(source="alicemilGiris.jpg",allow_stretch=True,keep_ratio=False)
        self.menuL1=Label(text="KARDAS?Ne baktin la kardas?")
        self.menuL2=Label(text="Oynasana")
        self.add_widget(self.menuI)
        self.add_widget(self.menuB)
        # self.add_widget(self.menu)
        # self.add_widget(self.menuL2)
        self.karakter = Image(source="20240421_222400.png")
        self.tus = Button(on_press=self.yukari,background_color=(1,1,1,0))
        self.arkaPlan=Image(source="arkaplan.jpg",allow_stretch=True,keep_ratio=False,color=(1,1,1,.4))
        self.biberust=Image(source="biberust.png")
        self.biberalt=Image(source="biberalt.png")
        self.muz=Image(source="muz.png")
        self.yenidenDene = Button(on_press=self.start)
        self.puan =Label(text="0",font_name="digital-7.ttf",color=(1,0,1),font_size=dp(90))
        self.tesekkur = Label(text="Yeniden Dene",font_size=dp(40))

    def on_size(self,*args) :
        self.menuB.size=self.width/3,self.height/4
        self.menuB.pos = self.width/2-self.width/6,self.height/2-self.height/3
        self.yenidenDene.size=self.size
        # self.yenidenDene.pos = self.width/2-self.width/6,self.height/2-self.height/3
        self.menuI.size=self.width,self.height
        self.menuL1.font_size = 30
        self.menuL1.pos = self.width/2-15,self.height/2
        self.menuL2.font_size = 30
        self.menuL2.pos = self.width/2-20,self.height/2-60
        self.karakter.size = dp(85),dp(85)
        self.karakter.pos = self.width/4,self.center_y
        self.tus.size=self.size
        # self.tus.pos = self.width-3*self.tus.width,self.tus.width
        self.arkaPlan.size = self.size
        self.biberust.size = self.height/3,self.height/3
        self.biberalt.size = self.height/3,self.height/3
        self.biberust.pos = self.width-self.biberust.width,self.height-self.biberust.height
        self.biberalt.pos = self.width-self.biberalt.width,0
        self.muz.size=dp(80),dp(80)
        self.muz.pos=1.5*self.width,random.randint(0,int(self.height-self.muz.height))
        self.tus.disabled=False
        self.puan.pos =self.puan.width,self.height-self.puan.height
        self.tesekkur.pos = self.center_x-self.tesekkur.width,self.center_y-self.tesekkur.height/2


    def start(self,*args) :
        self.puan.text="0"
        self.puan.font_size =dp(90)
        self.on_size()
        self.clear_widgets()
        self.add_widget(self.tus)
        self.add_widget(self.arkaPlan)
        self.add_widget(self.karakter)

        self.add_widget(self.biberalt)
        self.add_widget(self.biberust)
        self.add_widget(self.muz)
        self.add_widget(self.puan)
        self.eventAsagi=Clock.schedule_interval(self.asagi,1/35)
        self.eventAkis=Clock.schedule_interval(self.akis,1/40)
        self.eventKontrol=Clock.schedule_interval(self.kontrol,1/60)
    
    def yukari(self,*args) :
        x,y = self.karakter.pos
        if y+((self.height-self.karakter.height)/6) <self.height :
            self.karakter.pos = x,y+((self.height-self.karakter.height)/6)
        else :
            self.karakter.pos = x,self.height-self.karakter.height+20
        
    
    def asagi(self,dt,*args) :
        x,y = self.karakter.pos
        if y-((self.height-self.karakter.height)/120) >0 :
            self.karakter.pos = x,y-((self.height-self.karakter.height)/120)
        else :
            self.karakter.pos = x,0
    
    def akis(self,dt,*args) :
        global hiz
        hiz += 0.01
        xa,ya = self.biberalt.pos
        xu,yu = self.biberust.pos
        xm,ym = self.muz.pos
        self.biberust.pos = xu-self.width/160-hiz,yu
        self.biberalt.pos = xa-self.width/160-hiz,ya
        self.muz.pos = xm-self.width/160-hiz,ym
        if xm-self.width/160 < -self.muz.width :
            # self.add_widget(self.muz)
            self.muz.pos = self.width*1.5,random.randint(0,int(self.height-self.muz.height))
        if xu-self.width/160 < -self.biberalt.width :
            self.biberust.pos = self.width,yu
        if xa-self.width/160 < -self.biberalt.width :
            self.biberalt.pos = self.width,ya

    def kontrol(self,dt,*args) :

        if self.biberalt.x-dp(10)<self.karakter.x<self.biberalt.x+dp(40) and ((self.karakter.y<self.biberalt.height+dp(10)) or (self.karakter.y>self.height-self.biberust.height-dp(40))) :
            self.carpti()
        
        if self.muz.x-dp(40)<self.karakter.x<self.muz.x+dp(40) and self.muz.y-dp(40)<self.karakter.y<self.muz.y+dp(40) :
            self.muz.pos = self.width*1.5,random.randint(0,int(self.height-self.muz.height))
            self.puan.text = str(int(self.puan.text) + 1)
    
    def carpti(self,*args) :
        global hiz
        hiz = 0.15
        self.eventAsagi.cancel()
        self.eventAkis.cancel()
        self.eventKontrol.cancel()
        self.tus.disabled=True
        self.clear_widgets()
        self.add_widget(self.yenidenDene)
        self.add_widget(self.arkaPlan)
        self.add_widget(self.tesekkur)
        self.puan.pos=self.center_x-self.puan.width,self.center_y*1.25
        self.puan.font_size=dp(150)
        self.add_widget(self.puan)
class DenemeApp(App) :
    def build(self) :
        self.title = "Muz Yiyen Deniz"
        return MainWidget()

if __name__ == "__main__" :
    DenemeApp().run()

for x in MainWidget().children :
    print(x)