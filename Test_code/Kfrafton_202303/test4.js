function solution(S) {
  let answer = -1;
  let myMap = new Map();

  for (let i = 0; i < S.length - 1; i++) {
    //start of digram
    const split = S.substr(i, 2);
    //skip the digram that you have already checked
    if (myMap.has(split)) {
      continue;
    } else {
      let lastDigram = S.lastIndexOf(split);
      if (lastDigram > i) {
        myMap.set(split, 0);
        answer = Math.max(answer, lastDigram - i);
      }
    }
  }
  return answer;
}
