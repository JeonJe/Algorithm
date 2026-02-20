package main

import (
	"bufio"
	"fmt"
	"os"
)

func main(){

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout) 

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	//n만큼 돌면서 data받기

	//종료시간 기준으로 정렬

	
	//last, start, end시간 비교 

	fmt.Fprintln(writer, n)

	
}