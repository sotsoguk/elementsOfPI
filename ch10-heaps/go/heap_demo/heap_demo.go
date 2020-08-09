package main

import (
	"container/heap"
	"fmt"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
	// old := *h
	n := len(*h)
	// x := old[n-1]
	// *h = old[0 : n-1]
	// return x
	x := (*h)[0]
	*h = (*h)[0 : n-1]
	return x

}

func main() {
	h := &IntHeap{2, 4, 10, 3, 5}
	heap.Init(h)
	heap.Push(h, 3)
	fmt.Printf("min: %d\n", (*h)[0])
	// for i := 0; i < h.Len(); i++ {
	// 	fmt.Print((*h)[i])
	// }
	for h.Len() > 0 {
		fmt.Printf("%d ", heap.Pop(h))
	}
	fmt.Println()
}
