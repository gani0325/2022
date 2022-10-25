const lcd = require("./test1.js");

const gpio = require('pigpio').Gpio;
const mcpadc = require('mcp-spi-adc'); // MCP3208 제어모듈

const SPI_SPEED = 1000000 // Clock Speed = 1Mhz
const MOISTURE = 0 // ADC 0번째 채널선택=아날로그센서


lcd.init();

 //const BLUE = 26
const RED = 20

//const bled = new gpio(BLUE, {mode: gpio.OUTPUT});
const rled = new gpio(RED, {mode: gpio.OUTPUT});

var timerid, timeout= 1000; // 타이머제어용
var waterdata = -1; // 조도값 측정데이터 저장용

const Water = mcpadc.openMcp3208(MOISTURE, // 채널0 지정 (아날로그조도센서)
              {  speedHz: SPI_SPEED }, // Clock속도 지정
                 (err) => { // 초기화처리후 콜백함수 등록
                 console.log("SPI 채널0 초기화완료!");
                 console.log("-----------------------------");
            if (err) console.log('채널0 초기화실패!(HW점검!)');
});

const analogMoisture = ( ) => {
   Water.read((error, reading)=> {
      console.log("현재 측정된 습도값 : (%d)", reading.rawValue);
      waterdata = reading.rawValue;
});

        if ( waterdata != -1 ){ // 아날로그 조도센서값을 읽었다면
             if (waterdata > 1000) {
                  console.log("습도 충분! blue LED!");
                  rled.digitalWrite(0);
         //         bled.digitalWriet(1);
             }
             else {
                  console.log("습도 부족! 건조! red LED!");
                  rled.digitalWrite(1);
           //       bled.digitalWrite(0);
             }
        timerid = setTimeout(analogMoisture, timeout);
        }

       network.get_active_interface( (err, ifaces) => { // WiFi IP주소(라즈베리파이)획득
              if (ifaces != undefined) {
                   if (ifaces.name == 'wlan0') {
                        console.log('라즈베리파이 IP주소: ' + ifaces.ip_address);
                        lcd.printMessage('Computer Gachon ', ifaces.ip_address); // LCD 출력
}
}
});

}

setImmediate(analogMoisture, 2000);
