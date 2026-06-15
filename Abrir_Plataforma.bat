@echo off
title Plataforma Regulatorio - Raiz Educacao
cd /d "%~dp0"
echo.
echo  =====================================================
echo   Plataforma de Gestao Regulatoria - Raiz Educacao
echo  =====================================================
echo.
echo  Abrindo no navegador em: http://localhost:8502
echo  Para encerrar: pressione Ctrl+C nesta janela
echo.
streamlit run app.py --server.port 8502 --server.headless false
pause
