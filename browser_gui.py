#!/usr/bin/env python3

from gi.repository import Gtk
import requests
from bs4 import BeautifulSoup as bs 

class History:
	
	def __init__(self):
		self.history = []
		self.position = -1

	def add(self, url):
		self.history.append(url)
		self.position += 1

	def get_previous(self):
		url = ""
		if self.position > 0:
			url = self.history[self.position]
			self.position -= 1
		else:
			url = self.history[self.position]
		return url

	def get_next(self):
		url = ""
		if (self.position + 1) == len(self.history):
			url = self.history[self.position]
		else:
			self.position += 1
			url = self.history[self.position]
		return url

	def get_current(self):
		return self.history[self.position]

class Handler:

	def on_quit(self, *args):
		print("Quit")
		Gtk.main_quit(*args)
	
	def on_back_button_clicked(self, button):
		# Get previous url from history
		url = history.get_previous()

		# Send request
		req = request_url(url)
		
		soup = bs(req.text)
		html_buffer.set_text(soup.prettify())

	def on_forward_button_clicked(self, button):
		# Get next url from history
		url = history.get_next()

		# Send request
		req = request_url(url)
		
		soup = bs(req.text)
		html_buffer.set_text(soup.prettify())

	def on_refresh_button_clicked(self, button):
		# Get current url
		url = history.get_current()

		# Send request
		req = request_url(url)

		soup = bs(req.text)
		html_buffer.set_text(soup.prettify())

	def on_go_button_clicked(self, button):
		# Get text from url entry box
		self.url_entry_text = url_entry.get_text()

		# Completes the request
		req = request_url(self.url_entry_text)
		
		# Make it pretty to put in the browser
		soup = bs(req.text)
		html_buffer.set_text(soup.prettify())

		# Add the url to the history
		history.add(self.url_entry_text)

		print("URL: {}".format(self.url_entry_text))

def request_url(url):
	http = "http://"
	new_url = ""

	# If "http://" was not typed in the url,
	# this will add it so the request library doesn't bitch
	if http in url:
		new_url = url
	else:
		new_url = http + url

	req = requests.get(new_url)
	
	return req

# Initialize History
history = History()

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
