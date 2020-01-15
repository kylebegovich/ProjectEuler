package main

import "fmt"


// Taken from golang's playground here: https://play.golang.org/p/9U22NfrXeq


// Send the sequence 2, 3, 4, ... to channel 'ch'.
func Generate(ch chan<- int) {
	for i := 2; ; i++ {
		ch <- i // Send 'i' to channel 'ch'.
	}
}

// Copy the values from channel 'in' to channel 'out',
// removing those divisible by 'prime'.
func Filter(in <-chan int, out chan<- int, prime int) {
	for {
		i := <-in // Receive value from 'in'.
		if i%prime != 0 {
			out <- i // Send 'i' to 'out'.
		}
	}
}

// The prime sieve: Daisy-chain Filter processes.
func main() {
	ch := make(chan int) // Create a new channel.
	go Generate(ch)      // Launch Generate goroutine.
    prime := 0
	for i := 0; i < 10001; i++ {
		prime = <-ch
		ch1 := make(chan int)
		go Filter(ch, ch1, prime)
		ch = ch1
	}
    fmt.Println("10001st prime = %d\n", prime)
}

// 10001st prime = 104743
