// 데이터 불러오기
function parseData(createGraph) {
	Papa.parse("./data/test.csv", {
	download: true,
	complete: function(results) {
	createGraph(results.data);
	}
	});
}
	    
var years = [];
var CNT_WAIT = [];

function createGraph(data) {
	// 새로운 배열에 데이터 각각 주입
	for (var i = 1; i < data.length; i++) {
		years.push(data[i][0]);
		CNT_WAIT.push(data[i][1]);
		}
	};

parseData(createGraph);
  
var data = [{
	x: years, 
	y: CNT_WAIT,
	mode: 'lines',
	line: {color: '#80CAF6'}
  }]
  
  Plotly.plot('graph', data);  
  
  var cnt = 0;  
  var index = 0;
  var interval = setInterval(function() {
	
	var update = {
		x: years, 
		y: CNT_WAIT,
	}

	var minuteView = {
		  xaxis: {
			range: [cnt-10, cnt]
		  }
		};
	
	Plotly.relayout('graph', minuteView);
	Plotly.extendTraces('graph', { y:[[CNT_WAIT[index]]]}, [0])
	cnt ++;
	index ++;
	
	if(cnt === 100) clearInterval(interval);
  }, 1000);
  