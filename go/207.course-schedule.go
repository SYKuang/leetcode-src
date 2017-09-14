/*
* [207] Course Schedule
*
* https://leetcode.com/problems/course-schedule
*
* Medium (31.62%)
* Total Accepted:
* Total Submissions:
* Testcase Example:  '2\n[[1,0]]'
*
*
* There are a total of n courses you have to take, labeled from 0 to n - 1.
*
* Some courses may have prerequisites, for example to take course 0 you have
* to first take course 1, which is expressed as a pair: [0,1]
*
*
* Given the total number of courses and a list of prerequisite pairs, is it
* possible for you to finish all courses?
*
*
* For example:
* 2, [[1,0]]
* There are a total of 2 courses to take. To take course 1 you should have
* finished course 0. So it is possible.
*
* 2, [[1,0],[0,1]]
* There are a total of 2 courses to take. To take course 1 you should have
* finished course 0, and to take course 0 you should also have finished course
* 1. So it is impossible.
*
* Note:
*
* The input prerequisites is a graph represented by a list of edges, not
* adjacency matrices. Read more about how a graph is represented.
* You may assume that there are no duplicate edges in the input
* prerequisites.
*
*
*
* click to show more hints.
*
* Hints:
*
* This problem is equivalent to finding if a cycle exists in a directed graph.
* If a cycle exists, no topological ordering exists and therefore it will be
* impossible to take all courses.
* Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera
* explaining the basic concepts of Topological Sort.
*
*
 */
func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := make([][]bool, numCourses)
	visit := make([]bool, numCourses)
	recStack := make([]bool, numCourses)
	for i := range graph {
		graph[i] = make([]bool, numCourses)
	}
	for row := 0; row < numCourses; row++ {
		for col := 0; col < numCourses; col++ {
			graph[row][col] = false
		}
	}
	// graph[i][j]=true means there is an edge from node i to node j
	for i := range prerequisites {
		graph[prerequisites[i][1]][prerequisites[i][0]] = true
	}
	// Initialize visit
	for i := range visit {
		visit[i] = false
		recStack[i] = false
	}
	for node, edges := range graph {
		for edge := range edges {
			if edges[edge] && !visit[node] {
				if DFS(node, graph, visit, recStack) {
					return false
				}
			}
		}
	}
	return true
}
func DFS(node int, graph [][]bool, visit []bool, recStack []bool) bool {
	visit[node] = true
	//Mark recStack for one DFS search
	recStack[node] = true
	for i, value := range graph[node] {
		if value {
			if !visit[i] && DFS(i, graph, visit, recStack) {
				return true
			} else if recStack[i] {
				// When recStack[i] is true means this node has been visit in this DFS search
				return true
			}
		}
	}
	recStack[node] = false
	return false
}
