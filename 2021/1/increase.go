package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

func countIncreases(nums []int) int {
	if len(nums) > 1 {
		increased := nums[0] < nums[1]
		remainingCount := countIncreases(nums[1:])
		if increased {
			return 1 + remainingCount
		} else {
			return remainingCount
		}

	}
	return 0
}

func countIncreasesWindow(nums []int, prevValue int) int {
	if len(nums) > 2 {
		// Only have to compare the previous value to the last number in this window
		// Middle two will have the same value for both
		increased := prevValue < nums[2]
		remainingCount := countIncreasesWindow(nums[1:], nums[0])
		if increased {
			return 1 + remainingCount
		} else {
			return remainingCount
		}
	}
	return 0
}

func importNumsFromFile(name string) []int {
	numbers := []int{}
	file, err := os.Open(name)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		numbers = append(numbers, num)
	}
	return numbers
}

func main() {
	nums := importNumsFromFile("input.txt")
	count := countIncreases(nums)
	log.Println(fmt.Sprintf("Increases: %d", count))
	countWindows := countIncreasesWindow(nums, math.MaxInt32)
	log.Println(fmt.Sprintf("Window Increases: %d", countWindows))
}
