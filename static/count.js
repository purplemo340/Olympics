function displayTime(){
    let clock = document.querySelector("#clock");
    let now = new Date();
    let game= new Date('July 26, 2024 13:30:00');
    let time= game.getTime()-now.getTime();
    sec=Math.floor((time%(1000*60))/(1000));
    min=Math.floor((time%(1000*60*60))/(1000*60));
    hour=Math.floor((time%(1000*60*60*24))/(1000*60*60));
    day=Math.floor(time/(1000*60*60*24));
    clock.textContent = day + " d " + hour +" h "+ min + " min " + sec +" sec ";
    console.log("hi");
    }

setInterval(displayTime,1000)
  