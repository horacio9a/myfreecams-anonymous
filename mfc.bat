@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
SET /P MODE=EXIT(6)  START(5)  MFCYTR(4)  MFCSLR(3)  MFCLSR(2)  MFCFFR(1)  MFC(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO MFC
IF "%MODE%"=="0" GOTO MFC
IF "%MODE%"=="1" GOTO MFCFFR
IF "%MODE%"=="2" GOTO MFCLSR
IF "%MODE%"=="3" GOTO MFCSLR
IF "%MODE%"=="4" GOTO MFCYTR
IF "%MODE%"=="5" GOTO START
IF "%MODE%"=="6" GOTO EXIT
:MFC
ECHO.
CLS && ECHO #################################################
ECHO ### MFC ####  P Y T H O N   R E C / P L A Y  ####
ECHO #################################################
cd C:/
COLOR 0F
cd -mfc-py
start python mfc.py
ECHO.
PAUSE
GOTO START
:MFCFFR
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/MFC_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose MFC Model Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/MFC_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:MFCFFR_
ECHO.
SET MODELNAME=%MODEL% ############## %M% ##########################
SET _MODEL_=%MODELNAME:~0,37%
ECHO.
CLS && ECHO #####################################################
ECHO ### MFCFFR ####  P Y T H O N   R E C  ###### 24/7 ###
ECHO ### FFMPEG #### %_MODEL_%
ECHO #####################################################
cd C:/
COLOR 0F
cd -mfc-py
python mfcffr.py %MODEL%
TIMEOUT 30
GOTO MFCFFR_
:MFCLSR
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/MFC_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose MFC Model Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/MFC_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:MFCLSR_
ECHO.
SET MODELNAME=%MODEL% ############## %M% ##########################
SET _MODEL_=%MODELNAME:~0,34%
ECHO.
CLS && ECHO #################################################
ECHO ### MFCLSR ### P Y T H O N   R E C ##### 24/7 ###
ECHO ### LS ####### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -mfc-py
python mfclsr.py %MODEL%
TIMEOUT 30
GOTO MFCLSR_
:MFCSLR
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/MFC_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose MFC Model Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/MFC_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:MFCSLR_
ECHO.
SET MODELNAME=%MODEL% ############## %M% ##########################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### MFCSLR #### P Y T H O N   R E C #### 24/7 ###
ECHO ### SL ######## %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -mfc-py
python mfcslr.py %MODEL%
TIMEOUT 30
GOTO MFCSLR_
:MFCYTR
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/MFC_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose MFC Model Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/MFC_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:MFCYTR_
ECHO.
SET MODELNAME=%MODEL% ############## %M% ##########################
SET _MODEL_=%MODELNAME:~0,37%
ECHO.
CLS && ECHO #####################################################
ECHO ### MFCYTR ####  P Y T H O N   R E C  ###### 24/7 ###
ECHO ### YTDL ###### %_MODEL_%
ECHO #####################################################
cd C:/
COLOR 0F
cd -mfc-py
python mfcytr.py %MODEL%
TIMEOUT 30
GOTO MFCYTR_
:EXIT
GOTO :EOF
ENDLOCAL
