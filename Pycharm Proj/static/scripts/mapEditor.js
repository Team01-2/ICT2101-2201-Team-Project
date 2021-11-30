var canvas = document.getElementById("canvas");
var ctx = document.getElementById('canvas').getContext("2d");
canvas.addEventListener('click', handleClick);

var canvas2 = document.getElementById("canvas2");
var ctx2 = document.getElementById('canvas2').getContext("2d");
canvas2.addEventListener('click', handleClick2);

var selection = [0, 0, 0];
var selected = 0; // 0 = obstacle, 1 = finishing grid, 2 = car, default is 0

window.addEventListener("keydown", function (e) {
    if (e.keyCode >= 37 && e.keyCode <= 40) {
        keysDown[e.keyCode] = true;
    }
});
window.addEventListener("keyup", function (e) {
    if (e.keyCode >= 37 && e.keyCode <= 40) {
        keysDown[e.keyCode] = false;
    }
});
requestAnimationFrame(drawGame);

var tileW = 100, tileH = 100;
var mapW = 5, mapH = 5;
var currentSecond = 0, frameCount = 0, framesLastSecond = 0, lastFrameTime = 0;

var keysDown = {
    37: false,
    38: false,
    39: false,
    40: false
};

var player = new Character();
var finish = [4, 4]; // finish point

// map design 0 = obstacle, 1 = no obstacle, 2 = player, 3 = finish
var gameMap = [
    1, 1, 1, 0, 0,
    1, 1, 1, 1, 0,
    1, 1, 1, 0, 0,
    1, 1, 1, 1, 1,
    0, 1, 0, 1, 0
];

gameMap[finish[0] + finish[1] * 5] = 3;

function Character()
{
    this.tileFrom = [1, 1];
    this.tileTo = [0, 0];
    this.timeMoved = 0;
    this.dimensions = [90, 90];
    this.position = [5, 5];
    this.delayMove = 700;
}
gameMap[player.tileTo[0] + player.tileTo[1] * 5] = 2;

Character.prototype.placeAt = function (x, y)
{
    this.tileFrom = [x, y];
    this.tileTo = [x, y];
    this.position = [((tileW * x) + ((tileW - this.dimensions[0]) / 2)), ((tileH * y) + ((tileH - this.dimensions[1]) / 2))];
};
Character.prototype.processMovement = function (t)
{
    if (this.tileFrom[0] == this.tileTo[0] && this.tileFrom[1] == this.tileTo[1])
    {
        return false;
    }
    if ((t - this.timeMoved) >= this.delayMove)
    {
        this.placeAt(this.tileTo[0], this.tileTo[1]);
    } else
    {
        this.position[0] = (this.tileFrom[0] * tileW) + ((tileW - this.dimensions[0]) / 2);
        this.position[1] = (this.tileFrom[1] * tileH) + ((tileH - this.dimensions[1]) / 2);

        if (this.tileTo[0] != this.tileFrom[0])
        {
            var diff = (tileW / this.delayMove) * (t - this.timeMoved);
            this.position[0] += (this.tileTo[0] < this.tileFrom[0] ? 0 - diff : diff);
        }
        if (this.tileTo[1] != this.tileFrom[1])
        {
            var diff = (tileH / this.delayMove) * (t - this.timeMoved);
            this.position[1] += (this.tileTo[1] < this.tileFrom[1] ? 0 - diff : diff);
        }

        this.position[0] = Math.round(this.position[0]);
        this.position[1] = Math.round(this.position[1]);
    }
    return true;
};

function toIndex(x, y)
{
    return((y * mapW) + x);
}

function drawGame()
{
    if (ctx == null)
    {
        return;
    }

    var currentFrameTime = Date.now();
    var timeElapsed = currentFrameTime - lastFrameTime;

    var sec = Math.floor(Date.now() / 1000);

    if (sec != currentSecond)
    {
        currentSecond = sec;
        framesLastSecond = frameCount;
        frameCount = 1;
    } else
    {
        frameCount++;
    }

    if (!player.processMovement(currentFrameTime))
    {
        if (keysDown[38] && player.tileFrom[1] > 0 && gameMap[toIndex(player.tileFrom[0], player.tileFrom[1] - 1)] == 1)
        {
            player.tileTo[1] -= 1;
        } else if (keysDown[40] && player.tileFrom[1] < (mapH - 1) && gameMap[toIndex(player.tileFrom[0], player.tileFrom[1] + 1)] == 1)
        {
            player.tileTo[1] += 1;
        } else if (keysDown[37] && player.tileFrom[0] > 0 && gameMap[toIndex(player.tileFrom[0] - 1, player.tileFrom[1])] == 1)
        {
            player.tileTo[0] -= 1;
        } else if (keysDown[39] && player.tileFrom[0] < (mapW - 1) && gameMap[toIndex(player.tileFrom[0] + 1, player.tileFrom[1])] == 1)
        {
            player.tileTo[0] += 1;
        } else if (keysDown[38] && player.tileFrom[1] > 0 && gameMap[toIndex(player.tileFrom[0], player.tileFrom[1] - 1)] == 3)
        {
            player.tileTo[1] -= 1;
        }  else if (keysDown[40] && player.tileFrom[1] < (mapH - 1) && gameMap[toIndex(player.tileFrom[0], player.tileFrom[1] + 1)] == 3)
        {
            player.tileTo[1] += 1;
        } else if (keysDown[37] && player.tileFrom[0] > 0 && gameMap[toIndex(player.tileFrom[0] - 1, player.tileFrom[1])] == 3)
        {
            player.tileTo[0] -= 1;
        } else if (keysDown[39] && player.tileFrom[0] < (mapW - 1) && gameMap[toIndex(player.tileFrom[0] + 1, player.tileFrom[1])] == 3)
        {
            player.tileTo[0] += 1;
        }
        if (player.tileFrom[0] != player.tileTo[0] || player.tileFrom[1] != player.tileTo[1])
        {
            player.timeMoved = currentFrameTime;
        }
        console.log(gameMap)
    }

    for (var y = 0; y < mapH; ++y)
    {
        for (var x = 0; x < mapW; ++x)
        {
            switch (gameMap[((y * mapW) + x)])
            {
                case 0:
                    ctx.fillStyle = "red";
                    break;
                case 3:
                    finish = [x, y];
                    ctx.fillStyle = "green";
                    break;
                default:
                    ctx.fillStyle = "#ccffcc";
            }

            ctx.fillRect(x * tileW, y * tileH, tileW, tileH);
        }
    }
    var imageUp = document.getElementById('carUp');
    var flag = document.getElementById('flag');

    ctx.drawImage(imageUp, player.position[0], player.position[1], player.dimensions[0], player.dimensions[1]);

    ctx.drawImage(flag, finish[0] * tileW, finish[1] * tileH, tileW, tileH);

    ctx.fillStyle = "#ff00ff";
    ctx.fillText("FPS: " + framesLastSecond, 10, 20);

    lastFrameTime = currentFrameTime;
    requestAnimationFrame(drawGame);
}

function getMousePos(c, evt)
{
    var rect = c.getBoundingClientRect();
    return{
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}

function handleClick(e)
{
    var pos = getMousePos(canvas, e);
    posx = pos.x;
    posy = pos.y;
    draw2(posx, posy);
}

function getMousePos2(c, evt)
{
    var rect = c.getBoundingClientRect();
    return{
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}

function handleClick2(e)
{
    var pos = getMousePos(canvas2, e);
    posx = pos.x;
    posy = pos.y;
    draw3(posx, posy);
}

function draw()
{
    for (var x = 0; x < 8; x++)
    {
        for (var y = 0; y < 8; y++)
        {
            if (gameMap[x + y * 8] == 1)
            {
                ctx.fillStyle = "black";
                ctx.fillRect(100 * x, 100 * y, 100, 100);
            } else
            {
                ctx.fillStyle = "white";
                ctx.fillRect(100 * x, 100 * y, 100, 100);
            }
        }
    }
    var imageUp = document.getElementById('carUp');
    var flag = document.getElementById('flag');
    for (var x = 0; x < 3; x++)
    {
        var y = 0; // only using row 1 for canvas 2
        if (x == 0)
        {
            ctx2.fillStyle = "red";
            ctx2.fillRect(60 * x, 60 * y, 60, 60);
        } else if (x == 1)
        {
            ctx2.drawImage(flag, 60 * x, 60 * y, 60, 60);
        } else
        {
            ctx2.drawImage(imageUp, 60 * x, 60 * y, 60, 60);
        }
    }
}

function draw2(xCordinate, yCordinate)
{
    var xCord = Math.floor(xCordinate / 100);
    var yCord = Math.floor(yCordinate / 100);


    if (gameMap[xCord + yCord * 5] == 1)
    {
        if (selected == 0)
        {
            gameMap[xCord + yCord * 5] = 0;

        } else if (selected == 1)
        {
            gameMap[finish[0] + finish[1] * 5] = 1;
            finish[0] = xCord;
            finish[1] = yCord;
            gameMap[finish[0] + finish[1] * 5] = 3;

        } else if (selected == 2)
        {
            gameMap[player.tileTo[0] + player.tileTo[1] * 5] = 1;
            player.tileTo[0] = xCord;
            player.tileTo[1] = yCord;
            gameMap[player.tileTo[0] + player.tileTo[1] * 5] = 2;
        }
    } else if(gameMap[xCord + yCord * 5] == 0)
    {
        gameMap[xCord + yCord * 5] = 1;
        ctx.fillStyle = "white";
    }
    ctx.fillRect(100 * xCord, 100 * yCord, 100, 100);
    return;
}

function draw3(xCordinate, yCordinate)
{
    var xCord = Math.floor(xCordinate / 60);
    selected = xCord;
    var yCord = Math.floor(yCordinate / 60);
    var y = 0; // row 1 = 0

    for (var x = 0; x < 3; x++)
    {
        if (x != xCord)
        {
            selection[x] = 0;
            ctx2.lineWidth = 5;
            ctx2.strokeStyle = 'transparent';
            ctx2.strokeRect(60 * x, 60 * y, 60, 60);
        } else
        {
            selection[x] = 1;

            ctx2.lineWidth = 5;
            ctx2.strokeStyle = 'black';
            ctx2.strokeRect(60 * x, 60 * y, 60, 60);
        }
    }

    return;
}

function clearCanvas(){
    var canvas = document.getElementById("canvas");
    var context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
}



