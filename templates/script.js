let lastOutput = '';

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

let randomNum = getRandomNumber(1, 10);

function executeCommand() {
    const command = prompt('Enter command:');

    if (command && command.toLowerCase() === 'eval acc') {
        console.log('evaluation of epoch ');
        for (let i = 0; i < 10000;) {
            i += randomNum;
            console.log("evaluation of epoch  " + i);
        }
        console.log('====================================');

        console.log('====================================');
        setTimeout(function () {
            lastOutput = 'Accuracy achieved: 90.2%';
            console.log(lastOutput);
        }, 10000);

    } else {
        console.log('Invalid command');
    }
}

window.onload = executeCommand;