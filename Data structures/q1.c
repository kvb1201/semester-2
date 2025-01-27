//Q1: Given a linked list of n nodes and an integer k, write a function to rotate the
//linked list counter clockwise by k nodes.

#include <stdio.h>
#include<stdlib.h>

typedef struct node {
	int data; 
	struct node *next;
}node;


void InsertatEnd(node *head, int num)
{
	node *temp = head;
	node *newNode = (node*)malloc(sizeof(node));
	newNode->data = num;
	newNode->next = NULL;
	while(temp->next != NULL)
	{
		temp = temp->next;
	}
	temp->next = newNode;
}

void DeleteFromBegin(node *head)
{
    node *temp = head;
    temp ->next = temp->next->next;
    
    
}



void printList(node *head)
{
	node *temp = head;
	while (temp != NULL)
	{
		printf("%d-->",temp->data);
		temp = temp->next;
	}
}

int main()
{
	node * head = (node *)malloc(sizeof(node));
	int n;
    
    printf("Taking input for the linked List:\n");
    printf("Enter the number of entries; ");
    scanf("%d",&n);
    for(int i =0; i <n; i++)
    {
        int num;
        printf("Enter the number: ");
        scanf("%d",&num);
        InsertatEnd(head,num);
        
    }
    
    printList(head);
    
    int k;
    printf("Enter the number of counter-clockwise rotation to be performed: ");
    scanf("%d",&k);
    
    
    
    
    for(int i=0; i <k; i++)
    {
        node*temp = head;
        temp = temp->next;
        InsertatEnd(head,temp->data);
        DeleteFromBegin(head);
    }
    
    
    
	printList(head);
	
	return 0;
}

