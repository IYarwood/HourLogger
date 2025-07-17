let startTime;
let stopTime;
let timerStart;
let timerStop;
let startTimeValue;
let stopTimeValue;
let jobID;

async function getTime() {
    try {
        const response = await fetch("http://127.0.0.1:8000/getTime/");
        const data = await response.json();
        return data.time; 
    } catch (error) {
        console.error("Fetch error:", error);
        return "---";
    }
}

async function makeLog() {
    try{
        const response = await fetch(`http://127.0.0.1:8000/createLog?start=${startTimeValue}&stop=${stopTimeValue}&jobID=${jobID}`);
        //const response = await fetch(`http://31.97.100.20:8080/createLog?start=${startTimeValue}&stop=${stopTimeValue}&jobID=${jobID}`);
        const data = await response.json();
        const status = data.status
        return status;
    } catch (error) {
        return "Failed"
    }
}

document.addEventListener("DOMContentLoaded", function () {
    startTime = document.querySelector('#startTime');
    stopTime = document.querySelector('#stopTime');
    statusOutput = document.querySelector('#status');
    submissionDiv = document.querySelector('#submissionDiv');
    jobID = statusOutput.dataset.jobid;

    startButton = document.querySelector('#startButton');
    stopButton = document.querySelector('#stopButton');

    startButton.addEventListener("click", async () => {
        const time = await getTime();
        startTime.innerText = time;
        startTimeValue = time;
        stopButton.hidden = false;
    });

    stopButton.addEventListener("click", async () => {
        const time = await getTime();
        stopTime.innerText = time;
        stopTimeValue = time;
        submitButton.hidden = false;
    });

    submitButton.addEventListener("click", async () => {
        statusOutput.innerText = await makeLog();
    });

});
