# Sorting algorithms

We need sometimes order a list of elements based on a criteria, like ascending or descending. Efficient sorting is important for efficiency of other algorithms on top of that such as Binary search.

## Quick sort

It takes a element as a pivot and separate the minor and the major elements. Recursively repeat the same process for the list of minor and the list of major. At the end it concatenate the list of minor (ordered), the pivot and the list of major(ordered).

## Merge sort

It uses divides and conquer approach to divide the entire list of elements into n *sub-lists* each one containing one element. Later merging each list sorting it's elements until just one list sorted result.

## Selection sort
It starts from first position and find the min value in the array, if it found a min value it swap the values from their indexes and repeadtly go to the next position to find the min value in the rest of the array.
