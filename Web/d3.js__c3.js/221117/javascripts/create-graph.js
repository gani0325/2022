/*
 * Parse the data and create a graph with the data.
 */


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

	// 슬라이스 하며 10칸씩 업데이트 하기 위한 배열 생성
	var index = 0;
	var N_CNT_WAIT = [];
	var N_YEARS = [];

	// 1초씩 반복하며 업데이트된 차트 시각화
	setInterval(function run() {
		temp = index++
		N_CNT_WAIT = CNT_WAIT.slice(temp, 10+temp)
		N_YEARS = years.slice(temp, 10+temp)

		console.log(N_CNT_WAIT);
		console.log(N_YEARS);
		
		// c3.js 사용해서 line chart 그리기
		var chart = c3.generate({
			bindto: '#chart',
			data: {
				columns: [
					N_CNT_WAIT
				],
				labels: true
			},
			
			axis: {
				x: {
					type: 'category',
					categories: N_YEARS,
					tick: {
						multiline: false,
						culling: {
							// 틱이 추려진 다음 제한된 틱 텍스트만 표시
							max: 15
						}
					}
				}
			},
			zoom: {
				enabled: true
			},
			legend: {
				position: 'right'
			}
		});

	}, 1000)
	
	// console.log("finish")
};

parseData(createGraph);
