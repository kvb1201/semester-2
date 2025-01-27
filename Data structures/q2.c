//Q2: Given an unsorted linked list of n nodes, remove duplicates from the list.
#include<stdio.h>
#include<stdlib.h>

typedef struct node{
	int data;
	struct node* next;
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
    int i;
    for( i =0; i <n; i++)
    {
        int num;
        printf("Enter the number: ");
        scanf("%d",&num);
        InsertatEnd(head,num);
        
    }
    printList(head);
	int unique =0;
	int uniqueEle[n];
    
    for(i=0; i <n; i++)
    {
		int found =0;
		node *temp = head;
	
		for(int j =0; j < unique; j++)
		{
			if(temp->next->data== uniqueEle[j])
			{
				found =1;
				break;
			}
		}
		
		if(found == 1)
		{
			temp = temp ->next->next;
		}
		else
		{
		    uniqueEle[unique] = temp->next->data;
		    unique ++;
		}
    	
	}
	printf("\n");
	printList(head);
    
    
}