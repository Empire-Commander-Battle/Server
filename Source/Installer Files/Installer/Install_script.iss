; -- Installer.iss --

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

; Some GUIDS for you to choose from:
; {6115732F-390B-44EE-AEA7-E680D053B25F}
; {BD715ED1-26B8-406B-94AE-A48441B4BD2A}
; {7F2BBB4A-5A48-423E-9176-0A4942DF4E4F}
; {1868D835-C2C6-447D-8688-B8085F3BAF81}
; {B0E91C6A-CF5B-4DD6-BF98-7BE75AABAC66}
; {A239A004-0766-4C67-953D-D529E736DF2F}
; {9E380CBE-6096-4BDD-8F7D-C0F40224A22D}
; {30157F0E-B3F2-42FA-8000-06F833A4141A}
; {F9773B1C-B0AC-49E1-A10B-035339FFF664}
; {D1CBB861-423A-4F1A-9345-1142AC0E0E0B}
; {35A5F6A5-4CE0-46DE-9D9C-D0A15770E1AD}
; {F9EA4F2E-641A-4533-819B-F6100923D0C2}
; {DB5FB36A-B602-443E-A441-8A337EFC0508}
; {3C262E00-3C8B-4774-83DB-6412EDFE9FB4}
; {B749FA52-E65E-41F8-9ECA-832EDB9359F2}
; {9EDC3A3F-0804-4F9E-93E3-AAB5A29D0648}
; {E16DAA32-2C42-461A-B752-6F3460288359}

[Setup]
AppId={{77CBC355-CF43-4253-AF9B-4D33BA859FD6}
AppName={cm:ModName}
AppVerName={cm:ModName}
AppVersion={cm:ModVersion}
AppPublisher={cm:ModAuthor}
AppPublisherURL={cm:ModSite}
AppSupportURL={cm:ModSite}
AppUpdatesURL={cm:ModSite}
AppCopyright=Copyright © 2012 {cm:ModAuthor}
DefaultDirName={reg:HKLM\SOFTWARE\Mount&Blade Warband\,Install_Path|{pf}\Mount&Blade Warband}\Modules\{cm:ModFolder}
DefaultGroupName={cm:ModName}
AllowNoIcons=yes
UninstallDisplayIcon=Images\iconwb.ico
UninstallDisplayName={cm:ModName}
VersionInfoVersion=1.0.0.0
VersionInfoProductName=My Mod
VersionInfoDescription=My Mod Setup
VersionInfoProductVersion=1.0.0
OutputDir=..\Setup\
OutputBaseFilename=My_Mod_V1.0
Compression=lzma/ultra64
InternalCompressLevel=ultra64
SetupIconFile=Images\iconwb.ico
LicenseFile=Info\License.txt
WizardSmallImageFile=Images\mb_inst_top.bmp
WizardImageFile=Images\mb_inst_left.bmp

[Languages]
Name: en; MessagesFile: "compiler:Default.isl"
Name: nl; MessagesFile: "compiler:Languages\Dutch.isl"
Name: de; MessagesFile: "compiler:Languages\German.isl"
Name: fr; MessagesFile: "compiler:Languages\French.isl"

[Messages]
en.BeveledLabel=English
nl.BeveledLabel=Nederlands
de.BeveledLabel=Deutsch
fr.BeveledLabel=Français

[CustomMessages]
ModName=My Mod
ModFolder=mymod
ModAuthor=Author
ModSite=http://www.website.com/
ModVersion=1.0.0

en.AllUsers=For all users
en.CurrentUser=For the current user only
nl.AllUsers=Voor alle gebruikers
nl.CurrentUser=Alleen voor de huidige gebruiker
de.AllUsers=Für alle verbraucher
de.CurrentUser=Nur für den aktuellen benutzer
fr.AllUsers=Pour tous les utilisateurs
fr.CurrentUser=Pour l'utilisateur courant seulement

[Tasks]
;Name: desktopicon; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}";
;Name: desktopicon\common; Description: "{cm:AllUsers}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: exclusive
;Name: desktopicon\user; Description: "{cm:CurrentUser}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: exclusive unchecked

[Files]
Source: "..\mymod\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs
;Source: "Info\License.txt"; DestDir: "{app}\Documentation\";
;Source: "Readme-Dutch.txt"; DestName: "Leesmij.txt"; DestDir: "{app}"; Languages: nl; Flags: isreadme
;Source: "Readme-German.txt"; DestName: "Liesmich.txt"; DestDir: "{app}"; Languages: de; Flags: isreadme

[Registry]
Root: HKCU; Subkey: "Software\MountAndBladeWarbandKeys"; ValueType: string; ValueName: "last_module_warband"; ValueData: "{cm:ModFolder}"

[Icons]
Name: "{group}\{cm:ProgramOnTheWeb,{cm:ModName}}"; Filename: "{cm:ModSite}"
Name: "{group}\{cm:UninstallProgram,{cm:ModName}}"; Filename: "{uninstallexe}";

[Run]
Filename: "{app}\..\..\mb_warband.exe"; WorkingDir: "{app}\..\..\"; Parameters: ""; Description: "{cm:LaunchProgram,Warband}"; Flags: nowait postinstall skipifsilent unchecked


[Code]
function CheckStringIfValidKey(cdkey : string) : boolean;
var
  success : boolean;
begin
    cdkey := Trim(cdkey);
	
    success := (Length(cdkey) = 19);

    if success then begin
      success := ((cdkey[5] = '-') and (cdkey[10] = '-') and (cdkey[15] = '-')); 
    end;

    result := success;
end;


function IsValidKeyDetected : boolean;
var
    key, cdkey: string;
    success: boolean;
	Names: TArrayOfString;
    I: Integer;
begin
    key := '\Software\MountAndBladeWarbandKeys\';
    cdkey := '';
    success := false;
	
    if RegGetSubkeyNames(HKEY_USERS, '', Names) then
    begin
      for I := 0 to GetArrayLength(Names)-1 do
	  begin
	    if success = false then 
		begin
	      success := RegQueryStringValue(HKEY_USERS, Names[I] + key, 'serial_key_nw', cdkey);
		
	  	  if success then begin
	  	    success := CheckStringIfValidKey(cdkey);
	  	  end;
	    end;
  	  end
    end else
    begin
      success := false;
    end;

    result := success;
end;


function InitializeSetup(): boolean;
begin
    if not IsValidKeyDetected then begin
        MsgBox('This mod requires the Napoleonic Wars expansion for Warband.'#13#13
            'Please get it on www.taleworlds.com or other places like steam,'#13
            'and then re-run the setup program.', mbInformation, MB_OK);
        result := false;
    end else
        result := true;
end;