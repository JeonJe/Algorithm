function solution(S) {
  let answerA = 0;
  let answerB = 0;
  let arr = [...S];
  let lastA = arr.lastIndexOf("A");
  let firstB = arr.indexOf("B");
  //Count how many 'B's come before the latest 'A'
  for (let i = 0; i < lastA; i++) {
    if (arr[i] == "B") {
      answerA++;
    }
  }
  //Count how many 'A's follow the first 'B'
  for (let j = firstB + 1; j < arr.length; j++) {
    if (arr[j] == "A") {
      answerB++;
    }
  }
  return Math.min(answerA, answerB);
}
