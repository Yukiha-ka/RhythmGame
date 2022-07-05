string1_y = 0
bpm = 120
tx = ""

def drawline():
    stroke(140)
    strokeWeight(20)
    line(0,520,400,520)

def setup():
    background(0)
    size(360,640)
    frameRate(60)
   

def draw():
    global string1_y,bpm,tx
    background(0)
    drawline()
    noStroke()
    fill(255)
    string1_y +=  (bpm/70)
    ellipse(180,string1_y,50,50)
    print(tx)
    
def  mouseClicked():
    global tx
    if 500 <= string_y <= 520:
         #textSize(30)
         #fill(255,0,0)
         #text("Perfect!",180,520)
         tx = "Perfect"
    else:
        #textSize(30)
        #fill(255,0,0)
        #text("False!",180,520)
        tx = "False"
    
