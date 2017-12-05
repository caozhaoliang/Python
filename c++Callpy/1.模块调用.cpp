#include <python2.6/Python.h>
#include <iostream>

using namespace std;


int main()
{
	Py_Initialize();
	
	string path = "./test";
	string chdir_cmd = string("sys.path.append(\"")+path+"\")";	
	const char* cstr_cmd = chdir_cmd.c_str();
	PyRun_SimpleString("import sys");
	PyRun_SimpleString(cstr_cmd);

	// 加载模块
	PyObject* moduleName = PyString_FromString("test_001");
	PyObject* pModule = PyImport_Import(moduleName);
	if(!pModule) //加载模块失败
	{
		cout << "[error] python get module failed"<<endl;
		return -1;	
	}
	cout << "[info] Python get module succeed."<<endl;

	PyObject* pv = PyObject_GetAttrString(pModule,"fun_add");
	if( !pv ){
		cout << "pv is null."<<endl;	
		return -1;
	}
	if(!PyCallable_Check(pv)){
		cout <<" nuable ."<<endl;	
		return -1;
	}
	//if(!pv || !PyCallable_Check(pv)){
	//	cout << "[error] can't find function(test_add)"<<endl;
	//	return -2;	
	//}
	cout<<"[info] Get function (test_add) succeed."<<endl;

	PyObject* args = PyTuple_New(2);
	PyObject* arg1 = PyInt_FromLong(4);
	PyObject* arg2 = PyInt_FromLong(3);

	PyTuple_SetItem(args,0,arg1);
	PyTuple_SetItem(args,1,arg2);

	PyObject* pRet = PyObject_CallObject(pv,args);
	if(pRet){
		long result = PyInt_AsLong(pRet);
		cout <<"result:"<< result<< endl;	
	}
	Py_Finalize();

	return 0;
}

