package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	
	defer writer.Flush()

	var hour, minute, time int
	fmt.Fscanln(reader, &hour, &minute)
	fmt.Fscanln(reader, &time)

	// 요리 시간이 얼마만큼 걸리는 지 확인 
	dHoure := (time) / 60
	dMinute := (time) % 60
	
	hour = (hour + dHoure)
	minute = (minute + dMinute)

	if minute >= 60 {
		minute = minute % 60
        hour += 1
    }
	if hour >= 24{
		hour = hour % 24
	}
	fmt.Fprintln(writer, hour, minute)
}
