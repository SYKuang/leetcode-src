/*
* [204] Count Primes
*
* https://leetcode.com/problems/count-primes
*
* Easy (26.45%)
* Total Accepted:
* Total Submissions:
* Testcase Example:  '0'
*
* Description:
* Count the number of prime numbers less than a non-negative number, n.
*
* Credits:Special thanks to @mithmatt for adding this problem and creating all
* test cases.
 */

//Reference : http://www.wikiwand.com/en/Sieve_of_Eratosthenes
func countPrimes(n int) int {
	list := make([]bool, n)
	for i := range list {
		list[i] = true
	}
	for i := 2; i < n; i++ {
		if list[i] {
			for j := i * 2; j < n; j = j + i {
				list[j] = false
			}
		}
	}
	res := 0
	for i := 2; i < n; i++ {
		if list[i] {
			res++
		}
	}
	return res
}
