#include "lists.h"
#include <stdlib.h>

/**
 * reversed - return reversed linked list
 * @head: pointer to linked lisr=t
 * Return: reversed linked list
 */
listint_t *reversed(listint_t *head)
{
	listint_t *prev = NULL, *rev;

	while (head)
	{
		rev = malloc(sizeof(listint_t));
		if (rev == NULL)
		{
			free_listint(rev);
			return (NULL);
		}

		rev->n = head->n;
		rev->next = prev;
		head = head->next;
		prev = rev;
	}
	return (rev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to linked list
 * Return: 1 if linked list is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = (*head)->next;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	fast = reversed(slow->next);
	if (fast == NULL)
		return (-1);

	slow = *head;
	while (fast)
	{
		if (fast->n != slow->n)
		{
			free_listint(fast);
			return (0);
		}
		slow = slow->next;
		fast = fast->next;
	}
	free_listint(fast);
	return (1);
}
