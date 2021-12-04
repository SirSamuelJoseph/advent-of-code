package main

import (
	"math"
	"testing"
)

func TestCountIncreases(t *testing.T) {
	sampleInput := importNumsFromFile("testinput.txt")
	increases := countIncreases(sampleInput)
	if increases != 7 {
		t.Errorf("Incorrect Increase Count; got %d, wanted %d", increases, 7)
	}
}

func TestCountWindowIncreases(t *testing.T) {
	sampleInput := importNumsFromFile("testinput.txt")
	increases := countIncreasesWindow(sampleInput, math.MaxInt32)
	if increases != 5 {
		t.Errorf("Incorrect Increase Count; got %d, wanted %d", increases, 5)
	}
}
