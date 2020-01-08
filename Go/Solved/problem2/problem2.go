package main

import "fmt"

func main() {
    max := 4000000
    sum := 2  // starting at 2 because we incr before we sum in loop body
    term1 := 1
    term2 := 2
	for {
        temp := term2
        term2 = term1 + term2
        term1 = temp

        if term2 > max {
            fmt.Printf("Sum =  %d\n", sum)
            return
        }

        if term2 % 2 == 0 {
            sum += term2
        }
    }
}

// Sum =  4613732
