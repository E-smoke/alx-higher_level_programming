#include "lists.h"
/**
 * insert_node - insert node in a sorted singly linked list
 * @head: ptr to ptr
 * @number: the number
 * Return: a ptr to the new node created
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *current;
listint_t *ca = NULL;
new_node = (listint_t *)malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL); }
if (head == NULL)
{
free(new_node);
return (NULL); }
if (*head == NULL)
{
*head = new_node;
new_node->next = NULL;
new_node->n = number; }
if((*head)->n > number)
{
new_node->next = *head;
*head = new_node;
new_node->n = number;
return(new_node); }
current = *head;
while ((current->next) != NULL)
{
if ((current->n) > number)
{
new_node->next = current;
new_node->n = number;
ca->next = new_node;
return (new_node); }
ca = current;
current = current->next; }
if (current->n > number)
{
new_node->next = current;
new_node->n = number;
ca->next = new_node;
return (new_node); }
else
{
new_node->next = NULL;
new_node->n = number;
current->next = new_node; }
return (new_node); }
