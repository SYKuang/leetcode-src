/*
* [203] Remove Linked List Elements
*
* https://leetcode.com/problems/remove-linked-list-elements
*
* Easy (32.05%)
* Total Accepted:
* Total Submissions:
* Testcase Example:  '[1,2,6,3,4,5,6]\n6'
*
* Remove all elements from a linked list of integers that have value val.
*
* Example
* Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
* Return: 1 --> 2 --> 3 --> 4 --> 5
*
*
* Credits:Special thanks to @mithmatt for adding this problem and creating all
* test cases.
 */
/**
* Definition for singly-linked list.
* type ListNode struct {
    *     Val int
    *     Next *ListNode
    * }
*/
func removeElements(head *ListNode, val int) *ListNode {
	var newHead ListNode
	newHead.Next = head
	head = &newHead
	for head.Next != nil {
		if head.Next.Val == val {
			head.Next = head.Next.Next
		} else {
			head = head.Next
		}
	}
	return newHead.Next
}
