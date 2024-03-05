package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
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
	readFile, err := os.Open("0082_matrix.txt")

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

func (m *Matrix) minPathSum(i, j int, canGoUp, canGoDown bool) int {
	if value, ok := m.CachedValues[fmt.Sprintf("%d-%d-%t-%t", i, j, canGoUp, canGoDown)]; ok {
		return value
	}
	if j == m.Cols - 1 {
		return m.Values[i][j]
	}

	right := -1
	up := -1
	down := -1
	if i > 0 && canGoUp {
		up = m.Values[i][j] + m.minPathSum(i - 1, j, true, false)
	}
	if i < m.Rows - 1 && canGoDown {
		down = m.Values[i][j] + m.minPathSum(i + 1, j, false, true)
	}
	right = m.Values[i][j] + m.minPathSum(i, j + 1, true, true)

	minimum := right
	if up != -1 && up < minimum {
		minimum = up
	}
	if down != -1 && down < minimum {
		minimum = down
	}
	m.CachedValues[fmt.Sprintf("%d-%d-%t-%t", i, j, canGoUp, canGoDown)] = minimum
	return minimum
}

func main() {
	matrix := getMatrix()
	var allValues []int
	for i := 0; i < matrix.Rows; i++ {
		allValues = append(allValues, matrix.minPathSum(i, 0, false, false))
	}

	fmt.Println(slices.Min(allValues))
}
