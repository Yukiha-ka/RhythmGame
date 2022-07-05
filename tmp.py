string_y = 0
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
    textSize(30)
   

def draw():
    global string_y,bpm,tx
    background(0)
    drawline()
    noStroke()
    fill(255)
    string_y +=  (bpm/5)
    ellipse(180,string_y,50,50)
    text(tx,180,520)
    
def  mouseClicked():
    global string_y,tx
    if 500 <= string_y <= 520:
        tx = "Perfect"
         

    else:
        textSize(30)
        tx = "False"
    
