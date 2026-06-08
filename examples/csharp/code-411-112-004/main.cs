// CredentialManager.cs
using System;
using System.Runtime.InteropServices;
using System.Text;

public static class CredentialManager
{
    // Импорт WinAPI — безопаснее, чем сторонние библиотеки
    [DllImport("advapi32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    private static extern bool CredWrite(ref Credential credential, uint flags);

    [DllImport("advapi32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    private static extern bool CredRead(string target, CredentialType type, int reservedFlag, out IntPtr credentialPtr);

    [DllImport("advapi32.dll", SetLastError = true)]
    private static extern bool CredFree(IntPtr cred);

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    private struct Credential
    {
        public uint Flags;
        public CredentialType Type;
        public IntPtr TargetName;
        public IntPtr Comment;
        public System.Runtime.InteropServices.ComTypes.FILETIME LastWritten;
        public uint CredentialBlobSize;
        public IntPtr CredentialBlob;
        public uint Persist;
        public uint AttributeCount;
        public IntPtr Attributes;
        public IntPtr TargetAlias;
        public IntPtr UserName;
    }

    private enum CredentialType : uint
    {
        Generic = 1,
        DomainPassword = 2,
        DomainCertificate = 3,
        DomainVisiblePassword = 4,
        GenericCertificate = 5,
        DomainExtended = 6,
        Maximum = 7,
        MaximumEx = Maximum + 1000
    }

    public static void SaveCredential(string targetName, string userName, string password)
    {
        var cred = new Credential
        {
            Type = CredentialType.Generic,
            TargetName = Marshal.StringToCoTaskMemUni(targetName),
            UserName = Marshal.StringToCoTaskMemUni(userName),
            CredentialBlobSize = (uint)Encoding.Unicode.GetBytes(password).Length,
            CredentialBlob = Marshal.StringToCoTaskMemUni(password),
            Persist = 2 // CRED_PERSIST_LOCAL_MACHINE (сохраняется между перезагрузками)
        };

        try
        {
            if (!CredWrite(ref cred, 0))
                throw new Exception($"Ошибка сохранения учётных данных: {Marshal.GetLastWin32Error()}");
        }
        finally
        {
            Marshal.FreeCoTaskMem(cred.TargetName);
            Marshal.FreeCoTaskMem(cred.UserName);
            Marshal.FreeCoTaskMem(cred.CredentialBlob);
        }
    }

    public static (string? UserName, string? Password) ReadCredential(string targetName)
    {
        if (!CredRead(targetName, CredentialType.Generic, 0, out IntPtr credPtr))
        {
            var error = Marshal.GetLastWin32Error();
            if (error == 1168) // ERROR_NOT_FOUND
                return (null, null);
            throw new Exception($"Ошибка чтения учётных данных: {error}");
        }

        try
        {
            var cred = Marshal.PtrToStructure<Credential>(credPtr);
            var userName = cred.UserName != IntPtr.Zero ? Marshal.PtrToStringUni(cred.UserName) : null;
            var password = cred.CredentialBlob != IntPtr.Zero 
                ? Marshal.PtrToStringUni(cred.CredentialBlob, (int)cred.CredentialBlobSize / 2) 
                : null;
            return (userName, password);
        }
        finally
        {
            CredFree(credPtr);
        }
    }
}

// Пример использования в ViewModel
/*
var (user, pwd) = CredentialManager.ReadCredential("MyApp");
if (user != null)
{
    Username = user;
    // Пароль можно использовать для автоматического входа — но НИКОГДА не сохранять в свойствах ViewModel
}
else
{
    // Требуем ввод логина/пароля
}
*/
