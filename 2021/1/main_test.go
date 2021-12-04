package main

import (
	"math"
	"testing"
)

func TestCountIncreases(t *testing.T) {

	tests := map[string]struct {
		input     []int
		increases int
	}{
		"testinput": {
			input:     importNumsFromFile("testinput.txt"),
			increases: 7,
		},
		"emptyInput": {
			input:     []int{},
			increases: 0,
		},
	}

	for name, testcase := range tests {
		t.Run(name, func(t *testing.T) {
			count := countIncreases(testcase.input)
			if count != testcase.increases {
				t.Errorf("Incorrect Increase Count; got %d, wanted %d", count, testcase.increases)
			}
		})
	}
}

func TestCountWindowIncreases(t *testing.T) {
	tests := map[string]struct {
		input     []int
		increases int
	}{
		"testinput": {
			input:     importNumsFromFile("testinput.txt"),
			increases: 5,
		},
		"emptyInput": {
			input:     []int{},
			increases: 0,
		},
	}

	for name, testcase := range tests {
		t.Run(name, func(t *testing.T) {
			count := countIncreasesWindow(testcase.input, math.MaxInt32)
			if count != testcase.increases {
				t.Errorf("Incorrect Increase Count; got %d, wanted %d", count, testcase.increases)
			}
		})
	}
}
