window.onload = function()
{
    commandList = document.getElementById('info').innerHTML;
    const obj = JSON.parse(commandList);
    commandList = obj.cmdHistory;
    commandTimelist = obj.cmdTime;
    console.log(commandList);
    console.log(commandTimelist);
    console.log(typeof commandList);
    for(var i = 0; i < commandList.length; i++)
    {
        $("#list").append("<tr> <td>" + commandTimelist[i] + "</td> <td>" + commandList[i] + "</td> </tr>");
    }
}