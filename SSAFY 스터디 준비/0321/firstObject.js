// 고차 함수: 함수를 인자로 받거나, 함수를 반환하는 함수를 고차 함수라고 합니다.
//  고차 함수를 사용하면 코드의 재사용성을 높일 수 있습니다.

// 고차 함수 예시
function multiplyBy(factor) {
    return function(number) {
      return number * factor;
    };
  }
  
  var double = multiplyBy(2);
  var triple = multiplyBy(3);
  
  console.log(double(5)); // 10
  console.log(triple(5)); // 15




// 클로저: 함수가 자신의 밖에 있는 변수를 참조할 때, 클로저가 형성됩니다.
// 클로저를 사용하면 변수를 숨기고, 정보를 보호할 수 있습니다.

// 클로저 예시
function makeCounter() {
    var count = 0;
    return function() {
      count += 1;
      return count;
    };
  }
  
  var counter1 = makeCounter();
  var counter2 = makeCounter();
  
  console.log(counter1()); // 1
  console.log(counter1()); // 2
  
  console.log(counter2()); // 1
  console.log(counter2()); // 2