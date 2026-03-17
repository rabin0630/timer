const start = document.getElementById("start");
const stop = document.getElementById("stop");
const reset = document.getElementById("reset");
const timer = document.getElementById("timer");

let timeleft = 1500; // 25分を秒数にした
let interval ;

const updatetimer = () => {
    const minutes = Math.floor(timeleft / 60);
    const second = timeleft % 60 ;

    timer.innerHTML = `${minutes.toString().padStart(2,"0")}
    :${second.toString().padStart(2,"0")}`;
}

const startTimer = () => {
    interval = setInterval(() => {
        timeleft--;
        updatetimer();

    if (timeleft === 0){
        clearInterval(interval);
        alert("Times up!");
        timeleft = 1500;
        updatetimer();
    }
    },1000);
};

const stopTimer = () => clearInterval(interval);

const resetTimer = () => {
    clearInterval(interval);
    timeleft = 1500;
    updatetimer();
}

start.addEventListener("click",startTimer);
stop.addEventListener("click",stopTimer);
reset.addEventListener("click",resetTimer);