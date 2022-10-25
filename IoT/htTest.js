const gpio = require("pigpio").Gpio;
const mcpadc = require("mcp-spi-adc");

const SPI_SPEED = 1000000
const MOISTURE = 0

var timerid, timeout = 200;
var waterdata = -1;

const Water = mcpadc.openMcp3208(MOISTURE,
        { speedHz : SPI_SPEED },
         (err) => {
            console.log("SPI 채널 0 초기화 완료");
            console.log("----------------------");
            if (err) console.log("채널 0 초기화 실패");
        });

const analogMoisture = () => {
    Water.read((error, reading) => {
         console.log("현재 조도값 : %d ", reading.rawValue);
         waterdata = reading.rawValue;
    });
    if (waterdata != -1) {
         console.log("습도");
     }
     timerid = setTimeout(analogMoisture, timeout);
}

process.on("SIGINT", () => {
      Water.close(() =>  {
         console.log("MCP-ADC 해제, 종료");
         process.exit();
      });
});

setImmediate(analogMoisture);

