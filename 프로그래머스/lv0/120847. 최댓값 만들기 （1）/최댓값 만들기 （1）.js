function solution(numbers ) {
    var answer = 0;
    var toNumbers  = numbers.map((i) => Number(i));
    
    toNumbers.sort(function compare(a,b){
        return b - a;
    })
    
    answer = toNumbers[0] * toNumbers[1]
    return answer;
}