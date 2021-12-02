package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func importDirectionsFromFile(name string) []string {
	directions := []string{}
	file, err := os.Open(name)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		comm := scanner.Text()
		directions = append(directions, comm)
	}
	return directions
}

func getPositionFromDirections(dirs []string) {
	depth := 0
	horizontal := 0

	for _, dir := range dirs {
		// Split the direction into cardinality [0] and value [1]
		components := strings.Split(dir, " ")
		num, err := strconv.Atoi(components[1])
		if err != nil {
			log.Fatal(err)
		}
		switch components[0] {
		case "forward":
			horizontal += num
		case "down":
			depth += num
		case "up":
			depth -= num
		}
	}
	log.Println(fmt.Sprintf("Depth: %d", depth))
	log.Println(fmt.Sprintf("Horizontal: %d", horizontal))
	log.Println(fmt.Sprintf("Product: %d", depth*horizontal))
}

func getComplexPositionFromDirections(dirs []string) {
	depth := 0
	horizontal := 0
	aim := 0

	for _, dir := range dirs {
		components := strings.Split(dir, " ")
		num, err := strconv.Atoi(components[1])
		if err != nil {
			log.Fatal(err)
		}
		switch components[0] {
		case "forward":
			horizontal += num
			depth += aim * num
		case "down":
			aim += num
		case "up":
			aim -= num
		}
	}
	log.Println(fmt.Sprintf("Depth: %d", depth))
	log.Println(fmt.Sprintf("Horizontal: %d", horizontal))
	log.Println(fmt.Sprintf("Product: %d", depth*horizontal))
}

func main() {
	directions := importDirectionsFromFile("input.txt")
	getComplexPositionFromDirections(directions)
}
