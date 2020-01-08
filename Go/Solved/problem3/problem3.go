package main

import "fmt"
import "math"

func main() {
    fmt.Printf("Factor =  %d\n", GreatestPrimeFactor(600851475143))
}

func GreatestPrimeFactor(num int) int {
    max_prime_fac := 1
    num_float := float64(num)
    num_sqrt := int(math.Ceil(math.Sqrt(num_float)))
    for i := num_sqrt; i > 1; i -- {
        if num % i == 0 {
            if IsPrime(i) && i > max_prime_fac{
                return i
            }
            gpfi := GreatestPrimeFactor(i)
            if gpfi > max_prime_fac {
                max_prime_fac = gpfi
            }
        }
    }
    return max_prime_fac
}

func IsPrime(num int) bool {
    for i := 2; i <= int(math.Floor(float64(num) / 2)); i++ {
        if num % i == 0 {
            return false
        }
    }
    return num > 1
}

//  Factor =  6857
