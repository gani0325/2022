const temp = require("node-dht-sensor");

const network = require("network");
const lcd = require("./myLcd.js");

lcd.init();

const humitemp = {
    type : 22,
    pin : 21,
    humi : 0.0,
    temp : 0.0,
    str : '',
    
    init : (number) => {
        humitemp.pin = number;
        console.log("초기화 pin : " + humitemp.pin);
       },
 
    read : () => {
        let humistr = '';
        temp.read(humitemp.type, humitemp.pin, (err, temp, humi) => {
            if (!err) {
                 humitemp.temp = temp.toFixed(1);
                 humitemp.humi = humi.toFixed(1);
                 humitemp.str = (new Date()).toLocaleString("ko");
                 humistr = humitemp.temp + "C       " + humitemp.humi + "%";
                 console.log("온도습도 측정값 : " + humitemp.temp + "C" + humitemp.humi + "%");
                 var th = humistr

                }
            else {
                console.log(err);
            }

        network.get_active_interface((err, ifaces) => {
             if (ifaces != undefined) {
                  if (ifaces.name = "wlan0")  {
                      console.log(ifaces.ip_address);
                      lcd.printMessage(ifaces.ip_address, th);
                     }
                 }
            });
         console.log("현재 온/습도 값 : ", th);
        });
   }
 }

module.exports.init = function(number) {humitemp.init(number); };
module.exports.read = function() { humitemp.read(); };
module.exports.read = function() {humitemp.read(); };
