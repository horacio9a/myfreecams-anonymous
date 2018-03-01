@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
SET OUT_DIR=C:/Videos/MFC/
CLS
ECHO.
SET /P MODE=EX(7) START(6) MFCYTR(5) MFCSLR(4) MFCLSR(3) MFCFFR(2) MFCRTMPR(1) MFC(0)(%MODE%): 
IF "%MODE%"=="" GOTO MFC
IF "%MODE%"=="0" GOTO MFC
IF "%MODE%"=="1" GOTO MFCRTMPR
IF "%MODE%"=="2" GOTO MFCFFR
IF "%MODE%"=="3" GOTO MFCLSR
IF "%MODE%"=="4" GOTO MFCSLR
IF "%MODE%"=="5" GOTO MFCYTR
IF "%MODE%"=="6" GOTO START
IF "%MODE%"=="7" GOTO EXIT
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
:MFCRTMPR
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
:MFCRTMPR_
COLOR 0F
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### MFCRTMPR ## P Y T H O N   R E C #### 24/7 ###
ECHO ### RTMP ###### %_MODEL_%
ECHO #################################################
cd C:/-mfc-py
python mfcrtmpr.py %MODEL%
cd %OUT_DIR%
FOR /R %%F in (*) DO IF %%~ZF LSS 40 DEL "%%F"
TIMEOUT 30
GOTO MFCRTMPR_

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
COLOR 0F
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### MFCFFR #### P Y T H O N   R E C #### 24/7 ###
ECHO ### FFMPEG #### %_MODEL_%
ECHO #################################################
cd C:/-mfc-py
python mfcffr.py %MODEL%
cd %OUT_DIR%
FOR /R %%F in (*) DO IF %%~ZF LSS 40 DEL "%%F"
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
COLOR 0F
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO ################################################
ECHO ### MFCLSR ### P Y T H O N   R E C #### 24/7 ###
ECHO ### LS ####### %_MODEL_%
ECHO ################################################
cd C:/-mfc-py
python mfclsr.py %MODEL%
cd %OUT_DIR%
FOR /R %%F in (*) DO IF %%~ZF LSS 40 DEL "%%F"
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
COLOR 0F
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### MFCSLR #### P Y T H O N   R E C #### 24/7 ###
ECHO ### SL ######## %_MODEL_%
ECHO #################################################
cd C:/-mfc-py
python mfcslr.py %MODEL%
cd %OUT_DIR%
FOR /R %%F in (*) DO IF %%~ZF LSS 40 DEL "%%F"
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
COLOR 0F
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### MFCYTR #### P Y T H O N   R E C #### 24/7 ###
ECHO ### YTDL ###### %_MODEL_%
ECHO #################################################
cd C:/-mfc-py
python mfcytr.py %MODEL%
cd %OUT_DIR%
FOR /R %%F in (*) DO IF %%~ZF LSS 40 DEL "%%F"
TIMEOUT 30
GOTO MFCYTR_
:EXIT
GOTO :EOF
ENDLOCAL
