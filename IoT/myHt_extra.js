const myHt = require("./myHt.js");
const HTPIN = 21;

myHt.init(HTPIN);

console.log("====================================");
console.log("5초 후 부터 5초 간격으로 온습도 측정");
console.log("====================================");


setInterval(() => {myHt.read(); }, 5000);
