using System;
using System.ComponentModel;
using System.Runtime.InteropServices;
using System.Security.Permissions;

namespace MacronInterop
{
    public interface IWebviewBridge
    {
        object eval_python(string script);

        object call(string className, string methodName, object args);
    }
}
