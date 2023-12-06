#include "lists.h"
/**
 * is_palindrome - palindrome function
 * @head: ptr to ptr
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
int sum, sum0, i, num, num0;
listint_t *current;
listint_t *current0;
sum = 0;
sum0 = 0;
num0 = 2;
if (*head == NULL)
{
return (1); }
num = 0;
current = *head;
while (current != NULL)
{
current = current->next;
++num; }
if (num % 2 != 0)
{
num0 = num;
num = num - 1; }
current = *head;
current0 = *head;
for (i = 1; i <= num / 2; ++i)
{
current0 = current0->next; }
if (num0 % 2 != 0)
{
current0 = current0->next; }
for (i = 0; i < num / 2; ++i)
{
sum += current->n;
sum0 += current0->n;
current = current->next;
current0 = current0->next; }
if (sum != sum0)
{
return (0); }
return (1); }
