#include "lists.h"
/**
 * check_cycle - checks if there is a cycle in a linked list
 * @list: 1st para
 * Return: returns 1 if there is a cycles, else 0
 */
int check_cycle(listint_t *list)
{
listint_t *slow;
listint_t *fast;
if (list == NULL)
{
return (0);
}
if (list->next == NULL)
{
return (0);
}
slow = list;
fast = list->next;
while (fast != NULL && fast != slow)
{
fast = fast->next;
if (fast == NULL)
{
return (0);
}
fast = fast->next;
if (fast == NULL)
{
return (0);
}
slow = slow->next;
}
return (1);
}
