package main

import "testing"

func TestCountIncreases(t *testing.T) {
	sampleInput := []int{1, 2, 3}
	increases := countIncreases(sampleInput)
	if increases != 2 {
		t.Errorf("Incorrect Increase Count; got %d, wanted %d", increases, 2)
	}
}
