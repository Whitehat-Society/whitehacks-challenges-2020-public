package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println("Enter Code:")
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	text = strings.Replace(text, "\n", "", -1)
	partone := "WH2020{G0_"
	parttwo := "R3v3s1ing_"
	partthree := "1s_FuN_Isnt_it}"
	strflag := partone + parttwo + partthree
	if text == strflag {
		fmt.Println("Flag: " + strflag)
	} else {
		fmt.Println("Wrong")
	}

}
