package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

var BOARD_SIZE = 5

type bingoBoard struct {
	board [][]int
}

type GameState struct {
	boards []bingoBoard
	draws  []int
}

func importBingoCardFromFile(name string) GameState {
	state := GameState{
		boards: []bingoBoard{},
		draws:  []int{},
	}
	file, err := os.Open(name)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if len(state.draws) == 0 {
			drawString := scanner.Text()
			drawStringSlice := strings.Split(drawString, ",")
			var draws []int
			for _, numString := range drawStringSlice {
				if numString != "" {
					num, err := strconv.Atoi(numString)
					if err != nil {
						log.Fatal(err)
					}
					draws = append(draws, num)
				}

			}
			state.draws = draws
		} else {
			var board bingoBoard
			board.board = make([][]int, BOARD_SIZE)
			for i := 0; i < BOARD_SIZE; i++ {
				_ = scanner.Scan()
				line := scanner.Text()
				lineSlice := strings.Fields(line)
				row := make([]int, BOARD_SIZE)
				for index, val := range lineSlice {
					num, err := strconv.Atoi(val)
					if err != nil {
						log.Fatal(err)
					}
					row[index] = num
				}
				board.board[i] = row
			}
			state.boards = append(state.boards, board)
		}
	}
	return state
}

func hasAnyBoardWon(state GameState, drawn []int) int {
	victoryBoard := false
	for ind, board := range state.boards {
		victoryBoard = victoryBoard || hasBoardWon(board, drawn)
		if victoryBoard {
			return ind
		}
	}
	return -1
}

func hasBoardWon(board bingoBoard, drawn []int) bool {
	claimed := make([][]bool, BOARD_SIZE)
	for rowInd, row := range board.board {
		claimed[rowInd] = make([]bool, BOARD_SIZE)
		for colInd, val := range row {
			check := false
			for _, drawn := range drawn {
				if drawn == val {
					check = true
				}
			}
			claimed[rowInd][colInd] = check
		}
	}
	// Check for row victory
	for _, cRow := range claimed {
		rowVictory := true
		for _, elem := range cRow {
			rowVictory = rowVictory && elem
		}
		if rowVictory {
			return true
		}
	}

	// Check for column victory
	for i := 0; i < BOARD_SIZE; i++ {
		columnVictory := true
		for _, row := range claimed {
			columnVictory = columnVictory && row[i]
		}
		if columnVictory {
			return true
		}
	}

	// Check for diagonal victory
	for i := 0; i < BOARD_SIZE; i++ {
		downwardDiagonalVictory := true
		upwardDiagonalVictory := true
		for _, row := range claimed {
			downwardDiagonalVictory = downwardDiagonalVictory && row[i]
			upwardDiagonalVictory = upwardDiagonalVictory && row[BOARD_SIZE-1-i]
		}
		if upwardDiagonalVictory || downwardDiagonalVictory {
			return true
		}
	}
	return false
}

func getBoardScore(board bingoBoard, drawn []int) int {
	sum := 0
	for _, row := range board.board {
		for _, val := range row {
			valDrawn := false
			for _, num := range drawn {
				if num == val {
					valDrawn = true
				}
			}
			if !valDrawn {
				sum += val
			}
		}
	}
	return sum * drawn[len(drawn)-1]
}

func main() {
	state := importBingoCardFromFile("input.txt")
	score := getLastBoardLosingScore(state)
	log.Println(score)
}

func getLastBoardLosingScore(state GameState) int {
	var drawn []int
	for len(state.boards) > 1 {
		for -1 == hasAnyBoardWon(state, drawn) {
			drawn = append(drawn, state.draws[len(drawn)])
		}
		index := hasAnyBoardWon(state, drawn)
		contenders := make([]bingoBoard, 0)
		for ind, contender := range state.boards {
			if ind != index {
				contenders = append(contenders, contender)
			}
		}
		state.boards = contenders
	}
	// Now finish this board
	for -1 == hasAnyBoardWon(state, drawn) {
		drawn = append(drawn, state.draws[len(drawn)])
	}
	return getBoardScore(state.boards[0], drawn)
}
