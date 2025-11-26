 $acl = Get-Acl C:\Informes
 $rule = New-Object System.Security.AccessControl.FileSystemAccessRule('2-DAW','FullControl','Allow')
 $acl.SetAccessRule($rule) ; Set-Acl -Path C:\Informes -AclObject $acl
 Get-Acl C:\Informes | Format-List
>>