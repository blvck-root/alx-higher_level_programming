#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print basic info about Python lists
 * @p: Python object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	PyObject *element;
	Py_ssize_t i, len = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < len; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
