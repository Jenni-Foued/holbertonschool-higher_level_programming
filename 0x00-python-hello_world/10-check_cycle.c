#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle.
 *
 * @list: pointer to head of list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *first_pointer = list, *second_pointer = list;

	while (first_pointer && second_pointer && second_pointer->next)
	{
		first_pointer = first_pointer->next;
		second_pointer = second_pointer->next->next;
		if (first_pointer == second_pointer)
			return (1);
	}
	return (0);
}
