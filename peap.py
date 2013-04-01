#!/usr/bin/env python3

from gi.repository import Gtk


def get_test_data():
    f = open('/home/eap/code/peap/test_data.txt')
    data = [line for line in f.read().split('\n') if line != '']
    return data


class PeapWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title='PEAP')

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label='New items:')
        display1 = self.create_display()

        grid.add(button1)
        grid.attach(display1, 1, 0, 1, 1)

    def create_display(self):
        grid = Gtk.Grid()
        data = get_test_data()
        for i, thing in enumerate(data):
            button = Gtk.Button(label=thing)
            if i == 0:
                grid.add(button)
            else:
                grid.attach(button, 0, i, 1, 1)
        return grid





def main():
    win = PeapWindow()
    win.connect('delete-event', Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
