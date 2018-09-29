#!/usr/bin/env python

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import NumericProperty, ListProperty, ObjectProperty, DictProperty
from kivy.properties import StringProperty
from kivy.event import EventDispatcher

class Port(EventDispatcher):
    title = StringProperty()
    def __init__(self, **kwargs):
        super(Port, self).__init__(**kwargs)

class Component(EventDispatcher):
    title = StringProperty()
    ports = ListProperty()
    def __init__(self, **kwargs):
        super(Component, self).__init__(**kwargs)

class Symbol(EventDispatcher):
    component = ObjectProperty()
    def __init__(self, **kwargs):
        super(Symbol, self).__init__(**kwargs)

class SymbolView(RelativeLayout):
    symbol = ObjectProperty()
    def __init__(self, **kwargs):
        self.port_views = {}
        super(SymbolView, self).__init__(**kwargs)
        self.symbol.component.bind(ports=self.update_ports)
        self.update_ports()

    def update_ports(self, *args, **kw):
        print('update_ports')
        for p in self.symbol.component.ports:
            if not p.title in self.port_views:
                print('adding port:', p.title)
                pv = RectLabel(text=p.title)
                #pv.width = self.ids.box.width
                pv.bg_color = 0,1,0,0.5
                self.port_views[p.title] = pv
                self.ids.box.add_widget(pv)

class Main(BoxLayout):
    pass

class RectLabel(Label):
    bg_color = ListProperty((0,0,0,0))

c = Component(title="C1", ports=[
    Port(title="Port1xxxxxxxx"),
    Port(title="Port2xxxxxx"),
])
s = Symbol(component=c)

class GcdApp(App):

    def callback(self, button):
        print("pressed")
        c.title = c.title + "k"
        c.ports.append(Port(title="a{}".format(len(c.ports))))

    def build(self):
        root = Main()
        button = root.ids.button1
        button.bind(on_press=self.callback)
        d = root.ids.drawing1
        d.add_widget(SymbolView(symbol=s))
        return root

if __name__ == '__main__':
    GcdApp().run()
