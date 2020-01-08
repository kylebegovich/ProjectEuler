package main

import "fmt"
import "strconv"

func main() {
    max_pal := 0
    for i := 999; i > 1; i -- {
        for j := i; j > 1; j -- {
            prod := i * j
            if prod < max_pal {
                break
            }
            if IsPal(prod) && prod > max_pal {
                max_pal = prod
            }
        }
    }

    fmt.Printf("Max pal product = %d\n", max_pal)
}

func IsPal(num int) bool {
    str := strconv.Itoa(num)
    str_len := len(str)
    for i := 0; i < str_len / 2; i ++ {
        if !(str[i] == str[str_len - i - 1]) {
            return false
        }
    }
    return true
}

// Max pal product = 906609
