from tkinter import *
import tkinter as Tk
import math
import copy
from tkinter import font as tkFont
from tkinter import filedialog

#Main class, refered from _init_ method
class my2dtransfomations:
    # Variable 't' is the multyplayer for setting bigger size
    t = 2
    arr = []
    arrOriginal = []
    movetocenter = True
    w = 900
    h = 600
    centernew = 0
    centernewy = 0
    scaleARGS = 1
    root = Tk.Tk()
    color = 'gray'
    frame = Frame(root, bg=color, height=80)
    framefoot = Frame()
    canvas = Tk.Canvas(root)
    scaleox = Tk.Entry()
    scaleox2 = scaleox
    inputx = scaleox2
    inputy = scaleox2
    # Added coding help for circle, no need to check - it's:
    # OUT OF REQUIRMENTS OF THIS EXRECIE
    # add codeing help with circule no need to check its
    # OUT OF REQUIRMENTS OF THIS EXRECIE
    # function To Draw Circules
    ymax = 0
    xmax = 0
    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
    # Function to Draw the Circles
    Tk.Canvas.create_circle = _create_circle
    # Function to Draw the Archs
    def _create_circle_arc(self, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self.create_arc(x - r, y - r, x + r, y + r, **kwargs)
    Tk.Canvas.create_circle_arc = _create_circle_arc
    ######################################Assaf please add
    def validate(self, char):

        if char == '.':
            vch = '2'
            return vch.isdigit()
        if char.isdigit():
            self.scaleARGS = int(char)
            print(self.scaleARGS)
        else:

            try:
                self.scaleARGS = float(char)
            except:
                vch = 't'
                return vch.isdigit()
        vch = '2'
        return vch.isdigit()
    def validatenum(self, char):

        if char == '.':
            vch = '2'
            return vch.isdigit()
        if char.isdigit():
            a = int(char)

        else:

            try:
                a = float(char)
            except:
                vch = 't'
                return vch.isdigit()
        vch = '2'
        return vch.isdigit()
        #Setting the drawing in the center of the canvas screen
    def moveTocenter(self):

        distancex = math.floor(((self.w // (self.t*2)) - self.centernew))
        distancey = math.floor((((self.h // (self.t*3)) + 40) - self.centernewy))
        print(distancex, distancey)
        for i in range(len(self.arr)):
            if self.arr[i][0] != 'r':
                varis = int(self.arr[i][0])
                varis += distancex
                self.arr[i][0] = str(varis)
                self.arr[i][1] += distancey
                self.arr[i][2] += distancex
                self.arr[i][3] += distancey
            else:
                #self.arr[i][1] += distancey
                self.arr[i][2] += distancex
                self.arr[i][3] += distancey
    #calling Shearing     
    def shearingx(self):
        self.xshearing = True

    def shearingy(self):
        self.yshearing = True


    xshearing = False
    yshearing = False
    mx = 0
    ymaxx = 0
    xmaxx = 0
    my = 0
    def shearing(self):
        distancex = math.floor(((self.w // (self.t * 2)) - self.centernew))
        distancey = math.floor((((self.h // (self.t * 3)) + 40) - self.centernewy))
        self.ymax = (self.ymax + distancey)
        self.xmax = (self.xmax + distancex)
        y1 = self.leaveinput[1]/self.t
        x1 = self.leaveinput[0]/self.t
        y2 = self.ymax
        x2 = self.ymaxx

        self.mx = -1 * math.floor((y2 - y1)/(x2 - x1))

        x3 = self.xmax
        y3 = self.xmaxx
        self.my = -1 * math.floor((y2 - y1)/(x2 - x1))



        print('ymax', self.ymax, ' xmax ', self.xmax)
        arrbacup = copy.deepcopy(self.arr)
        for i in range(len(self.arr)):
            if self.arr[i][0] != 'r':
                a = int(self.arr[i][0])
                b = self.arr[i][1]
                d = self.arr[i][2]
                e = self.arr[i][3]
            if a != 'r':
                if int(b) > self.ymax:
                    self.ymax = int(b)
                    self.ymaxx = int(a)
                if int(e) > self.ymax:
                    self.ymax = int(e)
                    self.ymaxx = int(d)
                if int(a) > self.xmax:
                    self.xmax = int(a)
                    self.xmaxx = int(b)
                if int(d) > self.xmax:
                    self.xmax = int(d)
                    self.xmaxx = int(e)
            else:
                if int(d) > self.xmax:
                    self.xmax = int(d)
                    self.xmaxx = int(e)
                if int(e) > self.ymax:
                    self.ymaxx = int(d)
                    self.ymax = int(e)
        if self.xshearing:

            for i in range(len(self.arr)):
                if self.arr[i][0] != 'r':
                    x1 = int(self.arr[i][0])
                    y1 = self.arr[i][1]
                    x2 = self.arr[i][2]
                    y2 = self.arr[i][3]

                    # self.arr[i][0] = str(varis)
                    if y1 < self.ymax:
                        self.arr[i][0] = str(math.floor(x1 + self.mx * y1))

                    if y2 < self.ymax:
                        self.arr[i][2] = int(math.floor(x2 + self.mx * y2))




                else:
                    rad = self.arr[i][1]
                    x2 = self.arr[i][2]
                    y2 = self.arr[i][3]
                    if y2 < self.ymax:
                        self.arr[i][2] = int(math.floor(x2 + self.mx * y2))
        else:
            if self.yshearing:
                for i in range(len(self.arr)):
                    if self.arr[i][0] != 'r':
                        x1 = int(self.arr[i][0])
                        y1 = self.arr[i][1]
                        x2 = self.arr[i][2]
                        y2 = self.arr[i][3]

                        if y2 < self.ymax:
                            self.arr[i][3] = int(math.floor(y2 + self.disy))
                        if y1 < self.ymax:
                            self.arr[i][1] = int(math.floor(y1 + self.disy))
                        # self.arr[i][0] = str(varis)






                    else:
                        if self.arr[i][3] >= self.ymax:
                            continue
                        rad = self.arr[i][1]
                        x2 = self.arr[i][2]
                        y2 = self.arr[i][3]
                        self.arr[i][3] = int(math.floor(y2 +  self.disy))

        self.centernew = self.arr[0][2]
        self.centernewy = self.arr[0][3]
        self.movetocenter = False
        self.drawfromarr(self.canvas)
        self.movetocenter = True
        self.arr = copy.deepcopy(arrbacup)

        self.yshearing = False
        self.xshearing = False
    countermir = 0

    #Mirroring function
    def mirror(self):
        arrbacup = copy.deepcopy(self.arr)
        # {y 0}
        # {0 x}
        if self.countermir > 4:
            self.countermir = 0
        if self.countermir == 0:
            xmir = -1
            ymir = 1
        else:
            if self.countermir == 1:
                xmir = -1
                ymir = -1
            else:
                if self.countermir == 2:
                    xmir = 1
                    ymir = -1
                else:
                    xmir = 1
                    ymir = 1

        self.countermir += 1

        for i in range(len(self.arr)):
            if self.arr[i][0] != 'r':
                varis = int(self.arr[i][0])
                varis *= xmir
                self.arr[i][0] = str(varis)
                self.arr[i][1] *= ymir
                self.arr[i][2] *= xmir
                self.arr[i][3] *= ymir
            else:

                self.arr[i][2] *= xmir
                self.arr[i][3] *= ymir

        self.centernew = self.arr[0][2]
        self.centernewy = self.arr[0][3]
        self.drawfromarr(self.canvas)
        # print(arrbacup)
        self.arr = copy.deepcopy(arrbacup)

    #Static mirroring function
    def staticmirror(self):

        # {x 0} 1 0 1 0 -1 0 -1 0
        # {0 y} 0 1 0 -1 0 1 0 -1
        if self.countermir >= 4:
            self.countermir = 0
        if self.countermir == 0:
            xmir = -1
            ymir = 1
        else:
            if self.countermir == 1:
                xmir = -1
                ymir = -1
            else:
                if self.countermir == 2:
                    xmir = -1
                    ymir = 1
                else:
                    xmir = -1
                    ymir = -1

        self.countermir += 1

        for i in range(len(self.arr)):
            if self.arr[i][0] != 'r':
                varis = int(self.arr[i][0])
                varis *= xmir
                self.arr[i][0] = str(varis)
                self.arr[i][1] *= ymir
                self.arr[i][2] *= xmir
                self.arr[i][3] *= ymir
            else:

                self.arr[i][2] *= xmir
                self.arr[i][3] *= ymir

        self.centernew = self.arr[0][2]
        self.centernewy = self.arr[0][3]
        self.drawfromarr(self.canvas)
        # print(arrbacup)

    #Drwaing a translation according to values of X and Y
    def translation(self):

        try:
            a = int(self.inputx.get())
            b = int(self.inputy.get())
        except:
            print('Error fetching X/Z values')
        arrbacup = copy.deepcopy(self.arr)
        distancex = int(self.inputx.get())
        distancey = int(self.inputy.get())
        print(distancex, distancey)
        for i in range(len(self.arr)):
            if self.arr[i][0] != 'r':
                varis = int(self.arr[i][0])
                varis += distancex
                self.arr[i][0] = str(varis)
                self.arr[i][1] += distancey
                self.arr[i][2] += distancex
                self.arr[i][3] += distancey
            else:
                #self.arr[i][1] += distancey
                self.arr[i][2] += distancex
                self.arr[i][3] += distancey

        self.centernew = self.arr[0][2]
        self.centernewy = self.arr[0][3]
        self.movetocenter = False
        self.drawfromarr(self.canvas)
        self.movetocenter = True
        self.arr = copy.deepcopy(arrbacup)

    #Drwaing the Static (fixed) Scale
    def staticscale(self):
        p = 2
        for i in range(len(self.arr)):
            if self.arr[i][0] != 'r':
                varis = int(self.arr[i][0])
                varis *= p
                self.arr[i][0] = str(varis)
                self.arr[i][1] *= p
                self.arr[i][2] *= p
                self.arr[i][3] *= p
            else:
                self.arr[i][1] *= p
                self.arr[i][2] *= p
                self.arr[i][3] *= p
        self.centernew = self.arr[0][2]
        self.centernewy = self.arr[0][3]
        self.drawfromarr(self.canvas)

    #Drwaing the Scale according to the Numerical Value
    def scale(self):
        arrbacup = copy.deepcopy(self.arr)
        if '.' in self.scaleox.get():
            print('----------------------Float Scalar')
            strso = self.scaleox.get()
            strso = str(int(math.floor(int(strso[strso.find('.') + 1]))))
            self.scaleARGS = int(strso)
            try:
                for i in range(len(self.arr)):
                    if self.arr[i][0] != 'r':
                        varis = int(self.arr[i][0])
                        varis = math.floor(varis / self.scaleARGS)
                        self.arr[i][0] = str(varis)
                        self.arr[i][1] = math.floor(self.arr[i][1] / self.scaleARGS)
                        self.arr[i][2] = math.floor(self.arr[i][2] / self.scaleARGS)
                        self.arr[i][3] = math.floor(self.arr[i][3] / self.scaleARGS)
                        if self.arr[i][3] == 0:
                            self.arr[i][3] = 1
                    else:
                        self.arr[i][1] = math.floor(self.arr[i][1] / self.scaleARGS)
                        if self.arr[i][1] == 0:
                            self.arr[i][1] = 1
                        self.arr[i][2] = math.floor(self.arr[i][2] / self.scaleARGS)
                        if self.arr[i][2] == 0:
                            self.arr[i][2] = 1
                        self.arr[i][3] = math.floor(self.arr[i][3] / self.scaleARGS)
                        if self.arr[i][3] == 0:
                            self.arr[i][3] = 1
            except:
                print('Error')
                self.StartOver()
        else:
            self.scaleARGS = int(self.scaleox.get())
            for i in range(len(self.arr)):
                if self.arr[i][0] != 'r':
                    varis = int(self.arr[i][0])
                    varis *= self.scaleARGS
                    self.arr[i][0] = str(varis)
                    self.arr[i][1] *= self.scaleARGS
                    self.arr[i][2] *= self.scaleARGS
                    self.arr[i][3] *= self.scaleARGS
                else:
                    self.arr[i][1] *= self.scaleARGS
                    self.arr[i][2] *= self.scaleARGS
                    self.arr[i][3] *= self.scaleARGS

        self.centernew = self.arr[0][2]
        self.centernewy = self.arr[0][3]
        self.drawfromarr(self.canvas)
        # print(arrbacup)
        self.arr = copy.deepcopy(arrbacup)
        print('Scale')

    #Rotate the drawing according to numerical value
    def rotate(self):
        arrbacup = copy.deepcopy(self.arr)
        teta = float(self.scaleox2.get())
        # xtag = x*cosq - y*sinq
        # ytag = x*sinq + y*cosq
        for i in range(len(self.arr)):
            if self.arr[i][0] != 'r':
                # self.arr[i][0] = str(varis)
                x1 = int(self.arr[i][0])
                y1 = self.arr[i][1]
                x2 = self.arr[i][2]
                y2 = self.arr[i][3]
                self.arr[i][0] = str(math.floor(x1 * math.cos(teta) - y1 * math.sin(teta)))
                self.arr[i][1] = int(math.floor(x1 * math.sin(teta) + y1 * math.cos(teta)))
                self.arr[i][2] = int(math.floor(x2 * math.cos(teta) - y2 * math.sin(teta)))
                self.arr[i][3] = int(math.floor(x2 * math.sin(teta) + y2 * math.cos(teta)))

            else:
                rad = self.arr[i][1]
                x2 = self.arr[i][2]
                y2 = self.arr[i][3]
                self.arr[i][2] = int(math.floor(x2 * math.cos(teta) - y2 * math.sin(teta)))
                self.arr[i][3] = int(math.floor(x2 * math.sin(teta) + y2 * math.cos(teta)))

        self.centernew = self.arr[0][2]
        self.centernewy = self.arr[0][3]
        self.drawfromarr(self.canvas)
        self.arr = copy.deepcopy(arrbacup)
        print(teta)
    rotatecount = 0

    # Rotate the drawing staticaly (by a fixed angle of 45 degrees)
    def staticrotate(self):
        if self.rotatecount < 4:
            teta = float(self.scaleox2.get())+self.rotatecount
            self.rotatecount += 1
        else:
            teta = float(self.scaleox2.get())
            self.rotatecount = 1
        arrbacup = copy.deepcopy(self.arr)
        # xtag = x*cosq - y*sinq
        # ytag = x*sinq + y*cosq
        for i in range(len(self.arr)):
            if self.arr[i][0] != 'r':
                #self.arr[i][0] = str(varis)
                x1 = int(self.arr[i][0])
                y1 = self.arr[i][1]
                x2 = self.arr[i][2]
                y2 = self.arr[i][3]
                self.arr[i][0] = str(math.floor(x1 * math.cos(teta) - y1 * math.sin(teta)))
                self.arr[i][1] = int(math.floor(x1 * math.sin(teta) + y1 * math.cos(teta)))
                self.arr[i][2] = int(math.floor(x2 * math.cos(teta) - y2 * math.sin(teta)))
                self.arr[i][3] = int(math.floor(x2 * math.sin(teta) + y2 * math.cos(teta)))

            else:
                rad = self.arr[i][1]
                x2 = self.arr[i][2]
                y2 = self.arr[i][3]
                self.arr[i][2] = int(math.floor(x2 * math.cos(teta) - y2 * math.sin(teta)))
                self.arr[i][3] = int(math.floor(x2 * math.sin(teta) + y2 * math.cos(teta)))

        self.centernew = self.arr[0][2]
        self.centernewy = self.arr[0][3]
        self.drawfromarr(self.canvas)
        self.arr = copy.deepcopy(arrbacup)
        print(teta)

    #Method for clearing and resetting the canvas 
    def StartOver(self):
        self.arr = []
        self.canvas.delete("all")
        self.drawfromfile(self.canvas)

    #Extracting the matrix values and creating the drawing (Matrix is represented in a file) 
    def drawfromfile(self, canvas):
        self.canvas.delete("all")

        try:
            with open('loader.txt', 'r') as file_coordinates:
                for line in file_coordinates:
                    if line is '\n':
                        continue
                    if not line.startswith('#'):
                        a, b, d, e = line.split()
                        print(line)
                        self.arr.append([a, int(b), int(d), int(e)])
                self.arrOriginal = copy.deepcopy(self.arr)
                print(self.arr)
                self.centernew = self.arr[0][2]
                self.centernewy = self.arr[0][3]

                self.drawfromarr(self.canvas)

        # Exception with openning the file
        except IOError:
            print('Error trying to open txt file')
        # Exception of the values in the file
        except:
            print('Error in values in the TXT file - '
                  'Only those formats can works n n n n  OR r n n n'
                  ' (n is an numeric value)')

    ######################################Assaf please add
    def drawfromfilefiledialog(self):
        self.canvas.delete("all")
        self.arr = []
        file_path = filedialog.askopenfilename()
        if '.txt' not in file_path:
            print('File Type Error')
            self.StartOver()

        try:
            with open(file_path, 'r') as file_coordinates:
                for line in file_coordinates:
                    if line is '\n':
                        continue
                    if not line.startswith('#'):
                        a, b, d, e = line.split()
                        print(line)
                        self.arr.append([a, int(b), int(d), int(e)])
                self.arrOriginal = copy.deepcopy(self.arr)
                print(self.arr)
                self.centernew = self.arr[0][2]
                self.centernewy = self.arr[0][3]

                self.drawfromarr(self.canvas)

        # Exception with openning the file
        except IOError:
            print('Error trying to open txt file')
        # Exception caused by the values in the file
        except:
            print('Error in values at the TXT file - '
                  'Only those formats can works n n n n  OR r n n n'
                  ' (n is an numeric value)')

    ######################################Assaf please add
    def drawfromarr(self, canvas):
        self.canvas.delete("all")
        try:
            if self.movetocenter:
                self.moveTocenter()
            print(self.arr)
            for vector in self.arr:

                a, b, d, e = vector
                print(a, b, d, e)

                if a != 'r':
                    x1 = int(a) * self.t
                    y1 = int(b) * self.t
                    x2 = int(d) * self.t
                    y2 = int(e) * self.t
                    line = canvas.create_line(
                        (x1, y1, x2, y2),
                        fill="blue")
                else:
                    r = int(b) * self.t
                    x = int(d) * self.t
                    y = int(e) * self.t
                    canvas.create_circle(x, y, r,
                                         fill="white", outline="blue")
                if self.movetocenter:
                    canvas.create_circle(self.arr[0][2]+self.w/4, self.arr[0][3]+self.h/4-10, 2,
                                         fill="red", outline="red")

        except:
            print('Error while drawing this shape, you reached maximun value')
            
    ######################################Assaf please add
    def erase(self):
        self.canvas.delete("all")

    distance = 0
    enterinput = 0, 0
    leaveinput = 0, 0
    disx = 0
    disy = 0
    def Enter(self,event):
        self.enterinput = event.x, event.y
        print('---------Mouse event noticed')
        print("Enter at", event.x, event.y)

    def Leave(self, event):
        self.leaveinput = event.x, event.y
        self.distance = math.floor(math.sqrt((
                                            self.leaveinput[0] - self.enterinput[0])**2 +(self.leaveinput[1] - self.enterinput[1])**2))
        if self.xshearing or self.yshearing:
            self.disx = math.floor((self.leaveinput[1] - self.enterinput[1])/(self.leaveinput[0] - self.enterinput[0]))
            self.disy = math.floor((self.leaveinput[1] - self.enterinput[1])/(self.leaveinput[0] - self.enterinput[0]))
            self.shearing()
        print("Leave at", event.x, event.y, 'Distance', self.distance)
        print('Dis-X', self.disx, 'Dis-Y', self.disy)
        print('---------Mouse event ended')


    def __init__(self):
        ##Canvas, buttons & font general settings
        fontstyle = tkFont.Font(family='Courier', size=14)
        Tk.Canvas.create_circle_arc = self._create_circle_arc
        self.canvas.bind("<Button-1>", self.Enter)
        self.canvas.bind("<ButtonRelease-1>", self.Leave)

        ##### Buttons for transformations 
        ## Erase button 
        erasebtn = Button(self.frame, text=' Erase ', command=self.erase, font=fontstyle)
        erasebtn.pack(side='left',padx=2)

        ## Load from txt file button
        erasebtn = Button(self.frame, text=' Load from txt ', command=self.StartOver)
        erasebtn.pack(side='left',padx=2)
        label = Label(self.frame, text=" ", bg=self.color).pack(side='left' ,padx=2)
        self.frame.pack(fill='x')

        ## Scale button
        scalebtn = Button(self.frame, text='Scale', command=self.scale)
        scalebtn.pack(side='left', padx=2)
        validation = self.frame.register(self.validate)
        escale = Entry(self.frame, width=4, validate="key", validatecommand=(validation, '%S'))
        escale.insert(1, "2")
        escale.pack(side='left')
        self.scaleox = escale
        label = Label(self.frame, text=" ", bg=self.color).pack(side='left', padx=4)

        ## Rotate button
        scalebtn2 = Button(self.frame, text='Rotate', command=self.rotate)
        scalebtn2.pack(side='left', padx=2)
        validationm = self.frame.register(self.validatenum)
        escale2 = Entry(self.frame, width=4, validate="key", validatecommand=(validationm, '%S'))
        escale2.insert(1, "2")
        escale2.pack(side='left')
        self.scaleox2 = escale2
        label = Label(self.frame, text=" ", bg=self.color).pack(side='left',padx=2)
        
        ## Translate button
        scalebtn3 = Button(self.frame, text='Translate', command=self.translation)
        scalebtn3.pack(side='left', padx=2)

        ## Field for X        
        labelx = Label(self.frame, text="x").pack(side='left',padx=2)
        validationm = self.frame.register(self.validatenum)
        escalex = Entry(self.frame, width=2, validate="key", validatecommand=(validationm, '%S'))
        escalex.insert(1, "40")
        escalex.pack(side='left',padx=2)
        self.inputx = escalex
        
        ## Field for X
        labely = Label(self.frame, text="y").pack(side='left',padx=2)
        validationm = self.frame.register(self.validatenum)
        escaley = Entry(self.frame, width=2, validate="key", validatecommand=(validationm, '%S'))
        escaley.insert(1, "40")
        escaley.pack(side='left')
        self.inputy = escaley
        label = Label(self.frame, text=" ", bg=self.color).pack(side='left', padx=2)
        
        ## Mirror auto button
        scalebtn = Button(self.frame, text='Mirror-Auto', command=self.mirror)
        scalebtn.pack(side='left', padx=2)
        validation = self.frame.register(self.validate)
        label = Label(self.frame, text=" ", bg=self.color).pack(side='left', padx=2)
        
        ## Shear X button
        scalebtn = Button(self.frame, text='Shear X', command=self.shearingx)
        scalebtn.pack(side='left', padx=2)

        ## Shear Y button
        scalebtn = Button(self.frame, text='Shear Y', command=self.shearingy)
        scalebtn.pack(side='left', padx=2)

        ## Transperant background image
        background_image = Tk.PhotoImage(file="bg.png")
        # Stretching the canvas to window(root) size
        self.canvas.pack(fill=Tk.BOTH, expand=1)  
        image = self.canvas.create_image(0, 0, anchor=Tk.NW, image=background_image)
        self.drawfromfile(self.canvas)
        self.framefoot = Frame(self.root, bg=self.color, height=80)
        self.framefoot.pack(fill='x')

        ## Static scale button
        scalebtn = Button(self.framefoot, text='Static Scale', command=self.staticscale)
        scalebtn.pack(side='left', padx=5, pady=40)

        ## Static mirror button
        scalebtn = Button(self.framefoot, text='Static Mirror', command=self.staticmirror)
        scalebtn.pack(side='left', padx=5, pady=40)

        ## Static rotate button
        scalebtn = Button(self.framefoot, text='Static Rotate', command=self.staticrotate)
        scalebtn.pack(side='left', padx=5, pady=40)

        ## Load costum .txt file button
        scalebtn = Button(self.framefoot, text='Load costum .txt file', command=self.drawfromfilefiledialog)
        scalebtn.pack(side='left', padx=5, pady=40)

        ## Window (root)
        self.root.wm_geometry(str(self.w) + "x" + str(self.h))
        self.root.title('CS Graphics Ex2 - by Asaf L & Alon A ')
        self.root.mainloop()


main = my2dtransfomations()
