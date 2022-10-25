const gpio = require("pigpio").Gpio;

const GREEN = 21;
const gled = new gpio(GREEN, {mode: gpio.OUTPUT});


const TurnOn = () => {

    gled.digitalWrite(1);
    console.log("turn on");
}


process.on('SIGINT', ( ) => {
    gled.digitalWrite(0);
    console.log(" Ctrl+x Exit...");
    process.exit();
});
setImmediate(TurnOn);



