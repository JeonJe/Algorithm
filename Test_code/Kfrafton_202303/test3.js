function solution(A) {
  let myMap = new Map();
  //Counting Sort
  for (var i = 0; i < A.length; i++) {
    if (myMap.has(Number(A[i]))) {
      let value = myMap.get(Number(A[i]));
      myMap.set(Number(A[i]), value + 1);
    } else {
      myMap.set(Number(A[i]), 1);
    }
  }
  //Sort by key in descending order
  const mapSort = new Map([...myMap.entries()].sort().reverse());
  let arr = [...mapSort];
  let answer = 1;
  let appear = 0;

  for (var i = 1; i < arr.length; i++) {
    appear = mapSort.get(arr[i][0]);
    //can only put 1 each side
    if (appear >= 2) {
      answer += 2;
    } else if (appear == 1) {
      answer += 1;
    }
  }
  return answer;
}
