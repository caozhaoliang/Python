#include <python2.6/Python.h>
#include <iostream>

using namespace std;

void HelloWorld();
void Add();
void TestTransferDict();
void TestClass();


int main()
{
	cout << "call helloworld..."<< endl;
	HelloWorld();
	cout <<"call add()..."<< endl;
	Add();
	cout <<"call testDict..."<<endl;
	TestTransferDict();
	cout <<"call TestClass..."<<endl;
	TestClass();
	return 0;
}

void HelloWorld()
{
	Py_Initialize();
	PyObject* pModule = NULL;
	PyObject* pFunc = NULL;
	string path = "./test";
	PyRun_SimpleString("import sys");
	PyRun_SimpleString( string("sys.path.append(\""+path+"\")").c_str() );

	pModule = PyImport_ImportModule("test_001");
	if(!pModule){
		cout <<"at HelloWorld pModule is NULL."<< endl;
		return ;
	} 
	pFunc = PyObject_GetAttrString(pModule,"HelloWorld");
	if(!pFunc){
		cout <<"at HelloWorld pFunc is NULL."<<endl;
		return ;
	}
	PyEval_CallObject(pFunc,NULL);
	Py_Finalize();	
	return ;
}
void Add()
{
	Py_Initialize();

	PyObject* pModule=NULL;
	PyObject* pFunc=NULL;
	
	string path = "./test";
	PyRun_SimpleString("import sys");
	PyRun_SimpleString( string("sys.path.append(\""+path+"\")").c_str() );
	
	pModule = PyImport_ImportModule("test_001");
	if( !pModule )
	{
		cout <<"at Add() pModule is NULL."<< endl;
		return ;
	}
	pFunc = PyObject_GetAttrString(pModule,"add");
	if(!pFunc)
	{
		cout <<"at Add() pFunc isNULL."<<endl;
		return ;	
	}
	PyObject* pArgs = PyTuple_New(2);
	PyTuple_SetItem(pArgs,0,Py_BuildValue("i",5));
	PyTuple_SetItem(pArgs,1,Py_BuildValue("i",7));

	PyObject* pReturn = NULL;
	pReturn = PyEval_CallObject(pFunc,pArgs);
	int result;
	PyArg_Parse(pReturn,"i",&result);
	cout <<"result :"<<result <<endl;
	Py_Finalize();
}

void TestTransferDict(){
	Py_Initialize();
	PyObject* pModule=NULL;
	PyObject* pFunc=NULL;

	string path = "./test";
	PyRun_SimpleString("import sys");
	PyRun_SimpleString( string("sys.path.append(\""+path+"\")").c_str() );
	
	pModule = PyImport_ImportModule("test_001");
	if(!pModule){
		cout << "at TestTransferDIct pModule is NULL."<<endl;
		return;
	}
	pFunc = PyObject_GetAttrString(pModule,"TestDict");
	if(!pFunc){
		cout <<"at TestTransferDict pFunc is NULL."<<endl;
		return;	
	}

	PyObject* pArgs = PyTuple_New(1);
	PyObject* pDict = PyDict_New();
	PyDict_SetItemString(pDict,"Name",Py_BuildValue("s","Liang"));
	PyDict_SetItemString(pDict,"Age",Py_BuildValue("i",25));
	PyTuple_SetItem(pArgs,0,pDict);
	PyObject *pReturn = NULL;
	pReturn = PyEval_CallObject(pFunc,pArgs);

	int size = PyDict_Size(pReturn);
	cout <<"返回字典大小为："<<size<<endl;
	PyObject* pNewAge = PyDict_GetItemString(pReturn,"Age");
	int nAge;
	PyArg_Parse(pNewAge,"i",&nAge);
	cout <<"True Age:"<<nAge<<endl;
	Py_Finalize();
}
void TestClass()
{
	Py_Initialize();
	PyObject* pModule = NULL;
	PyObject* pFunc = NULL;
	string path = "./test";
	PyRun_SimpleString("import sys");
	PyRun_SimpleString(string("sys.path.append(\""+path+"\")").c_str());
	
	pModule = PyImport_ImportModule("test_001");
	if( !pModule )
	{
		cout << "at TestClass pModule is NULL."<<endl;
		return;	
	}
	pFunc = PyObject_GetAttrString(pModule,"TestDict");
	if( !pFunc ){
		cout << "at TestClass pFunc is NULL."<<endl;
		return;	
	}
	// 获取类
	PyObject* pClassPerson = PyObject_GetAttrString(pModule,"Person");
	if( !pClassPerson ){
		cout <<"at TestClass pClassPerson isNULL."<<endl;
		return;	
	}
	//获取实例
	PyObject* pInstancePerson = PyInstance_New(pClassPerson,NULL,NULL);
	
	char grt[32] = "greet";
	char s[32] ="s";
	/*
	 *  parameter1 对象。参数2 对象的函数名称，参数3 调用函数的传参类型
	 *  参数4 调用函数传参的值。
	 * */
	PyObject_CallMethod(pInstancePerson,grt,s,string("Hello zrror").c_str());

	Py_Finalize();	
}

