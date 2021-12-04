package main

import (
	"testing"
)

func TestBingoScore(t *testing.T) {

	tests := map[string]struct {
		state GameState
		score int
	}{
		"testinput": {
			state: importBingoCardFromFile("testinput.txt"),
			score: 4512,
		},
	}

	for name, testcase := range tests {
		t.Run(name, func(t *testing.T) {
			score := getFirstBoardWinningScore(testcase.state)
			if score != testcase.score {
				t.Errorf("Incorrect Value; got %d, wanted %d", score, testcase.score)
			}
		})
	}
}
