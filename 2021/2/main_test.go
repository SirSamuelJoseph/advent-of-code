package main

import (
	"testing"
)

func TestGetPosition(t *testing.T) {

	tests := map[string]struct {
		input    []string
		position int
	}{
		"testinput": {
			input:    importDirectionsFromFile("testinput.txt"),
			position: 150,
		},
		"emptyInput": {
			input:    []string{},
			position: 0,
		},
	}

	for name, testcase := range tests {
		t.Run(name, func(t *testing.T) {
			pos := getPositionFromDirections(testcase.input)
			if pos != testcase.position {
				t.Errorf("Incorrect Position; got %d, wanted %d", pos, testcase.position)
			}
		})
	}
}

func TestGetComplexPosition(t *testing.T) {

	tests := map[string]struct {
		input    []string
		position int
	}{
		"testinput": {
			input:    importDirectionsFromFile("testinput.txt"),
			position: 900,
		},
		"emptyInput": {
			input:    []string{},
			position: 0,
		},
	}

	for name, testcase := range tests {
		t.Run(name, func(t *testing.T) {
			pos := getComplexPositionFromDirections(testcase.input)
			if pos != testcase.position {
				t.Errorf("Incorrect Position; got %d, wanted %d", pos, testcase.position)
			}
		})
	}
}
