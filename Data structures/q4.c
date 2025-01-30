// Q4: Write a C/C++ program to implement doubly linked list with the
// following function
// (i) insertAtFirst(&head, new_data): This function should insert the new
// data/element at the beginning of the linked list.
// (ii) insertAtEnd(&head, new_data): This function should insert the new
// data/element at the end of the linked list
// (iii) insertAtMiddle(&head, new_data): This function should insert the new
// data/element at the middle of the linked list
// (iv) insertAfterNode(&head, given_node, new_data): This function should
// insert the new data/element after the given node in the linked list.

#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct *node prev;
    struct *node next;
}