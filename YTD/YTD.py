import re
from functools import partial

from kivy.uix.dropdown import DropDown
from pytube import YouTube

from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.core.window import Window
Window.size = (500,600)

class MyApp(MDApp):
    def getLinkInfo(self,event, layout):
        self.link = self.input.text
        self.chkLink = re.match("^https://www.youtube.com/.*", self.link)
        print(self.chkLink)

        if(self.chkLink):
            self.errLabel.text=""
            self.errLabel.pos_hint={'center_x':0.5,'center_y':20}
            
            try:
                self.yt = YouTube(self.link)
                self.titleLabel.text ="Title :" + str(self.yt.title)
                self.titleLabel.pos_hint = {'center_x':0.5,'center_y':0.4}

                self.viewsLabel.text ="Views :" +  str(self.yt.views)
                self.viewsLabel.pos_hint = {'center_x':0.5,'center_y':0.35}

                self.lengthLabel.text ="Length :" +  str(self.yt.length / 60)
                self.lengthLabel.pos_hint = {'center_x':0.5,'center_y':0.3}

                self.dwnloadButt.text ="Download"
                self.dwnloadButt.pos_hint = {'center_x':0.5,'center_y':0.15}
                self.dwnloadButt.size_hint = (0.3,0.1)

                self.video = self.yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
                print(self.video)
                self.dropDown = DropDown()
                for video in self.video:
                    bttn = Button(
                        text = video.resolution,
                        size_hint_y = None,
                        height = 30
                    )
                    bttn.bind(on_release = lambda bttn:self.dropDown.select(bttn.text))
                    self.dropDown.add_widget(bttn)

                self.main_btn = Button(
                    text = "144p",
                    size_hint = (None, None),
                    pos = (350, 65),
                    height = 50
                )
                self.main_btn.bind(on_release = self.dropDown.open)
                self.dropDown.bind(on_select = lambda instance, x:setattr(self.main_btn,'text',x))
                layout.add_widget(self.main_btn)

                print("Title :" + str(self.yt.title))
                print("Views :" + str(self.yt.views))
                print("Length :" + str(self.yt.length))
            except:
                self.errLabel.text = "Network or unknown Error"
                self.errLabel.pos_hint = {'center_x':0.5, 'center_y':0.40}
            
        else:
            print("Invalid Link")
            self.errLabel.text = "Invalid or Empty Link"
            self.errLabel.pos_hint = {'center_x':0.5, 'center_y':0.40}

    def download(self,event,layout):
        self.ys = self.yt.streams.filter(file_extension='mp4').filter(res=self.main_btn.text).first()
        print("Downloading")
        self.ys.download()
        print("Complete")

    def build(self):
        layout = MDRelativeLayout(md_bg_color = [51/255,153/255,255/255])
        self.img = Image(
                source='image.png', size_hint=(0.5,0.5), 
                pos_hint = {'center_x':0.5, 'center_y':0.90}
                         )
        
        self.ytLink = Label(
                text = "Please enter the YT link",
                pos_hint = {'center_x':0.5, 'center_y':0.75},
                size_hint=(1,1), font_size=20,color=(1,0,0)
                            )
        self.input = TextInput(
                text = "",
                pos_hint = {'center_x':0.5, 'center_y':0.65},
                size_hint=(1,None), 
                height=48,
                font_size=29,
                foreground_color=(0,0.5,0),
                font_name="Comic"
                )

        self.linkbutton = Button(
            text = "Get Link",
            pos_hint={'center_x':0.5, 'center_y':0.5},
            size_hint = (0.2,0.1),
            font_name = "Comic",
            font_size = 24,
            background_color = [0,1,0]
        )
        self.linkbutton.bind(on_press = partial(self.getLinkInfo,layout))

        self.titleLabel = Label(
            text=" ",
            pos_hint={'center_x':0.5, 'center_y':20},
            size_hint=(1,1),
            font_size=20
        )

        self.viewsLabel = Label(
            text=" ",
            pos_hint={'center_x': 0.5, 'center_y': 20},
            size_hint=(1, 1),
            font_size=20
        )

        self.lengthLabel = Label(
            text=" ",
            pos_hint={'center_x': 0.5, 'center_y': 20},
            size_hint=(1, 1),
            font_size=20
        )

        self.dwnloadButt = Button(
            pos_hint = {'center_x':0.5, 'center_y':20.0},
            size_hint = (1,1),
            size = (75,75),
            font_name='Comic',
            bold = True,
            font_size = 24,
            background_color = (0,1,0)
        )
        self.dwnloadButt.bind(on_press = partial(self.download,layout))

        self.errLabel = Label(
            text="", 
            pos_hint={'center_x':0.5,'center_y':20},
            size_hint = (1,1),
            font_size = 20,
            color = (1,0,0)
            )

        layout.add_widget(self.img)
        layout.add_widget(self.ytLink)
        layout.add_widget(self.input)
        layout.add_widget(self.linkbutton)

        layout.add_widget(self.titleLabel)
        layout.add_widget(self.viewsLabel)
        layout.add_widget(self.lengthLabel)

        layout.add_widget(self.dwnloadButt)

        layout.add_widget(self.errLabel)

        return layout

if __name__ == "__main__":

    MyApp().run()
