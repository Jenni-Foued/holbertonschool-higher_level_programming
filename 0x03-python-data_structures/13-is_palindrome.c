#include "lists.h"
#include <stdlib.h>

/**
 * list_len - Calculate the number of elements.
 *
 * @h: Pointer to a list.
 *
 * Return: Integer.
 **/

int list_len(const listint_t *h)
{

	int counter = 0;

	while (h)
	{
		counter++;
		h = h->next;
	}
	return (counter);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: pointer to the first node of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	int *reversed_list, i, len;
	listint_t *temp;

	if (*head == NULL)
		return (1);
	temp = *head;
	len = list_len(temp);

	reversed_list = malloc(sizeof(int) * len);
	temp = *head;
	i = len - 1;
	for (; i >= 0; i--)
	{
		reversed_list[i] = temp->n;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < len; i++)
	{
		if (reversed_list[i] != temp->n)
		{
			return (0);
			free(reversed_list);
		}
		temp = temp->next;
	}
	free(reversed_list);
	return (1);
}
