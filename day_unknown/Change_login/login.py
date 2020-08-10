#!/usr/bin/env python3
import os,gi,shutil,subprocess,sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk,GdkPixbuf,Gdk,Pango
def root_check():
    root = subprocess.getoutput("id -u")
    if root!=str(0):
        print("This script needs root permission \n Try again with sudo \n Exiting.....")
        sys.exit(0)
root_check()
curr_dir = os.path.dirname(__file__)
gres_file = "/usr/share/gnome-shell/gnome-shell-theme.gresource"
css = "gnome-shell.css"
version = subprocess.getoutput("lsb_release -c | cut -f 2")
if version.__contains__("focal"):
    gres_file = subprocess.getoutput("update-alternatives --display gdm3-theme.gresource | grep current")
    gres_file = gres_file[gres_file.index("/")::]
    css = "gdm3.css"
dest_dir = os.path.join(curr_dir+"/theme")
os.chdir(curr_dir)
print(os.getcwd())
def shell(cmd):
    os.system(cmd)
class Handler:
    def showimg(self):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(filechooser.get_filename(),750,500)
        image.set_from_pixbuf(pixbuf)
    def confirm(self):
        if filechooser.get_filename():
            dialog = Gtk.MessageDialog(parent=window,title="Confirmation",modal=True,buttons=Gtk.ButtonsType.OK_CANCEL,text="Immediate restart required \n Do you want to continue?")
            dialog.show()
            dialog.connect("response",Handler.restart)
        else:
            dialog = Gtk.MessageDialog(parent=window,title="ERROR",modal=True,buttons=Gtk.ButtonsType.OK,text="Please select image first")
            dialog.run()
            dialog.destroy()
    def restart(self,response_id):
        if response_id==Gtk.ResponseType.OK:
            print(os.getcwd())
            shell("sudo %s %s %s %s"%(curr_dir+"/script/login",filechooser.get_filename(),gres_file,css))
            self.destroy()
        else:
            Gtk.main_quit()
            self.destroy()


        
        
window = Gtk.Window()
window.connect("destroy",Gtk.main_quit)
lt1 = Gtk.Layout()
lt2 = Gtk.Frame()
lt2.set_label("Your Image Here")
lt2.modify_bg(Gtk.StateType.NORMAL,Gdk.color_parse("#808080"))
lt2.set_label_align(0.5,0.5)
grid = Gtk.Box()
grid.set_spacing(10)
confirm = Gtk.Button(("confirm"))
confirm.set_size_request(150,50)
confirm.set_margin_left(600)
confirm.connect("clicked",Handler.confirm)
filechooser = Gtk.FileChooserButton()
filechooser.connect("file-set",Handler.showimg)
filechooser.set_size_request(150,50)
filefilter = Gtk.FileFilter()
filefilter.add_pattern("*.jpg")
filefilter.add_pattern("*.png")
filechooser.set_filter(filefilter)
grid.set_valign(Gtk.Align.CENTER)
grid.set_orientation(Gtk.Orientation.VERTICAL)
lt2.set_size_request(750,430)
lt1.set_size_request(750,200)
image = Gtk.Image()
lt2.add(image)
image.show()
label = Gtk.Label("Choose a Image")
label.modify_font(Pango.FontDescription("Serif Italic 14"))
label.set_margin_top(50)
lt1.add(filechooser)
lt1.add(label)
lt1.add(confirm)
grid.add(lt2)
grid.add(lt1)
window.add(grid)
window.show_all()
window.set_size_request(750,800)
Gtk.main()
