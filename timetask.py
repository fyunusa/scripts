import gtk.gdk
import time
import random

while 1 :
    # generate a random time between 120 and 300 sec
    random_time = random.randrange(120,300)

    # wait between 120 and 300 seconds (or between 2 and 5 minutes)
    print "Next picture in: %.2f minutes" % (float(random_time) / 60)
    time.sleep(random_time)

    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])

    ts = time.time()
    filename = "screenshot"
    filename += str(ts)
    filename += ".png"

    if (pb != None):
        pb.save(filename,"png")
        print "Screenshot saved to "+filename
    else:
        print "Unable to get the screenshot."