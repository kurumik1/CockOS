Set objFSO=CreateObject("Scripting.FileSystemObject")

outFile = "SYSSTATS.cfg"
Set objFile = objFSO.CreateTextFile(outFile,True)
objFile.Write "PC-01" & vbCrLf
objFile.Write "1.3" & vbCrLf
objFile.Write "0"
objFile.Close

x=msgbox("SystemStats File is now fixed" ,0, "SystemStats File is now fixed")