// <!DOCTYPE html>
// <html lang="en" >
// <head>
//   <meta charset="UTF-8">
//   <title>D3 REaltime chart </title>
// <style>
//     svg {
//       font: 10px sans-serif;
//     }
//     .line {
//       fill: none;
//       stroke: #000;
//       stroke-width: 1.5px;
//     }
//     .axis path,
//     .axis line {
//       fill: none;
//       stroke: #000;
//       shape-rendering: crispEdges;
//     }
// </style>
// </head>
// <body>
//     <script src='https://d3js.org/d3.v3.min.js'></script>
//     <script  src="javascripts/index.js"></script>
// </body>
// </html>

var CNT_WAIT = [];
var YEARS = [];

d3.csv("./data/test.csv", function(error, data) {
    for (var i = 0; i < data.length; i++) {
        CNT_WAIT.push(data[i]. cnt_wait)
        YEARS.push(data[i]. insert_date_time)
    }
    console.log(CNT_WAIT);
    console.log(YEARS);

})
console.log(CNT_WAIT);
console.log(YEARS);

	
google.charts.load('current', {'packages':['bar']});
google.charts.setOnLoadCallback(drawChart);
 
function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Year', 'Sales', 'Expenses', 'Profit'],
        ['2014', 1000, 400, 200],
        ['2015', 1170, 460, 250],
        ['2016', 660, 1120, 300],
        ['2017', 1030, 540, 350]
    ]);
 
    var options = {
        chart: {
        title: 'Company Performance',
        subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        }
    };
 
    var chart = new google.charts.Bar(document.getElementById('columnchart_material'));
 
    chart.draw(data, google.charts.Bar.convertOptions(options));
}















// var n = 40,
//     random = d3.random.normal(0, .2),
//     data = d3.range(n).map(random);
 
// var margin = {top: 20, right: 20, bottom: 20, left: 40},
//     width = 960 - margin.left - margin.right,
//     height = 500 - margin.top - margin.bottom;
 
// var x = d3.scale.linear()
//     .domain([0, n - 1])
//     .range([0, width]);
 
// var y = d3.scale.linear()
//     .domain([-1, 1])
//     .range([height, 0]);
 
// var line = d3.svg.line()
//     .x(function(d, i) { return x(i); })
//     .y(function(d, i) { return y(d); });
 
// var svg = d3.select("body").append("svg")
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom)
//   .append("g")
//     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
 
// svg.append("defs").append("clipPath")
//     .attr("id", "clip")
//   .append("rect")
//     .attr("width", width)
//     .attr("height", height);
 
// svg.append("g")
//     .attr("class", "x axis")
//     .attr("transform", "translate(0," + y(0) + ")")
//     .call(d3.svg.axis().scale(x).orient("bottom"));
 
// svg.append("g")
//     .attr("class", "y axis")
//     .call(d3.svg.axis().scale(y).orient("left"));
 
// var path = svg.append("g")
//     .attr("clip-path", "url(#clip)")
//   .append("path")
//     .datum(data)
//     .attr("class", "line")
//     .attr("d", line);
 
// tick();
 
// function tick() {
 
//   // push a new data point onto the back
//   data.push(random());
 
//   // redraw the line, and slide it to the left
//   path
//       .attr("d", line)
//       .attr("transform", null)
//     .transition()
//       .duration(500)
//       .ease("linear")
//       .attr("transform", "translate(" + x(-1) + ",0)")
//       .each("end", tick);
 
//   // pop the old data point off the front
//   data.shift();
 
// }



// 데이터 불러오기
// function parseData(createGraph) {
// 	Papa.parse("./data/test.csv", {
// 		download: true,
// 		complete: function(results) {
// 			createGraph(results.data);
// 		}
// 	});
// }

// var years = [];
// var CNT_WAIT = [];

// function createGraph(data) {
// 	// console.log("create 1");
// 	// 새로운 배열에 데이터 각각 주입
// 	for (var i = 1; i < data.length; i++) {
// 		years.push(data[i][0]);
// 		CNT_WAIT.push(data[i][1]);
// 	}
//     console.log(CNT_WAIT);
// };


    //   // load current chart package
    //   google.charts.load('current', {
    //     packages: ['corechart', 'line'],
    //   });
    //   // set callback function when api loaded
    //   google.charts.setOnLoadCallback(drawChart);
    //   function drawChart() {
    //     // create data object with default value
    //     let data = google.visualization.arrayToDataTable([
    //       ['Time', 'CPU Usage', 'RAM'],
    //       [0, 0, 0],
    //     ]);
    //     // create options object with titles, colors, etc.
    //     let options = {
    //       title: 'CPU Usage',
    //       hAxis: {
    //         textPosition: 'none',
    //       },
    //       vAxis: {
    //         title: 'Usage',
    //       },
    //     };
    //     // draw chart on load
    //     let chart = new google.visualization.LineChart(
    //       document.getElementById('chart_div')
    //     );
    //     chart.draw(data, options);
    //     // max amount of data rows that should be displayed
    //     let maxDatas = 50;
    //     // interval for adding new data every 250ms
    //     let index = 0;
    //     setInterval(function () {
    //       // instead of this random, you can make an ajax call for the current cpu usage or what ever data you want to display
    //       let randomCPU = Math.random() * 20;
    //       let randomRAM = Math.random() * 50 + 20;
    //       if (data.getNumberOfRows() > maxDatas) {
    //         data.removeRows(0, data.getNumberOfRows() - maxDatas);
    //       }
    //       data.addRow([index, randomCPU, randomRAM]);
    //       chart.draw(data, options);
    //       index++;
    //     }, 100);
    //   }










    