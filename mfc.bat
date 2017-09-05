@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
SET /P MODE=EXIT(4) MFCRTS(3) MFCR(2) MFCTS(1) MFC(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO MFC
IF "%MODE%"=="0" GOTO MFC
IF "%MODE%"=="1" GOTO MFCTS
IF "%MODE%"=="2" GOTO MFCR
IF "%MODE%"=="3" GOTO MFCRTS
IF "%MODE%"=="4" GOTO EXIT
:MFC
ECHO.
CLS && ECHO #################################################
ECHO ### MFC ######## R E C O R D I N G ##############
ECHO #################################################
cd C:/
COLOR 0F
cd -mfc-py
python mfc.py
ECHO.
PAUSE
GOTO START
:MFCTS
ECHO.
CLS && ECHO #################################################
ECHO ### MFCTS ###### R E C O R D I N G ##############
ECHO #################################################
cd C:/
COLOR 0F
cd -mfc-py
python mfcts.py
ECHO.
PAUSE
GOTO START
:MFCR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-mfc-py/MFC_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose MFC MODEL Name (%M%:%MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-mfc-py/MFC_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:MFCR_
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### MFCR ###### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -mfc-py
python mfcr.py %MODEL%
TIMEOUT 30
GOTO MFCR_
:MFCRTS
SET n=0
FOR /F "tokens=*" %%A IN (C:/-mfc-py/MFC_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose MFC MODEL Name (%M%:%MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-mfc-py/MFC_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
:MFCRTS_
ECHO.
CLS && ECHO #################################################
ECHO ### MFCRTS #### R E C O R D I N G ###############
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -mfc-py
python mfcrts.py %MODEL%
TIMEOUT 30
GOTO MFCRTS_
:EXIT
GOTO :EOF
ENDLOCAL
