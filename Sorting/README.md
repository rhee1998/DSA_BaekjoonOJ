# **Sorting Algorithms**
## **Merge Sort**
### **1. Simple Merge Sort**
#### **Algorithm**
* *divide and conquer*

#### **Time Complexity**
* Average : $\cal{O}$ $(N \log N)$
* Worst case : $\cal{O}$ $(N \log N)$

#### `def MergeSort(A)`
* Input(s)
  * `A` : Array or list to sort
* Output(s)
  * `R` : Sorted array or list

### **2. Generalized Merge Sort**
* Generalized sorting with generalized function `Compare(x, y)`

#### `def Compare(x, y)`
* Input(s)
  * `x` & `y` : tuples of lists to compare
* Output(s)
  * `True` if `x` is equal to or in front of `y`, otherwise `False`
 
#### `def GeneralizedMergeSort(A)`
* Input(s)
  * `A` : Array or list to sort
* Output(s)
  * `R` : Sorted array or list
