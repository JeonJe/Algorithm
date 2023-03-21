function solution(n) {
    var answer = 0;
    var div = 0;
    var remain = 0;
    div = parseInt(n / 7)
    remain = n % 7
    if (remain == 0){
        answer = div
    }else{
        answer = div + 1
    }
    return answer;
}