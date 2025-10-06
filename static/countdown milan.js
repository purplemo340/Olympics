function displayTime(){
    let clock = document.querySelector("#clock1");
    let now = new Date();
    let game= new Date('February 6, 2026 00:00:00');
    let time= game.getTime()-now.getTime();
    sec=Math.floor((time%(1000*60))/(1000));
    min=Math.floor((time%(1000*60*60))/(1000*60));
    hour=Math.floor((time%(1000*60*60*24))/(1000*60*60));
    day=Math.floor(time/(1000*60*60*24));
    month=Math.floor(time/(1000*60*60*24*30));
    year=Math.floor(time/(1000*60*60*24*365.25));
    month1=Math.floor(day%365)
    month2=Math.floor(month1/30)
    day1=month1%30
    clock.textContent =year+ "y " + month2+ "m " + (day1) + " d "  + hour +" h "+ min + " min " + sec +" sec ";
    }

setInterval(displayTime,1000)
