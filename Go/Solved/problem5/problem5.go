package main

import "fmt"

func main() {
    num := 2520
    for {
        if num % 11 == 0 && num % 13 == 0 && num % 14 == 0 && num % 16 == 0 && num % 17 == 0 && num % 18 == 0 && num % 19 == 0 {
            fmt.Printf("Least common divisor = %d\n", num)
            return
        }
        num += 20
    }
}


// Least common divisor = 232792560
