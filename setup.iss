[Setup]
AppName=HEIC Converter
AppVersion=1.1
DefaultDirName={pf}\HEIC Converter
DefaultGroupName=HEIC Converter
DisableProgramGroupPage=yes
OutputDir=dist_installer
OutputBaseFilename=HEICConverterSetup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
; Update the Source path to point to the 'build_exe' directory
Source: "C:\Users\zimme\OneDrive\Documents\build_exe\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{userdesktop}\HEIC Converter"; Filename: "{app}\HEICConverter.exe"
Name: "{group}\HEIC Converter"; Filename: "{app}\HEICConverter.exe"

[Run]
Filename: "{app}\HEICConverter.exe"; Description: "Launch HEIC Converter"; Flags: nowait postinstall skipifsilent