/*
 * [201] Bitwise AND of Numbers Range
 *
 * https://leetcode.com/problems/bitwise-and-of-numbers-range
 *
 * Medium (33.73%)
 * Total Accepted:
 * Total Submissions:
 * Testcase Example:  '0\n0'
 *
 * Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
 * of all numbers in this range, inclusive.
 *
 *
 * For example, given the range [5, 7], you should return 4.
 *
 *
 * Credits:Special thanks to @amrsaqr for adding this problem and creating all
 * test cases.
 */
func rangeBitwiseAnd(m int, n int) int {
	var shift uint = 0
	for m != n {
		m = m >> 1
		n = n >> 1
		shift++
	}
	return m << shift
}
