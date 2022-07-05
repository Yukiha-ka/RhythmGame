string1_y = 0
bpm = 120

def drawline():
    stroke(140)
    strokeWeight(20)
    line(0,520,400,520)

def setup():
    background(0)
    size(360,640)
    frameRate(60)


def draw():
    global string1_y,bpm
    background(0)
    drawline()
    noStroke()
    fill(255)
    string1_y += (bpm/70)
    ellipse(180,string1_y,50,50)
