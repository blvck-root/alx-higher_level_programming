#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: pointer to linked list
 * Return: 0 if there is no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next  != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
