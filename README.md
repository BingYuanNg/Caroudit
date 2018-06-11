# Caroudit
This project is created using python with flask framemork.
# Installation
1. Clone the project
```
git@github.com:BingYuanNg/Caroudit.git
```
2. Change directory
```
cd Caroudit
```
2. Install required dependency
```
pip install -r requirement.txt
```
3. Run test
```
python -m unittest
```
4.
```
python run.py
```
# Path taken
### Storing Topics: 

Hashtable. There are advantages and disadvantage in using hashtable.
One of the major advantage will be fast read and write speed.

### Top Topics: 

I've created a list of index to store the sorted result. The sort that I've decided to use is an Insertion Sort. Since the top 20 index will always be a partial sorted list, insertion sort only does one insert. Which would make the algorithm O(n), in fact less than n can be achieve on average case if optimization is done.
