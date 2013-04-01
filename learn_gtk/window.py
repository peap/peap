#!/usr/bin/env python3

from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title='Hello World')

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label='Hello')
        self.button1.connect('clicked', self.on_button_clicked, 'Hello')
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label='Goodbye')
        self.button2.connect('clicked', self.on_button_clicked, 'Goodbye')
        self.box.pack_start(self.button2, True, True, 0)

        self.launch_button = Gtk.Button(label='launch grid...')
        self.launch_button.connect('clicked', self.launch_grid)
        self.box.pack_start(self.launch_button, True, True, 0)

    def on_button_clicked(self, widget, value):
        print('value: {0}'.format(value))

    def launch_grid(self, widget):
        win = GridWindow()
        win.show_all()


class GridWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title='Grid Example')
 
        grid = Gtk.Grid()
        self.add(grid)
 
        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")
 
        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)


def main():
    win = MyWindow()
    win.connect('delete-event', Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
