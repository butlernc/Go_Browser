package main

import (
		"fmt"
		"github.com/mattn/go-gtk/gtk"
		"github.com/mattn/go-gtk/glib"
)

func main() {
    gtk.Init(nil)
    window := gtk.NewWindow(gtk.WINDOW_TOPLEVEL)
    window.SetPosition(gtk.WIN_POS_CENTER)
    window.SetTitle("Go Browser!")
    window.SetIconName("gtk-dialog-info")
    window.Connect("destroy", func(ctx *glib.CallbackContext) {
        println("got destroy!", ctx.Data().(string))
        gtk.MainQuit()
    }, "now exiting")

	entry := gtk.NewEntry()

	url_fixed_frame := gtk.NewFixed()
	url_fixed_frame.Put(entry, 10, 10)
	window.Add(url_fixed_frame)

	window.SetSizeRequest(600, 600)
	window.ShowAll()
	gtk.Main()

	fmt.Printf("browser\n")
}
