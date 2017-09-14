/*
* [200] Number of Islands
*
* https://leetcode.com/problems/number-of-islands
*
* Medium (33.88%)
* Total Accepted:
* Total Submissions:
* Testcase Example:  '["11110","11010","11000","00000"]'
*
* Given a 2d grid map of '1's (land) and '0's (water), count the number of
* islands. An island is surrounded by water and is formed by connecting
* adjacent lands horizontally or vertically. You may assume all four edges of
* the grid are all surrounded by water.
*
* Example 1:
* 11110110101100000000
* Answer: 1
* Example 2:
* 11000110000010000011
* Answer: 3
*
* Credits:Special thanks to @mithmatt for adding this problem and creating all
* test cases.
 */
func numIslands(grid [][]byte) int {
	var ans int = 0
	for x, rows := range grid {
		for y,_ := range rows {
			if grid[x][y] != '0' {
                markLand(grid, x, y)
				ans++
			}
		}
	}
	return ans
}
func markLand(grid [][]byte, x int, y int) {
	if x >= len(grid) || y >= len(grid[0]) || x < 0 || y < 0 {
		return
	}
	if grid[x][y] != '0' {
		grid[x][y] = '0'
		markLand(grid, x+1, y)
		markLand(grid, x-1, y)
		markLand(grid, x, y+1)
		markLand(grid, x, y-1)
	}
}
