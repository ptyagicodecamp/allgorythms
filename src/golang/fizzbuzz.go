package main

import (
	"fmt"
)

func fizzbuzz() {
	for num := 1; num <= 20; num++ {
		var fizz = num%3 == 0
		var buzz = num%5 == 0
		if fizz && buzz {
			fmt.Println("fizzbuzz")
		} else if fizz {
			fmt.Println("fizz")
		} else if buzz {
			fmt.Println("buzz")
		} else {
			fmt.Println(num)
		}
	}
}

func main() {
	fizzbuzz()
}
