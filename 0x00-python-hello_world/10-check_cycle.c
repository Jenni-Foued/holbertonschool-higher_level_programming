#include "lists.h"
/**
 * check_element - check if an adress of an element of a singly
 * linked list is redundant.
 *
 * @elm: adress of the element to be checked.
 * @list: pointer to the head of the list.
 *
 * Return: 0 or 1
 */

int check_element(listint_t *elm, listint_t *list)
{
	int flag = 0;

	while (list)
	{
		if (elm == list)
			flag++;

		if (flag > 1)
			return (1);
		list = list->next;
	}
	return (0);
}

/**
 * check_cycle - checks if a list has a cycle.
 * @list: pointer to head of list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *temp_list;
	int flag = 0;

	temp_list = list;
	if (temp_list == NULL || temp_list->next == NULL)
		return (0);
	while (temp_list)
	{
		flag = check_element(temp_list, list);
		if (flag)
			return (1);
		temp_list = temp_list->next;
	}
	return (0);
}
