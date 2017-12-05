#include <iostream>
#include <python2.6/Python.h>
int main()
{
	Py_Initialize();
	if(!Py_IsInitialized()){
		return -1;	
	}	
	PyRun_SimpleString("import sys");
	
	//PyRun_SimpleString("sys.argv[ 'arg1',' arg2' ]");
	int argc =2;
	char* argv[2];
	argv[0] = (char*)"arg1";
	argv[1] = (char*)"arg2";
	PySys_SetArgv(argc,argv);

	if(PyRun_SimpleString("execfile('./13.主函数.py')")== NULL)
	{
		return -1;	
	}
	Py_Finalize();
	return 0;
}
