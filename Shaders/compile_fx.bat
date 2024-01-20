@echo off
start /B fxc.exe /D PS_2_X=ps_2_a /Gpp /O3 /T fx_2_0 /Fo mb_2a.fxo mb.fx
start /B fxc.exe /D PS_2_X=ps_2_b /Gpp /O3 /T fx_2_0 /Fo mb_2b.fxo mb.fx

pause