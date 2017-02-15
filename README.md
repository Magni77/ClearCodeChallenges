# ClearCodeChallenges
# Python 3.5

First one was easy. I saw few steps in my head:
	- Check if is even
	- Convert number t o binary
	- Count solders
	- Compare number of soldiers 


The second challenge wasn’t so easy. First thought was: “I had something about is in school.”.  
I googled for shortest path algorithm and decided to used a Dijkstra algorithm . 
First version can handle max 9 fields, and they have to be unique. - That's because I used value of cost as id. 
That's work with data include in example input, but i couldn’t leave it like that.

That's why inspired by stack overflow I created new class Field - making every field unique. That gave me also ability to put information 
about previous move, cost and if is visited in the object.


#Usage
Example

python3 minimum_effort_2.0.py -f data
