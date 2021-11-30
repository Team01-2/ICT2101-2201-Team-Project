var ctx = null;

var direction = "up";

var received = ""; //variable storing data received from robot car
var counter = 0; //counter to store current index of commandlist
var len = 0; //size of commandlist
var commandList = []; //command list for storing commands
var cmdNumber = 0; //increment and decrement when command added or removed to command list

var finish = [4, 4]; // finish point

var modal = document.getElementById("popoutSection"); //pop up modal for game over
var modal1 = document.getElementById("popoutSection1"); // pop up modal for no commands to run


// map design
var gameMap = [
    1, 1, 1, 0, 0,
    1, 1, 1, 1, 0,
    1, 1, 1, 0, 0,
    1, 1, 1, 1, 1,
    0, 1, 0, 1, 0
];


var tileW = 100, tileH = 100;
var mapW = 5, mapH = 5;
var currentSecond = 0, frameCount = 0, framesLastSecond = 0, lastFrameTime = 0;

gameMap[finish[0] + finish[1] * 5] = 3; // set grid x: 4, y: 4 to 3 for finishing

var moveLeft = false;
var moveUp = false;
var moveDown = false;
var moveRight = false;

var player = new Character(); // robot car on map

function Character()
{
    this.tileFrom = [0, 3];
    this.tileTo = [0, 3];
    this.timeMoved = 0;
    this.dimensions = [90, 90];
    this.position = [5, 305];
    this.delayMove = 700;
}
Character.prototype.placeAt = function(x, y)
{
    this.tileFrom = [x, y];
    this.tileTo = [x, y];
	this.position	= [((tileW*x)+((tileW-this.dimensions[0])/2)), ((tileH*y)+((tileH-this.dimensions[1])/2))];
};
Character.prototype.processMovement = function(t)
{
if(this.tileFrom[0]==this.tileTo[0] && this.tileFrom[1]==this.tileTo[1])
    {
        return false;
    }
	if((t-this.timeMoved)>=this.delayMove)
	{
		this.placeAt(this.tileTo[0], this.tileTo[1]);
	}
    else
    {
		this.position[0] = (this.tileFrom[0] * tileW) + ((tileW-this.dimensions[0])/2);
		this.position[1] = (this.tileFrom[1] * tileH) + ((tileH-this.dimensions[1])/2);

		if(this.tileTo[0] != this.tileFrom[0])
		{
			var diff = (tileW / this.delayMove) * (t-this.timeMoved);
			this.position[0]+= (this.tileTo[0]<this.tileFrom[0] ? 0 - diff : diff);
		}
		if(this.tileTo[1] != this.tileFrom[1])
		{
			var diff = (tileH / this.delayMove) * (t-this.timeMoved);
			this.position[1]+= (this.tileTo[1]<this.tileFrom[1] ? 0 - diff : diff);
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

// on windows load assign ctx
window.onload = function()
{
    ctx = document.getElementById('game').getContext("2d");
    requestAnimationFrame(drawGame);
    ctx.font = "bold 10pt sans-serif";
    for (var x = 0; x < mapW * mapH; x++) // for resetting map retrieved from mapeditor
    {
        if(gameMap[x] == 2)
        {
            gameMap[x] = 1;
        }
    }

};

    $.post("/receiveOK", "name").done(function(data) {
    $("#Result").text(data);
    console.log(data)
});

function getUrl(){
    var output;
    $.ajax({
        type: "POST",
        url: "/receiveOK",
        async: false,
    })
    .done(function(data){
        //console.log(data);
        document.getElementById('info').innerHTML = data;
        received = document.getElementById('info').innerHTML;
    });
    return output;
}

//drawing canvas constantly
function drawGame()
{
    getUrl(); //trigger receiveOK in flask
    console.log(received);
    if(received == "KO") // black line detected
    {
        removeAll();
        modal.style.display = "block"; // can trigger restart menu
        return;
    }
    else if(received == "GO" && counter < len)
    {
        command = commandList[counter];
        console.log("getting direction")
        //console.log(direction);
        //console.log(counter);
        if(command == "up")
        {
            moveUp = true;
            console.log("getting direction up")
        }
        else if(command == "down")
        {
            moveDown = true;
             console.log("getting direction down")
        }
        else if(command == "right")
        {
            moveRight = true;
             console.log("getting direction right")
        }
        else if(command == "left")
        {
            moveLeft = true;
             console.log("getting direction left")
        }

        counter++;
        received = "";
        document.getElementById('info').innerHTML = "";
    }
    else if(received == "TO")
    {
        removeAll();
        document.getElementById('popout-text').innerHTML = "Command sent unsuccessfully!";
        modal1.style.display = "block";
    }
    if(ctx==null)
    {
        return;
    }

	var currentFrameTime = Date.now();
	var timeElapsed = currentFrameTime - lastFrameTime;

    var sec = Math.floor(Date.now()/1000);

    if(sec!=currentSecond)
    {
        currentSecond = sec;
        framesLastSecond = frameCount;
        frameCount = 1;
    }
    else
    {
        frameCount++;
    }

    if(!player.processMovement(currentFrameTime))
    {
        if(moveUp) //if(keysDown[38] && player.tileFrom[1]>0 && gameMap[toIndex(player.tileFrom[0], player.tileFrom[1]-1)]==1)
        {
            console.log("it is uppp")
            if(direction == "up")
            {
                player.tileTo[1]-= 1;

            }
            else if(direction == "down")
            {
                player.tileTo[1]+= 1;

            }
            else if(direction == "left")
            {
                player.tileTo[0]-= 1;

            }
            else if(direction == "right")
            {
                player.tileTo[0]+= 1;

            }
            moveUp = false;
        }
		else if(moveDown) //else if(keysDown[40] && player.tileFrom[1]<(mapH-1) && gameMap[toIndex(player.tileFrom[0], player.tileFrom[1]+1)]==1)
		{
		    console.log("it is downnnn")
            if(direction == "up")
            {
                player.tileTo[1]+= 1;

            }
            else if(direction == "down")
            {
                player.tileTo[1]-= 1;

            }
            else if(direction == "left")
            {
                player.tileTo[0]+= 1;

            }
            else if(direction == "right")
            {
                player.tileTo[0]-= 1;

            }
            moveDown = false;
		}
		else if(moveLeft) //else if(keysDown[37] && player.tileFrom[0]>0 && gameMap[toIndex(player.tileFrom[0]-1, player.tileFrom[1])]==1)
		{
		    console.log("it is lefttttt")
		    if(direction == "up")
		    {
		        direction = "left";
		    }
		    else if(direction == "left")
		    {
		        direction = "down";
		    }
		    else if(direction == "down")
		    {
		        direction = "right";
		    }
		    else if(direction == "right")
		    {
		        direction = "up"
		    }
		    moveLeft = false;
        }
		else if(moveRight) //else if(keysDown[39] && player.tileFrom[0]<(mapW-1) && gameMap[toIndex(player.tileFrom[0]+1, player.tileFrom[1])]==1)
		{
		    console.log("it is righttt")
            if(direction == "up")
		    {
		        direction = "right";
		    }
		    else if(direction == "left")
		    {
		        direction = "up";
		    }
		    else if(direction == "down")
		    {
		        direction = "left";
		    }
		    else if(direction == "right")
		    {
		        direction = "down";
		    }
		    moveRight = false;
        }
        if(player.tileFrom[0]!=player.tileTo[0] || player.tileFrom[1]!=player.tileTo[1])
        {
		    player.timeMoved = currentFrameTime;
        }
    }

    for(var y = 0; y < mapH; ++y)
    {
        for(var x = 0; x < mapW; ++x)
        {
            switch(gameMap[((y*mapW)+x)])
            {
                case 0:
                    ctx.fillStyle = "#000001";
                    break;
                default:
                    ctx.fillStyle = "#EEEEEE";
            }

        ctx.fillRect( x*tileW, y*tileH, tileW, tileH);
        }
    }
    ctx.fillStyle = "#0000ff";
	ctx.fillRect(player.position[0], player.position[1], player.dimensions[0], player.dimensions[1]);


    var imageUp = document.getElementById('carUp');
    var imageRight = document.getElementById('carRight');
    var imageDown = document.getElementById('carDown');
    var imageLeft = document.getElementById('carLeft');
    var flag = document.getElementById('flag');

    ctx.drawImage(flag, tileW * finish[0] + 5, tileH * finish[1] + 5, 90, 90);

    if(direction == "up")
    {
        ctx.drawImage(imageUp, player.position[0], player.position[1], player.dimensions[0], player.dimensions[1]);
    }
    else if(direction == "right")
    {
        ctx.drawImage(imageRight, player.position[0], player.position[1], player.dimensions[0], player.dimensions[1]);
    }
    else if(direction == "down")
    {
        ctx.drawImage(imageDown, player.position[0], player.position[1], player.dimensions[0], player.dimensions[1]);
    }
    else if(direction == "left")
    {
        ctx.drawImage(imageLeft, player.position[0], player.position[1], player.dimensions[0], player.dimensions[1]);
    }


    if (gameMap[toIndex(player.tileFrom[0], player.tileFrom[1])] == 0)
    {
        modal.style.display = "block"; // can trigger restart menu
        return;
    } else if(gameMap[toIndex(player.tileFrom[0], player.tileFrom[1])] == 3)
    {
        modal.style.display = "block"; // can trigger restart menu
        return;
    } else if(gameMap[toIndex(player.tileFrom[0], player.tileFrom[1])] == undefined)
    {
        modal.style.display = "block"; // can trigger restart menu
        return;
    }

    if(len > 0)
    {
        if(counter == len)
        {
            if(player.tileFrom[0]==player.tileTo[0] && player.tileFrom[1]==player.tileTo[1])
            {
                removeAll();
                document.getElementById('popout-text').innerHTML = "Finish";
                modal1.style.display = "block";
                len = 0;
            }
        }
    }

    lastFrameTime = currentFrameTime;
    requestAnimationFrame(drawGame);
}

//when run button is clicked
$(function () {
    $("#mybutton5").click(function (event) {
        len = commandList.length;
        if(len == 0)
        {
            document.getElementById('popout-text').innerHTML = "Please add command!";
            modal1.style.display = "block";
            return;
        }
        counter = 0;
        console.log(len)
        $.getJSON('/run', {},
                function (data) { });
        return true;
    });
});

//when up icon is clicked
$(function () {
    $("#up").click(function (event) {
    console.log(modal)
    if (cmdNumber >= 10)
    {
        document.getElementById('popout-text').innerHTML = "Commands exceeded limit!";
        modal1.style.display = "block";
        return;
    }
    var val = "Up";
    cmdNumber++;
    commandList.push("up");
    $("#list").append("<li>" + val + "</li>");
    });
});

//when down icon is clicked
$(function () {
    $("#down").click(function (event) {
    if (cmdNumber >= 10)
    {
        document.getElementById('popout-text').innerHTML = "Commands exceeded limit!";
        modal1.style.display = "block";
        return;
    }
    var val = "Down";
    cmdNumber++;
    commandList.push("down");
    $("#list").append("<li>" + val + "</li>");
    });
});

// when left icon is clicked
$(function () {
    $("#left").click(function (event) {
    if (cmdNumber >= 10)
    {
        document.getElementById('popout-text').innerHTML = "Commands exceeded limit!";
        modal1.style.display = "block";
        return;
    }
    var val = "Left";
    cmdNumber++;
    commandList.push("left");
    $("#list").append("<li>" + val + "</li>");
    });
});

// when right icon is clicked
$(function () {
    $("#right").click(function (event) {
    if (cmdNumber >= 10)
    {
        document.getElementById('popout-text').innerHTML = "Commands exceeded limit!";
        modal1.style.display = "block";
        return;
    }
    var val = "Right";
    cmdNumber++;
    commandList.push("right");
    $("#list").append("<li>" + val + "</li>");
    });
});

// reset commandlist
function removeAll() {
    commandList = [];
    cmdNumber = 0;
    document.getElementById("list").innerHTML = "";
}


// When the user clicks anywhere outside of the popout, close it
window.onclick = function (event) {
    if (event.target == modal1) {
        modal1.style.display = "none";
    }
}