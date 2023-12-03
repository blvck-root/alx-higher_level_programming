#include "lists.h"

/**
 * reverse_list - reverse linked list
 * @head: pointer to linked lisr=t
 * Return: reversed linked list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *curr = head, *next;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return prev;
}	

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to linked list
 * Return: 1 if linked list is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = (*head)->next;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	fast = reverse_list(slow->next);
	slow = *head;
	while (fast)
	{
		if (fast->n != slow->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
