package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Matrix struct {
	Rows int
	Cols int
	Values [][]int
	CachedValues map[string]int
}

func getMatrix() *Matrix {
	readFile, err := os.Open("0081_matrix.txt")

	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	readFile.Close()
	matrix := Matrix{}
	for _, line := range fileLines {
		var numbers []int
		numbersStr := strings.Split(line, ",")
		for _, numberStr := range numbersStr {
			i, err := strconv.Atoi(numberStr)
			if err != nil {
				panic(err)
			}
			numbers = append(numbers, i)
		}
		matrix.Values = append(matrix.Values, numbers)
	}
	matrix.Rows = len(matrix.Values)
	matrix.Cols = len(matrix.Values[0])
	matrix.CachedValues = make(map[string]int)

	return &matrix
}

func (m *Matrix) minPathSum(i, j int) int {
	if value, ok := m.CachedValues[fmt.Sprintf("%d-%d", i, j)]; ok {
		return value
	}
	if i == m.Rows - 1 && j == m.Cols - 1 {
		return m.Values[i][j]
	}

	if i == m.Rows - 1 {
		val := m.Values[i][j] + m.minPathSum(i, j + 1)
		m.CachedValues[fmt.Sprintf("%d-%d", i, j)] = val
		return val
	}

	if j == m.Cols - 1 {
		val := m.Values[i][j] + m.minPathSum(i + 1, j)
		m.CachedValues[fmt.Sprintf("%d-%d", i, j)] = val
		return val
	}
	right := m.Values[i][j] + m.minPathSum(i, j + 1)
	down := m.Values[i][j] + m.minPathSum(i + 1, j)

	minimum := 0
	if right < down {
		minimum = right
	} else {
		minimum = down
	}
	m.CachedValues[fmt.Sprintf("%d-%d", i, j)] = minimum
	return minimum
}

func main() {
	matrix := getMatrix()

	fmt.Println(matrix.minPathSum(0, 0))
}
