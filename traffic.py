from re import S
from threading import Timer, Thread, Event
from datetime import datetime
from datetime import datetime, timedelta

class PT():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
         self.thread.start()
    

def printer():
    tempo = datetime.today()
    h,m,s = tempo.hour, tempo.minute, tempo.second
    print(f"{h}:{m}:{s}")
    south=s + 45
    north=s + 30
    west=s+ 15
    east=s+ 0
    if south % 60 <=15 and north % 60 >=15 and east % 60>=15 and west % 60 >=15:
        print(f"south green,east {east % 60}s stop ,west {west % 60}s stop  and north {north % 60}s stop ")
    elif south % 60 >=15 and north % 60 <=15 and east % 60>=15 and west % 60>=15:
        print(f"north green ,east {east % 60}s stop ,west {west % 60}s stop  and south {south % 60}s stop ")
    elif south >=15 and north % 60 >=15 and east % 60>=15 and west % 60<=15:
        print(f"west green ,east {east % 60}s stop ,south {south % 60}s stop  and north {north % 60}s stop ")
    else:
        print(f"east green ,south {south % 60}s stop ,west {west % 60}s stop  and north {north % 60}s stop ")



t = PT(15, printer)
t.start()
# printer()