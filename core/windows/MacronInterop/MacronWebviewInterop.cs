using System;
using System.ComponentModel;
using System.Runtime.InteropServices;
using System.Security.Permissions;

namespace MacronWebviewInterop
{
    public interface IMacronBridge
    {
        object eval_python(string script);

        object call_common_module_classmethod(
            string module_name,
            string class_name,
            string method_name,
            object args
        );

        object call_module_func(
            string module_name,
            string func_name,
            object args
        );

        object call_module_classproperty(
            string module_name,
            string class_name,
            string property_name,
            object args
        );

        object call_module_classmethod(
            string module_name,
            string class_name,
            string method_name,
            object args
        );
    }
}
