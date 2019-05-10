Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> import tkinter
>>> import pygame
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
>>> for x in range(1,61):
	print(x)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
>>> for x in range(1,61):
	print(x)
	sleep(1)

	
1
Traceback (most recent call last):
  File "<pyshell#8>", line 3, in <module>
    sleep(1)
NameError: name 'sleep' is not defined
>>>  for x in range(1,61):
	print(x)
	time.sleep(1)
	
SyntaxError: unexpected indent
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
KeyboardInterrupt
>>> for x in range (1,61):
	print (x)
	time.sleep(1)

	
1
Traceback (most recent call last):
  File "<pyshell#24>", line 3, in <module>
    time.sleep(1)
NameError: name 'time' is not defined
>>> 
KeyboardInterrupt
>>> import time
>>> for x in range (1,61):
	print (x)
	time.sleep(1)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
Traceback (most recent call last):
  File "<pyshell#27>", line 3, in <module>
    time.sleep(1)
KeyboardInterrupt
>>> import os
>>> while True:
	t=time.localtime()
	os.system("cls")
	print (str(t[3])+":"+str(t[4])+":"+str(t[5]))
	time.sleep(0.5)

	
0
7:53:2
0
7:53:3
0
7:53:4
0
7:53:5
0
7:53:5
0
7:53:6
0
7:53:7
0
7:53:7
0
7:53:8
0
7:53:8
0
7:53:9
0
7:53:10
0
7:53:10
0
7:53:11
0
7:53:11
0
7:53:12
0
7:53:12
0
7:53:13
0
7:53:14
0
7:53:14
0
7:53:15
0
7:53:16
0
7:53:16
0
7:53:17
0
7:53:17
0
7:53:18
0
7:53:19
0
7:53:19
0
7:53:20
0
7:53:20
0
7:53:21
0
7:53:22
0
7:53:22
0
7:53:23
0
7:53:23
0
7:53:24
0
7:53:25
0
7:53:25
0
7:53:26
0
7:53:26
0
7:53:27
0
7:53:28
0
7:53:28
0
7:53:29
0
7:53:29
0
7:53:30
0
7:53:31
0
7:53:31
0
7:53:32
0
7:53:32
0
7:53:33
0
7:53:34
0
7:53:34
0
7:53:35
0
7:53:35
0
7:53:36
0
7:53:37
0
7:53:37
0
7:53:38
0
7:53:39
0
7:53:39
0
7:53:40
0
7:53:40
0
7:53:41
0
7:53:42
0
7:53:42
0
7:53:43
0
7:53:43
0
7:53:44
0
7:53:45
0
7:53:45
0
7:53:46
0
7:53:46
0
7:53:47
0
7:53:48
0
7:53:48
0
7:53:49
0
7:53:49
0
7:53:50
0
7:53:51
0
7:53:51
0
7:53:52
0
7:53:52
0Traceback (most recent call last):
  File "<pyshell#34>", line 3, in <module>
    os.system("cls")
KeyboardInterrupt
>>> while True:
	t=time.localtime()
	os.system("cls")
	print (str(t[3])+":"+str(t[4])+":"+str(t[5]))
	time.sleep(1)

	
0
7:54:22
0
7:54:23
0
7:54:24
0
7:54:25
0
7:54:26
0
7:54:27
0
7:54:29
0
7:54:30
0
7:54:31
0
7:54:32
0
7:54:33
0
7:54:34
0
7:54:35
0
7:54:36
0
7:54:37
0
7:54:39
0
7:54:40
0
7:54:41
0
7:54:42
0
7:54:43
0
7:54:44
0
7:54:45
0
7:54:46
0
7:54:47
0
7:54:49
0
7:54:50
0
7:54:51
0
7:54:52
0
7:54:53
0
7:54:54
0
7:54:55
0
7:54:56
0
7:54:57
0
7:54:59
0
7:55:0
0
7:55:1
0
7:55:2
0
7:55:3
0
7:55:4
0
7:55:5
0
7:55:6
0
7:55:7
0
7:55:8
0
7:55:10
0
7:55:11
0
7:55:12
0
7:55:13
0
7:55:14
0
7:55:15
0
7:55:16
0
7:55:17
0
7:55:18
0
7:55:20
0
7:55:21
0
7:55:22
0
7:55:23
0
7:55:24
0
7:55:25
0
7:55:26
0
7:55:27
0
7:55:28
0
7:55:30
0
7:55:31
0
7:55:32
0
7:55:33
0
7:55:34
0
7:55:35
0
7:55:36
0
7:55:37
0
7:55:41
0
7:55:42
0
7:55:43
0
7:55:44
0
7:55:46
0
7:55:47
0
7:55:48
0
7:55:49
0
7:55:50
0
7:55:51
0
7:55:52
0
7:55:53
0
7:55:55
0
7:55:56
0
7:55:57
0
7:55:58
0
7:55:59
0
7:56:0
0
7:56:1
0
7:56:2
0
7:56:3
0
7:56:5
0
7:56:6
0
7:56:7
0
7:56:8
0
7:56:9
0
7:56:10
0
7:56:11
0
7:56:12
0
7:56:13
0
7:56:14
0
7:56:16
0
7:56:17
0
7:56:18
0
7:56:19
0
7:56:20
0
7:56:21
0
7:56:22
0
7:56:23
0
7:56:24
0
7:56:26
0
7:56:27
0
7:56:28
0
7:56:29
0
7:56:30
0
7:56:31
0
7:56:32
0
7:56:33
0
7:56:35
0
7:56:36
0
7:56:37
0
7:56:38
0
7:56:39
0
7:56:40
0
7:56:41
0
7:56:42
0
7:56:43
0
7:56:44
0
7:56:46
0
7:56:47
0
7:56:48
0
7:56:49
0
7:56:50
0
7:56:51
0
7:56:52
0
7:56:53
0
7:56:54
0
7:56:56
0
7:56:57
0
7:56:58
0
7:56:59
Traceback (most recent call last):
  File "<pyshell#36>", line 5, in <module>
    time.sleep(1)
KeyboardInterrupt
>>> t=turtle.Pen()
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(50)
>>> turtle.getscreen._root.mainloop()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    turtle.getscreen._root.mainloop()
AttributeError: 'function' object has no attribute '_root'
>>> turtle.getscreen()._root.mainloop()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    turtle.getscreen()._root.mainloop()
  File "C:\Users\ESFOT\AppData\Local\Programs\Python\Python37\lib\tkinter\__init__.py", line 1280, in mainloop
    self.tk.mainloop(n)
KeyboardInterrupt


>>> t.reset()
>>> for x in range(1,9):
	t.forward(100)
	t.left(225)

	
>>> t.reset()
>>> for x in range (1,38):
	t.forward(100)
	t.left(175)

	
>>> t.reset()
>>> def micuadrado(size):
	for x in range(1,5):
		t.forward(size)
		t.left(90)

		
>>> micuadrado(100)
>>> t.reset()
>>> def estrella(n)
SyntaxError: invalid syntax
>>> def estrella(n):
        ang=(90/n)+90
	for x in range(1,n):
		t.forward(90)
		tleft(ang)
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def estrella(n):
	ang=(90/n)+90
	for x in range(1,n):
		t.forward(90)
		t.left(ang)

		
>>> estrella(5)
>>> t.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x00000000039796A0>>
>>> estrella(4)
>>> t.reset()
>>> estrella(8)
>>> cls
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> t.reset()
>>> for x in range(1,2):
	t.forward(size)
	t.left(90)

t.forward(20)
SyntaxError: invalid syntax
>>> for x in range(1,2):
	t.forward(size)
	t.left(90)
    t.forward(20)
    
SyntaxError: unindent does not match any outer indentation level
>>> for x in range(1,2):
	t.forward(size)
	t.left(90)


Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    t.forward(size)
NameError: name 'size' is not defined
>>> for x in range(1,2):
	t.forward(70)
	t.left(90)

	
>>> for x in range(1,3):
	t.forward(90)
	t.left(90)

	
>>> from tkinter import *
>>> tk=Tk()
>>> canvas=Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> my_image=PhotoImage(file="ball.gif")
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    my_image=PhotoImage(file="ball.gif")
  File "C:\Users\ESFOT\AppData\Local\Programs\Python\Python37\lib\tkinter\__init__.py", line 3542, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\ESFOT\AppData\Local\Programs\Python\Python37\lib\tkinter\__init__.py", line 3486, in __init__
    raise RuntimeError('Too early to create image')
RuntimeError: Too early to create image
>>> 
