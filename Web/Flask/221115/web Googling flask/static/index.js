// div의 width를 설정
// 키워드를 표현하는 div에 저장된 value값을 가져온 뒤, 각 퍼센트(%)를 계산하여 width를 재설정

var boxs = document.querySelectorAll('.box');

total = 0

// 총 값 확인
boxs.forEach(element => {
    console.log(element.getAttribute('value'))
    total += parseFloat(element.getAttribute('value'))
});

// width 지정
boxs.forEach(element => {
    element.style.width = parseFloat(element.getAttribute('value')) / total * 100 + '%';
});