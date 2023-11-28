#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to the head of the linked list
 * @number: integer
 * Return: what does your_function return
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node;

	if (head == NULL)
		return (NULL);

	new = (listint_t *) malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}

	node = *head;
	if (node->n > number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node->next)
	{
		if (node->next->n > number)
		{
			new->next = node->next;
			node->next = new;
			return (new);
		}
		node = node->next;
	}
	node->next = new;
	new->next = NULL;
	return (new);
}
