
function makeSet(str){
    let set = []

    for(let i = 0; i < str.length-1; i++){
        const split = str.substr(i,2)
        if (isAlphaNumeric(split)){
            set.push(split)
        }
    }
    return set
}

function isAlphaNumeric(token) {
  //특수문자가 있는지 확인하는 패턴
  const pattern = /^[a-zA-Z]+$/;
  //특수문자가 없으면 true, 있으면 false 반환
  return pattern.test(token);
}

function getUnionSet(setStr1, setStr2) {
  const union = [];

  let union1 = [...setStr1];
  let union2 = [...setStr2];
  while (union1.length > 0 ) {
    let a = union1.shift();
      //a라는 값이 없으면 추가 해줘야 함 
    if (union2.indexOf(a) === -1) union.push(a);
    else{
        for(let i = 0; i < union2.length; i++) {
          if(union2[i] === a)  {
            union2.splice(i, 1);
            i--;
          break
          }
        }
        union.push(a)
    }
  }
    
  if (union2.length > 0) union.push(...union2);

  return union;
}

function getIntersetionSet(set1, set2){
        const intersection = [];
        for (const element of set1) {
          if (set2.includes(element)) {
            intersection.push(element);
            set2.splice(set2.indexOf(element), 1);
          }
        }

        return intersection;
}

function getJaccardSimilarity(str1, str2){
  // 대소문자 구분 없이 비교하기 위해 모두 소문자로 변환
  str1 = str1.toLowerCase();
  str2 = str2.toLowerCase();

  
  // 두 글자씩 끊어서 다중집합 생성
  const setStr1 = makeSet(str1);
  const setStr2 = makeSet(str2);
    if (setStr1.length == 0 && setStr2.length ==0 ){
        return 1
    }
  // 합집합과 교집합 구하기
//   console.log("before union ", setStr1, setStr2)
  const union = getUnionSet(setStr1, setStr2);
//   console.log("after union ",setStr1, setStr2);
  const intersection = getIntersetionSet(setStr1, setStr2);
  console.log(intersection)
    console.log(union)
  
  // 자카드 유사도 계산

  const jaccard = intersection.length  / union.length ;
  
  return jaccard

}


function solution(str1, str2) {
  var answer = 0;
  answer = getJaccardSimilarity(str1,str2)
  answer = Math.floor(answer * 65536)
  return answer;
}

