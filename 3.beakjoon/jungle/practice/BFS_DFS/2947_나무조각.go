package main

import (
	"bufio"
	"fmt"
	"os"
)

func dfs(depth int, temp []int){
	if depth == len(temp){
		return 
	}
	if temp[depth] < temp[depth+1] && depth+1 < len(temp) {
		temp[depth], temp[depth+1] = temp[depth+1], temp[depth]
		dfs(depth+1, temp)
	}else if temp[depth-1] > temp[depth] && depth-1 > 0{
		temp[depth-1], temp[depth] = temp[depth], temp[depth-1]
		dfs(depth-1,temp)
	}else{
		dfs(depth+1,temp)
	}


}

func main(){

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	
	n := 5
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &arr[i])
	}

	dfs(0, arr)

	
	
	


	
}