package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func add(x int, y int) int {
	return x + y
}

func subtract(x int, y int) int {
	return x - y
}

func multiply(x int, y int) int {
	return x * y
}

func calculator() {
	var result int
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter the equation: ")
	for scanner.Scan() {
		var inp = scanner.Text()
		var s = strings.Fields(inp)
		var x, err1 = strconv.ParseInt(s[0], 10, 32)
		var op = s[1]
		var y, err2 = strconv.ParseInt(s[2], 10, 32)
		if err1 != nil {
			fmt.Println(err1)
		} else if err2 != nil {
			fmt.Println(err2)
		} else if op == "+" {
			result = add(int(x), int(y))
		} else if op == "-" {
			result = subtract(int(x), int(y))
		} else if op == "x" {
			result = multiply(int(x), int(y))
		} else {
			fmt.Println("Not a valid equaction", inp)
			return
		}
		fmt.Println(inp, " = ", result)
		fmt.Print("Enter the equation: ")
	}
}

func main() {
	calculator()
}
