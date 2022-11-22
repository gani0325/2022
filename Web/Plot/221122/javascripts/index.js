// Streaming with Timestamp

// 1. csv 로딩해서 전체적으로 공유하자
var years = new Array();
var CNT_WAIT = new Array();

function parseData() {
	Papa.parse("./data/test.csv", {
	download: true,
	complete: function(results) {
		console.log(results)
		for (var i = 1; i < results.data.length; i++) {
			years.push(results.data[i][0]);
			CNT_WAIT.push(results.data[i][1]);
			}
			console.log(years);
		}
	})
};
parseData();


// 2. 그 다음 Y 값을 가져오는 함수
var index = 0;
function getYvalueFromCsv(index){
	//csv 로딩
	return CNT_WAIT[index];

}
// 그 다음 X 값 가져오는 함수
function getXvalueFromCsv(index){
	//csv 로딩
	return years[index];

}

// 3. 시간을 활용해서 그다음 값 업데이트 하기
var time = new Date();

var data = [{
	x: [getXvalueFromCsv(index)], 
	y: [getYvalueFromCsv(index)],
	mode: 'lines',
	line: {color: '#80CAF6'}
}]


Plotly.newPlot('graph', data);  

// 그 다음 cnt 증가시키기
var cnt = 0;

// 1초마다 업데이트 반복하기
var interval = setInterval(function() {
	var time = new Date();

	var update = {
		x:  [[getXvalueFromCsv(cnt)]],
		y: [[getYvalueFromCsv(cnt)]]
	}
	
	console.log(getYvalueFromCsv(cnt))
	console.log(getXvalueFromCsv(cnt))

	var olderTime = time.setMinutes(time.getMinutes() - 1);
	var futureTime = time.setMinutes(time.getMinutes() + 1);

	var minuteView = {
        xaxis: {
			type: 'date',
			range: [olderTime,futureTime]
        }
      };

	// Plotly.relayout('graph', minuteView);
	// 전체 플롯을 다시 그리는 것 보다, 기존에 업데이트 하면서 그리기
	Plotly.extendTraces('graph', update, [0])

	// cnt 가 100 이 되면 다시 시작
	//if(++cnt === 100) clearInterval(interval);
	++cnt;
}, 500);
