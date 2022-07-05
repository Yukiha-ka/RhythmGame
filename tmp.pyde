string1_y = 640
bpm = 120

def drawline():
    stroke(140)
    strokeWeight(20)
    line(0,520,400,520)

def setup():
    background(0)
    size(360,640)
    frameRate(60)
    drawline()

def draw():
    background(0)
    noStroke()
    fill(255)
    string1_y += (bpm/10)
    ellipse(180,string1_y,50,50)
