var canvas = document.getElementById("gra");
var ctx = canvas.getContext('2d');

var kolumny = 10;
var wiersze = 10;

var moveRight = false;
var moveLeft = false;

function keyUp() {
    moveLeft = moveRight = false;
}

function keyDown(e) {
    if(e.keyCode == 65) { // a
        moveLeft = true;
        moveRight = false;
    }

    if(e.keyCode == 68) { // d
        moveLeft = false;
        moveRight = true;
    }
}

document.addEventListener('keydown', keyDown, false);
document.addEventListener('keyup', keyUp, false);



var zbite = [];
for(var i = 0; i<kolumny; i++){
    zbite[i] = [];
    for(var j=0; j<wiersze; j++){
        zbite[i][j] = 6;
    }
}




function Brick(bx, by) {
    this.x = bx;
    this.y = by;
}

function drawBrick(brick) {
    ctx.beginPath();
    ctx.rect(brick.x, brick.y, 60, 20);
    ctx.fillStyle = " #581845 ";
    ctx.fill();
    ctx.closePath();
}

var yp = 550;
var xp = 310;
function drawPad() {
    ctx.beginPath();
    ctx.rect(xp, yp, 100, 20);
    ctx.fillStyle = "black";
    ctx.fill();
    ctx.closePath();
}

var xb = 350;
var yb = 300;
function drawBall() {
    ctx.beginPath();
    ctx.arc(xb, yb, 20, 0, Math.PI * 2, false);
    ctx.fillStyle = "black";
    ctx.fill();
    ctx.closePath();
}



function movePad() {
    if(moveRight && xp + 80 < canvas.width) {
        xp += 6;
    }
    if(moveLeft && xp > 0) {
        xp -= 6;
    }
}

var kx = 4;
var ky = -4;
function moveBall() {

    if(xb + kx < 0 || xb + kx > canvas.width) {
        kx *= -1;
    }

    if(yb + ky < 0) {
        ky *= -1;
    }

    else if(yb +ky >= yp && xb > xp && xb < xp + 80) {
        ky *= -1;
    }

    xb += kx;
    yb += ky;


}


function zderzenie() {
    for(var i=0; i<kolumny; i++) {
        for(var j=0; j<wiersze;j++) {
            var brick = bricks[i][j];
            if(zbite[i][j] == 6) {
                if(xb > brick.x && xb < brick.x + 80) {
                    if(yb + 20 > brick.y && yb - 20 < brick.y+20) {
                        ky = -ky;
                        zbite[i][j] = 0;
                    }
                }
                if( yb > brick.y && yb < brick.y + 20) {
                    if(xb + 20 > brick.x &&  xb - 20 < brick.x + 80) {
                        kx = -kx;
                        zbite[i][j] = 0;
                    }
                }

            }
        }
    }
    //
}

var bricks = []
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    //brick = new Brick(10, 10);
    //drawBrick(brick);

    for(var i = 0; i <  kolumny; i++) {
        bricks[i] = []
        for(var j = 0; j < wiersze; j++) {
            x = i * 62 + 20;
            y = j * 22;
            bricks[i][j] = new Brick(x,y);
            if(zbite[i][j]==6){
                drawBrick(bricks[i][j]);
            }
        }


    }

    drawPad();
    drawBall();
    zderzenie();
    movePad();
    moveBall();
}

setInterval(draw, 10)