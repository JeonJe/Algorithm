class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        List<int[]> answer = new ArrayList<>();

        int start = intervals[0][0];
        int end = intervals[0][1];

        for (int i = 1 ; i < intervals.length; i++){
            //현재 시작 값이 이전 끝 값보다 크다면 이전 값은 추가 되어야 함
            if(intervals[i][0] > end) {
                answer.add(new int[]{start, end});
                start = intervals[i][0];
                end = intervals[i][1];
            } else if (intervals[i][1] > end){
                end = intervals[i][1];
            }
        }
        int answerSize = answer.size();
       if(answerSize == 0 || (start > answer.get(answerSize-1)[1])){
            answer.add(new int[]{start, end});
        }

        int[][] resultArray = new int[answer.size()][];
        for(int i = 0 ; i < answer.size(); i++){
            resultArray[i] = answer.get(i);
        }
        return resultArray;
    }
}