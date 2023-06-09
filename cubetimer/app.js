let [milliseconds, seconds, minutes, hours] = [0, 0, 0, 0];
let timerRef = document.querySelector(".timerDisplay");
let int = null;
frozen = true;
pressed = false;

// Start
document.addEventListener("keyup", (e) => {
    if (e.code === "Space") {
        if (pressed === false) {
            if (frozen === true) {
                int = setInterval(displayTimer, 10);
                frozen = false;
                [milliseconds, seconds, minutes, hours] = [0, 0, 0, 0];
            }
        } else {
            pressed = false;
        }
    }
});

// Stop
document.addEventListener("keydown", (e) => {
    if (e.code === "Space") {
        if (frozen === false) {
            clearInterval(int);
            frozen = true;
            pressed = true;
        }
    }
});

function displayTimer() {
    milliseconds += 10;
    if (milliseconds == 1000) {
        milliseconds = 0;
        seconds++;
        if (seconds == 60) {
            seconds = 0;
            minutes++;
            if (minutes == 60) {
                minutes = 0;
                hours++;
            }
        }
    }

    let h = hours < 10 ? "0" + hours : hours;
    let m = minutes < 10 ? "0" + minutes : minutes;
    let s = seconds < 10 ? "0" + seconds : seconds;
    let ms =
        milliseconds < 10
            ? "00" + milliseconds
            : milliseconds < 100
            ? "0" + milliseconds
            : milliseconds;

    timerRef.innerHTML = ` ${h} : ${m} : ${s} . ${ms}`;
}
