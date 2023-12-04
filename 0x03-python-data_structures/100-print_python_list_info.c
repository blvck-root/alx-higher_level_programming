#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print basic info about Python lists
 * @p: Python object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, len = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", Py_REFCNT(p));

	for (i = 0; i < len; i++)
	{
		PyObject *element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
