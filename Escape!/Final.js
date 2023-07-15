// Create x
var x = 1;

function start(x) {
    // This will play when the user starts the program
    // we need to show the tool buttons while getting rid of the start button
    // none is used when you do not want to see the element
    // block vs inline for visual placement
    document.getElementById("startButton").style.display = "none"
    document.getElementById("exitButton").style.display = "inline"
    document.getElementById("Text1").style.display = "block"
    document.getElementById("Text2").style.display = "block"
    // Here we change the background to fit the scene
    document.body.style.backgroundImage = "url('HTML1.png')";
    document.getElementById("ropeButton").style.display = "inline"
    document.getElementById("knifeButton").style.display = "inline"
    document.getElementById("clipButton").style.display = "inline"
    document.getElementById("crowbarButton").style.display = "inline"
    document.getElementById("ropeButton").disabled = false;
    document.getElementById("knifeButton").disabled = false;
    document.getElementById("crowbarButton").disabled = false;
    document.getElementById("clipButton").disabled = false;

 }

 function returnToStart() {
    // This function will play when the user clicks the exit button
    document.body.style.backgroundImage = "url('HTML2.png')";
    // Turn the display to none for the tool buttons
    document.getElementById("ropeButton").style.display = "none"
    document.getElementById("knifeButton").style.display = "none"
    document.getElementById("clipButton").style.display = "none"
    document.getElementById("crowbarButton").style.display = "none"
    document.getElementById("startButton").style.display = "inline"
    document.getElementById("Text1").innerHTML = "";
    document.getElementById("Text2").innerHTML = "";
    // set x to 1 to start over
    x = 1;
    document.getElementById("Text1").style.color = "black";
    document.getElementById("Text2").style.color = "black";
    return x;
 }

 function gameOver(){
    // This function will play if the user fails to use the correct tool
    document.body.style.backgroundImage = "url('HTML3.png')";
    document.getElementById("ropeButton").style.display = "none"
    document.getElementById("knifeButton").style.display = "none"
    document.getElementById("clipButton").style.display = "none"
    document.getElementById("crowbarButton").style.display = "none"
    document.getElementById("startButton").style.display = "inline"
    document.getElementById("Text1").style.color = "black";
    document.getElementById("Text2").style.color = "black";
    x = 1;
    return x;
 }
// Functions that serve as the buttons
 function crowbar() {
    // We will want to disable the tool afte ruse
    document.getElementById("crowbarButton").disabled = true;
    alert("You used the Crowbar!");
    if (x !== 3){
        document.getElementById("Text1").innerHTML = "Your crowbar breaks without completing the task! You do not have the proper tools the escape.";
        document.getElementById("Text2").innerHTML = "After running out of water and hope you did not escape the cell...";
        gameOver(x);
    }
    // Change the text box to show the step has been completed
    document.getElementById("Text1").innerHTML = "You begin to pry open the window while standing on the bed to give you a little extra height.";
    document.getElementById("Text2").innerHTML = "As the bars are separated enough for you to push through you can taste the freedom you have always wanted. How will you climb through?";
    // Increase x for the future function use
    x = x + 1;
    // return will allow for other functions to read the new x value
    return x;
 }

 function knife() {
    // Second funciton
    document.getElementById("knifeButton").disabled = true;
    alert("You used the Knife!");
    if (x !== 2){
        // Change the text if the player did the game wrong
        document.getElementById("Text1").innerHTML = "Your knife breaks without completing the task! You do not have the proper tools the escape.";
        document.getElementById("Text2").innerHTML = "After running out of water and hope you did not escape the cell...";
        // run the game over function
        gameOver(x);
    }
    document.getElementById("Text1").innerHTML = "After finding the areas where the bed is connected to the frame you cut it loose. The bed has been loosened enough to move.";
    document.getElementById("Text2").innerHTML = "You set it up against the wall and get just enough height to reach the window, but there are bars blocking the exit. What tool will you use?";
    x = x + 1;
    return x;
 }

 function rope() {
    // Function needs to also serve as the exit of thew game. We will need to be more here
    document.getElementById("ropeButton").style.display = "none"
    document.getElementById("knifeButton").style.display = "none"
    document.getElementById("clipButton").style.display = "none"
    document.getElementById("crowbarButton").style.display = "none"
    document.body.style.backgroundImage = "url('HTML4.png')";
    document.getElementById("ropeButton").disabled = true;
    // Alert the user
    alert("You used the Rope!");
    // Create an if statement to see if they did the game in the correct order.
    if (x !== 4){
        document.getElementById("Text1").innerHTML = "Your rope snaps without completing the task! You do not have the proper tools the escape.";
        document.getElementById("Text2").innerHTML = "After running out of water and hope you did not escape the cell...";
        gameOver(x);
        return;
    }
    document.getElementById("Text1").style.color = "black";
    document.getElementById("Text2").style.color = "black";
    document.getElementById("Text1").innerHTML = "Freedom at last! You have escaped the cell!";
    document.getElementById("Text2").innerHTML = "Congragulations on beating Escape!";
    x = x + 1;

    return x;
 }

 function paperClip() {
    // First function the player will use
    document.getElementById("clipButton").disabled = true;
    alert("You used the Paperclip!");
// Check if they did the steps correctly
    if (x !== 1){
        document.getElementById("Text1").innerHTML = "Your paperclip breaks without completing the task! You do not have the proper tools the escape.";
        document.getElementById("Text2").innerHTML = x;
        gameOver(x);
    }


    document.getElementById("Text1").innerHTML = "Using the paperclip you are able to fit the end into the handcuffs. The come undone and your hands are free.";
    document.getElementById("Text2").innerHTML = "There isn't much here and you can't make it out of the locked door. You see a window too high to reach and and bed. What tool will you use?";
    x = x + 1;
    return x;
 }
