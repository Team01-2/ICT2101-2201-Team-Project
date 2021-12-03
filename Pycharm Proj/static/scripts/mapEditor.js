var canvas = document.getElementById("canvas");
var ctx = document.getElementById('canvas').getContext("2d");
canvas.addEventListener('click', handleClick);

var canvas2 = document.getElementById("canvas2");
var ctx2 = document.getElementById('canvas2').getContext("2d");
canvas2.addEventListener('click', handleClick2);

var canvas3 = document.getElementById("canvas3");
var ctx3 = document.getElementById('canvas3').getContext("2d");

var canvas4 = document.getElementById("canvas4");
var ctx4 = document.getElementById('canvas4').getContext("2d");

var canvas5 = document.getElementById("canvas5");
var ctx5 = document.getElementById('canvas5').getContext("2d");

var modal1 = document.getElementById("popoutSection1"); // pop up modal for no commands to run

var availableMap = 3;
var mapList = [0, 0, 0];

var selection = [0, 0, 0];
var selected = 0; // 0 = obstacle, 1 = finishing grid, 2 = car, default is 0

window.onload = function()
{
    received = document.getElementById('mapData').innerHTML;
    const obj = JSON.parse(received);
    console.log(obj.map1)
    console.log(obj.start1)
    console.log(obj.end1)
    if(obj.map1.length != 0)
    {
        availableMap -= 1;
        mapList[0] = 1;
        drawSaveMap(ctx3, obj.map1, obj.start1, obj.end1);
    }
    if(obj.map2.length != 0)
    {
        availableMap -= 1;
        mapList[1] = 1;
        drawSaveMap(ctx4, obj.map2, obj.start2, obj.end2);
    }
    if(obj.map3.length != 0)
    {
        availableMap -= 1;
        mapList[2] = 1;
        drawSaveMap(ctx5, obj.map3, obj.start3, obj.end3);
    }
    draw();
    requestAnimationFrame(drawGame);
}


var tileW = 100, tileH = 100;
var mapW = 5, mapH = 5;
var currentSecond = 0, frameCount = 0, framesLastSecond = 0, lastFrameTime = 0;

var player = new Character();
var finish = [0, 0]; // finish point

// map design 0 = obstacle, 1 = no obstacle, 2 = player, 3 = finish
var gameMap = [
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1
];

gameMap[finish[0] + finish[1] * 5] = 3;

function Character()
{
    this.tileFrom = [4, 4];
    this.tileTo = [4, 4];
    this.timeMoved = 0;
    this.dimensions = [90, 90];
    this.position = [405, 405];
    this.delayMove = 700;
}
gameMap[player.tileTo[0] + player.tileTo[1] * 5] = 2;

Character.prototype.placeAt = function (x, y)
{
    this.tileFrom = [x, y];
    this.tileTo = [x, y];
    this.position = [((tileW * x) + ((tileW - this.dimensions[0]) / 2)), ((tileH * y) + ((tileH - this.dimensions[1]) / 2))];
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


    for (var y = 0; y < mapH; ++y)
    {
        for (var x = 0; x < mapW; ++x)
        {
            switch (gameMap[((y * mapW) + x)])
            {
                case 0:
                    ctx.fillStyle = "#000001";
                    break;
                case 3:
                    finish = [x, y];
                    ctx.fillStyle = "green";
                    break;
                default:
                    ctx.fillStyle = "#EEEEEE";
            }

            ctx.fillRect(x * tileW, y * tileH, tileW, tileH);
        }
    }
    var imageUp = document.getElementById('carUp');
    var flag = document.getElementById('flag');

    ctx.drawImage(imageUp, player.position[0], player.position[1], player.dimensions[0], player.dimensions[1]);

    ctx.drawImage(flag, finish[0] * tileW, finish[1] * tileH, tileW, tileH);

    lastFrameTime = currentFrameTime;
    //requestAnimationFrame(drawGame);
}

function drawSaveMap(canvasType, mapList, startPoint, endPoint)
{
    if (canvasType == null)
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


    for (var y = 0; y < mapH; ++y)
    {
        for (var x = 0; x < mapW; ++x)
        {
            switch (mapList[((y * mapW) + x)])
            {
                case 0:
                    canvasType.fillStyle = "#000001";
                    break;
                case 3:
                    canvasType.fillStyle = "green";
                    break;
                default:
                    canvasType.fillStyle = "#EEEEEE";
            }

            canvasType.fillRect(x * tileW, y * tileH, tileW, tileH);
        }
    }
    var imageUp = document.getElementById('carUp');
    var flag = document.getElementById('flag');

    canvasType.drawImage(imageUp, startPoint[0] * tileW + 5, startPoint[1] * tileH + 5, player.dimensions[0], player.dimensions[1]);

    canvasType.drawImage(flag, endPoint[0] * tileW, endPoint[1] * tileH, tileW, tileH);


    lastFrameTime = currentFrameTime;
    //requestAnimationFrame(drawGame);
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
    requestAnimationFrame(drawGame);
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
    for (var x = 0; x < 5; x++)
    {
        for (var y = 0; y < 5; y++)
        {
            if (gameMap[x + y * 5] == 1)
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
            ctx2.fillStyle = "#000001";
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
            player.position[0] = xCord * tileW + 5;
            player.position[1] = yCord * tileH + 5;
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
    for(var i = 0; i < mapW * mapH; i++)
    {
        if(gameMap[i] == 0)
        {
            gameMap[i] = 1;
        }
    }
    drawGame();
}

function saveMap(){
    if(availableMap != 0)
    {
        for(var i = 0; i < 3; i++)
        {
            if(mapList[i] == 0)
            {
                save(i+1);
                if(i == 0)
                {
                    drawSaveMap(ctx3, gameMap, player.tileTo, finish);
                }
                else if(i == 1)
                {
                    drawSaveMap(ctx4, gameMap, player.tileTo, finish);
                }
                else if(i == 2)
                {
                    drawSaveMap(ctx5, gameMap, player.tileTo, finish);
                }
                mapList[i] = 1;
                availableMap -= 1;
                break;
            }
        }
    }
    else
    {
        document.getElementById('popout-text').innerHTML = "Maximum limit has reached!";
        modal1.style.display = "block"; // can trigger restart menu
        return;
    }
    console.log(gameMap);
    console.log(finish);
    console.log(player.tileTo[0]);
    console.log(player.tileTo[1]);
}

function save(index){
    mapName = document.getElementById('mapName').value;
    console.log(mapName)
    let mapData = {
        'name': mapName,
        'map': gameMap,
        'start': player.tileTo,
        'end': finish,
        'index': index
    }
    const request = new XMLHttpRequest();
    request.open('POST', `/saveMap/${JSON.stringify(mapData)}`)
    request.onload = () => {
        const flaskMessage = request.responseText;
        console.log(flaskMessage);
    }
    request.send();
}

//Delete map function
function deleteMap(mapIndex)
{
    if(mapList[mapIndex] == 1)
    {
        mapList[mapIndex] = 0;
        availableMap += 1;
        if(mapIndex == 0)
        {
            ctx3.clearRect(0, 0, canvas.width, canvas.height);
        }
        else if(mapIndex == 1)
        {
            ctx4.clearRect(0, 0, canvas.width, canvas.height);
        }
        else if(mapIndex == 2)
        {
            ctx5.clearRect(0, 0, canvas.width, canvas.height);
        }
        deleteFromDatabase(mapIndex+1);
    }
}

function deleteFromDatabase(index){
    let mapData = {
        'index': index,
    }
    const request = new XMLHttpRequest();
    request.open('POST', `/deleteMap/${JSON.stringify(mapData)}`)
    request.onload = () => {
        const flaskMessage = request.responseText;
        console.log(flaskMessage);
    }
    request.send();
}

function play(index){
    if(mapList[index] == 1)
    {
        selectMap(index);
    }
    window.location.replace("playScreen");
}

function selectMap(index){
    let Index = {
        'index': index + 1,
    }
    const request = new XMLHttpRequest();
    request.open('POST', `/selectIndex/${JSON.stringify(Index)}`)
    request.onload = () => {
        const flaskMessage = request.responseText;
        console.log(flaskMessage);
    }
    request.send();
}

// When the user clicks anywhere outside of the popout, close it
window.onclick = function (event) {
    if (event.target == modal1) {
        modal1.style.display = "none";
    }
}