How to use the Napoleonic Wars Mod Installer Package:

To quickly test the compiler you can run "Compile Installer.bat" and it should create an installer for an empty mod.

To configure it for your own mod, simply follow the step-by-step instructions below:
1. Place your module files in the "mymod" folder and rename this folder to the name of your module (Important: module names must not contain special characters!)
2. Go into the "Installer" folder and open "Install_script.iss" in a text editor.
3. Replace the GUID numbers after the AppId= variable with another GUID, each installer must have a unique GUID. There are a couple at the top - just pick a random one.
4. Change any "My Mod"  to the name of your mod (in full writing). Scroll down, don't miss the name under "[CustomMessages]".
5. Change the variable for ModFolder under "[CustomMessages]" from "mymod" to the name you gave the folder earlier.
6. Scroll a bit down and also change the reference to "mymod" under the "[Files]" section to the name of your modfolder.
7. Save the file, you should be done!
8. (OPTIONAL) If need, edit License.txt inside the Info folder.
9. Run "Compile Installer.bat" in the main folder.
10. You should now have an installer for your module in the "Setup" directory.

If you run into any problems, you can ask for support at http://forums.taleworlds.com/index.php/board,64.0.html

Good luck with your mod!