package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func importBinariesFromFile(name string) []string {
	report := []string{}
	file, err := os.Open(name)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		binaries := scanner.Text()
		report = append(report, binaries)
	}
	return report
}

func getEpsilonAndGammaRates(binaries []string) (int, int) {
	binaryLength := len(binaries[0])
	totalBinaries := len(binaries)
	gamma := make([]int, binaryLength)
	// Count how many times a 1 is in each spot and store in the gamma array
	for _, binary := range binaries {
		bits := strings.Split(binary, "")

		for pos, bit := range bits {
			num, err := strconv.Atoi(bit)
			if err != nil {
				log.Fatal(err)
			}
			gamma[pos] += num
		}
	}

	// Convert that representation to binary and build epsilon
	epsilonStrings := make([]string, binaryLength)
	gammaStrings := make([]string, binaryLength)
	for index, val := range gamma {
		if val > totalBinaries/2 {
			gammaStrings[index] = "1"
			epsilonStrings[index] = "0"
		} else {
			gammaStrings[index] = "0"
			epsilonStrings[index] = "1"
		}
	}

	//Get it back to string
	gammaString := strings.Join(gammaStrings, "")
	epsilonString := strings.Join(epsilonStrings, "")

	//Convert from binary back to integer
	return convertBinaryStringToInteger(gammaString), convertBinaryStringToInteger(epsilonString)
}

func getOxygenAndCO2Rating(binaries []string) (int, int) {
	binaryLength := len(binaries[0])
	totalBinaries := len(binaries)
	sums := make([]int, binaryLength)
	// Count how many times a 1 is in each spot and store in the gamma array
	for _, binary := range binaries {
		bits := strings.Split(binary, "")

		for pos, bit := range bits {
			num, err := strconv.Atoi(bit)
			if err != nil {
				log.Fatal(err)
			}
			sums[pos] += num
		}
	}

	// Find out which bit is most common in each position
	mostCommon := make([]int, binaryLength)
	for index, val := range sums {
		if val > totalBinaries/2 {
			mostCommon[index] = 1
			// Use 2 to represent ties
		} else if val == totalBinaries/2 {
			mostCommon[index] = 2
		} else {
			mostCommon[index] = 0
		}
	}

	// Get the string representing the ratings
	oxygenString := getRatingFromBinaries(binaries, mostCommon, false)
	co2String := getRatingFromBinaries(binaries, mostCommon, true)

	return convertBinaryStringToInteger(oxygenString), convertBinaryStringToInteger(co2String)
}

func getMostCommonBitFromBinaries(binaries []string, position int) int {
	totalBinaries := float64(len(binaries))
	sum := 0.0

	for _, binary := range binaries {
		bit := string(binary[position])
		num, err := strconv.Atoi(bit)
		if err != nil {
			log.Fatal(err)
		}
		sum += float64(num)
	}
	log.Println(binaries)
	log.Println(sum)

	if sum > totalBinaries/2 {
		return 1
	} else if sum == totalBinaries/2 {
		return 2
	} else {
		return 0
	}
}

func getRatingFromBinaries(binaries []string, mostCommon []int, isCO2 bool) string {
	considered := binaries
	index := 0
	for len(considered) > 1 {
		mostCommonNum := getMostCommonBitFromBinaries(considered, index)
		newConsidereds := make([]string, 0)
		for _, binary := range considered {
			bit := string(binary[index])
			num, err := strconv.Atoi(bit)
			if err != nil {
				log.Fatal(err)
			}
			if isCO2 {
				if mostCommonNum == 0 && num == 1 {
					newConsidereds = append(newConsidereds, binary)
				} else if mostCommonNum == 1 && num == 0 {
					newConsidereds = append(newConsidereds, binary)
				} else if mostCommonNum == 2 && num == 0 {
					newConsidereds = append(newConsidereds, binary)
				}
			} else {
				if mostCommonNum == num {
					newConsidereds = append(newConsidereds, binary)
				} else if mostCommonNum == 2 && num == 1 {
					newConsidereds = append(newConsidereds, binary)
				}
			}
		}
		considered = newConsidereds
		index += 1

	}
	return considered[0]
}

func convertBinaryStringToInteger(binary string) int {
	sum := 0.0
	length := len(binary)
	for index, bit := range binary {
		num, err := strconv.Atoi(string(bit))
		if err != nil {
			log.Fatal(err)
		}
		if num == 1 {
			sum += math.Pow(2, float64(length)-1-float64(index))

		}
	}
	return int(sum)
}

func main() {
	binaries := importBinariesFromFile("input.txt")
	oxygen, co2 := getOxygenAndCO2Rating(binaries)

	log.Println(fmt.Sprintf("Oxygen: %d", oxygen))
	log.Println(fmt.Sprintf("CO2: %d", co2))
	log.Println(fmt.Sprintf("Product: %d", oxygen*co2))
}
