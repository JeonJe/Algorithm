function solution(A) {
  let myMap = new Map();

  //Counting sort
  for (var i = 0; i < A.length; i++) {
    if (myMap.has(Number(A[i]))) {
      let value = myMap.get(Number(A[i]));
      myMap.set(Number(A[i]), value + 1);
    } else {
      myMap.set(Number(A[i]), 1);
    }
  }
  answer_value = 0;
  answer_key = 0;
  for (const [key, value] of myMap) {
    //Find the largest value which occurs in A exactly A times
    if (value > answer_value && key === value) {
      answer_value = value;
      answer_key = key;
    }
  }

  return answer_key;
}
