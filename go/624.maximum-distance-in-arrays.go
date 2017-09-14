/*
 * [624] Maximum Distance in Arrays
 *
 * https://leetcode.com/problems/maximum-distance-in-arrays
 *
 * Easy (31.68%)
 * Total Accepted:
 * Total Submissions:
 * Testcase Example:  '[[1,2,3],[4,5],[1,2,3]]'
 *
 *
 * Given m arrays, and each array is sorted in ascending order. Now you can
 * pick up two integers from two different arrays (each array picks one) and
 * calculate the distance. We define the distance between two integers a and b
 * to be their absolute difference |a-b|. Your task is to find the maximum
 * distance.
 *
 *
 * Example 1:
 *
 * Input:
 * [[1,2,3],
 * ⁠[4,5],
 * ⁠[1,2,3]]
 * Output: 4
 * Explanation:
 * One way to reach the maximum distance 4 is to pick 1 in the first or third
 * array and pick 5 in the second array.
 *
 *
 *
 * Note:
 *
 * Each given array will have at least 1 number. There will be at least two
 * non-empty arrays.
 * The total number of the integers in all the m arrays will be in the range of
 * [2, 10000].
 * The integers in the m arrays will be in the range of [-10000, 10000].
 *
 *
 */
func maxDistance(arrays [][]int) int {
	res := 0
	minP := arrays[0][0]
	maxP := arrays[0][len(arrays[0])-1]
    for _, array := range arrays[1:] {
		res = Max(res, Abs(array[len(array)-1]-minP), Abs(maxP-array[0]))
		minP = Min(minP, array[0])
		maxP = Max(maxP, array[len(array)-1])
	}
	return res
}
func Min(a ...int) int {
	min := a[0]
	for _, va := range a {
		if va < min {
			min = va
		}
	}
	return min
}
func Max(a ...int) int {
	max := a[0]
	for _, va := range a {
		if va > max {
			max = va
		}
	}
	return max

}
func Abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return 0 - a
	}
}
