let xAxisData = ['철수','영희','민수','지수']; // x축 데이터 배열 생성
let seriesData = [70,80,100,30]; // 값 데이터 배열 생성

window.onload = function() { // 페이지 로드 시 실행
document.getElementById("drawLine").addEventListener('click', drawBaseLine); // Line Chart 버튼 클릭 시 이벤트 정의 : drawChart 매서드 실행
document.getElementById("drawDetection").addEventListener('click', drawDetectionLine); // Bar Chart 버튼 클릭 시 이벤트 정의 : drawChart 매서드 실행
}


function drawBaseLine () { 
	console.log("hi")


	// 데이터 불러오기
function parseData(createGraph) {
	Papa.parse("./data/test.csv", {
		download: true,
		complete: function(results) {
			createGraph(results.data);
		}
	});
}

function createGraph(data) {
	// console.log("create 1");
	var years = [];
	var CNT_WAIT = [];

	// 새로운 배열에 데이터 각각 주입
	for (var i = 1; i < data.length; i++) {
		years.push(data[i][0]);
		CNT_WAIT.push(data[i][1]);
	}
	console.log(years)
	console.log(CNT_WAIT)

	var myChart = echarts.init(document.getElementById('chart')); // echarts init 메소드로 id=chart인 DIV에 차트 초기화
	option = { // 차트를 그리는데 활용 할 다양한 옵션 정의
                  xAxis: {
                      type: 'category',
                      data: years // 위에서 정의한 X축 데이터
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [
                      {
                      data: CNT_WAIT, // 위에서 정의한 값 데이터
                      type: this.value // 버튼의 value 데이터 ('line' or 'bar')
                      }
                  ]
	};
	myChart.setOption(option); // 차트 디스플레이
}
parseData(createGraph);
}

function drawDetectionLine () { 
	var myChart = echarts.init(document.getElementById('chart')); // echarts init 메소드로 id=chart인 DIV에 차트 초기화
	option = { // 차트를 그리는데 활용 할 다양한 옵션 정의
                  xAxis: {
                      type: 'category',
                      data: xAxisData // 위에서 정의한 X축 데이터
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [
                      {
                      data: seriesData, // 위에서 정의한 값 데이터
                      type: this.value // 버튼의 value 데이터 ('line' or 'bar')
                      }
                  ]
	};
	myChart.setOption(option); // 차트 디스플레이
}