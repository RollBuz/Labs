"""
Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)

"""
Duplicates Not Allowed
Sets cannot have two items with the same value.
"""
#access
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #Note: If the item to remove does not exist, remove() will raise an error.

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") #Note: If the item to remove does not exist, discard() will NOT raise an error.

print(thisset)

#removes randomly
thisset = {"apple", "banana", "cherry"}

x = thisset.pop() #Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

print(x)

print(thisset)

#clear
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#deleate
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

"""
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""
#You can use the | operator instead of the union() method, and you will get the same result.
#The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
#You can use the & operator instead of the intersection() method, and you will get the same result.
#The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

"""
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Shortcut	Description
add()	 	                                Adds an element to the set
clear()	 	                                Removes all the elements from the set
copy()	 	                                Returns a copy of the set
difference()	                -	        Returns a set containing the difference between two or more sets
difference_update()	            -=	        Removes the items in this set that are also included in another, specified set
discard()	 	                            Remove the specified item
intersection()	                &	        Returns a set, that is the intersection of two other sets
intersection_update()	        &=	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                        Returns whether two sets have a intersection or not
issubset()	                    <=	        Returns whether another set contains this set or not
 	                            <	        Returns whether all items in this set is present in other, specified set(s)
issuperset()	                >=	        Returns whether this set contains another set or not
 	                            >	        Returns whether all items in other, specified set(s) is present in this set
pop()	 	                                Removes an element from the set
remove()	 	                            Removes the specified element
symmetric_difference()	        ^	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	        Inserts the symmetric differences from this set and another
union()                        	|	        Return a set containing the union of sets
update()	                    |=	        Update the set with the union of this set and others
"""