using System;
using System.ComponentModel;
using System.Runtime.InteropServices;
using System.Security.Permissions;

namespace MacronWebviewInterop
{
    public interface IMacronBridge
    {
        object eval_python(string script);

        object call(string className, string methodName, object args);
    }
}
