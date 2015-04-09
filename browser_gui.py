#!/usr/bin/env python3

from gi.repository import Gtk
import requests
from bs4 import BeautifulSoup as bs 

class Handler:

	def on_quit(self, *args):
		print("Quit")
		Gtk.main_quit(*args)
	
	def on_go_button_clicked(self, button):
		http = "http://"
		url = ""

		self.url_entry_text = url_entry.get_text()

		if http in self.url_entry_text:
			url = self.url_entry_text
		else:
			url = http + self.url_entry_text

		req = requests.get(url)
		soup = bs(req.text)
		html_buffer.set_text(soup.prettify())
		print("URL: {}".format(url))

# Build the GUI from the XML specifications
# and connect handler functions
builder = Gtk.Builder()
builder.add_from_file("gui_layout.glade")
builder.connect_signals(Handler())

# Get the main window to show all widgets
window = builder.get_object("main_browser_window")

# Get the url entry text box so the go button handler
# can access that text
url_entry = builder.get_object("url_entry")

# Get the html_buffer object so we can set the text inside of it
html_buffer = builder.get_object("html_buffer")

# Show the main browser window
window.show_all()

Gtk.main()
