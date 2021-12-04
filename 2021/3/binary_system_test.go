package main

import (
	"testing"
)

func TestGetPowerConsumption(t *testing.T) {

	tests := map[string]struct {
		input []string
		value int
	}{
		"testinput": {
			input: importBinariesFromFile("testinput.txt"),
			value: 198,
		},
	}

	for name, testcase := range tests {
		t.Run(name, func(t *testing.T) {
			eps, gam := getEpsilonAndGammaRates(testcase.input)
			if eps*gam != testcase.value {
				t.Errorf("Incorrect Value; got %d, wanted %d", eps*gam, testcase.value)
			}
		})
	}
}

func TestGetLifeSupportRating(t *testing.T) {

	tests := map[string]struct {
		input []string
		value int
	}{
		"testinput": {
			input: importBinariesFromFile("testinput.txt"),
			value: 230,
		},
	}

	for name, testcase := range tests {
		t.Run(name, func(t *testing.T) {
			ox, co := getOxygenAndCO2Rating(testcase.input)
			if ox*co != testcase.value {
				t.Errorf("Incorrect Value; got %d, wanted %d", ox*co, testcase.value)
			}
		})
	}
}
