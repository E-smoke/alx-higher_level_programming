#include "lists.h"
/**
 * print_python_list_info - prints info about a list
 * @p: the list
 */
void print_python_list_info(PyObject *p)
{
if (!PyList_Check(p))
{
printf("Invalid object: Not a Python list\n");
return;
}
Py_ssize_t list_length = PyList_Size(p);
printf("[*] Size of the Python List = %zd\n", list_length);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
for (Py_ssize_t i = 0; i < list_length; ++i)
{
PyObject *item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
