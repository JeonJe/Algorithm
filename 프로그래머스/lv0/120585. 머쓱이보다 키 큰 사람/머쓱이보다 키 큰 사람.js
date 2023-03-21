function solution(array, height) {
    var answer = 0;
    array.reverse()
    for (var i = 0; i< array.length; i++){
        if (array[i] > height)
        answer++;
    }
    return answer;
}