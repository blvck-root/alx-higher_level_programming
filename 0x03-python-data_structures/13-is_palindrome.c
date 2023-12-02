#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to linked list
 * Return: 1 if linked list is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head;
	int *right, i, mid, len = 0;

	while (node != NULL)
	{
		node = node->next;
		++len;
	}

	mid = len / 2;
	right = (int *) malloc(mid * sizeof(int));
	if (right == NULL)
		return (-1);

	node = *head;
	for (i = mid - 1; i >= 0; i--)
	{
		right[i] = node->n;
		node = node->next;
	}

	if (len % 2 == 1)
		node = node->next;

	for (i = 0;  i < mid; i++)
	{
		if (right[i] != node->n)
		{
			free(right);
			return (0);
		}
		node = node->next;
	}
	free(right);
	return (1);
}
