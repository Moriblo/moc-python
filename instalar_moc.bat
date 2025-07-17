@echo off
chcp 65001 >nul
echo.
echo ╭────────────────────────────────────────────────────╮
echo │        🔧 moc-python — Instalação Inicial         │
echo ╰────────────────────────────────────────────────────╯
echo.

:: Verificando Python
echo 🐍 Verificando versão do Python...
python --version
if errorlevel 1 (
    echo ❌ Python não detectado ou fora do PATH.
    goto FIM
)

:: Verificando Poetry
echo 🔍 Verificando presença do Poetry...
where poetry >nul
IF ERRORLEVEL 1 (
    echo ⚠️ Poetry não encontrado no ambiente.
    echo 💡 Instale manualmente com o comando abaixo no PowerShell:
    echo.
    echo (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing^).Content ^| python -
    echo.
    echo Após instalar, reinicie o terminal e tente novamente.
    goto FIM
) ELSE (
    echo ✅ Poetry detectado com sucesso!
)

:: Instalando dependências
echo 📦 Instalando dependências via Poetry...
poetry install
poetry check

:: Validando estrutura mínima
echo 📁 Validando estrutura de diretórios esperada...
if exist moc (
    echo ✅ Pacote moc/ presente.
) else (
    echo ⚠️ Pasta moc/ não encontrada!
)

if exist tests (
    echo ✅ Pasta de testes encontrada.
) else (
    echo ⚠️ Pasta tests/ não encontrada!
)

echo.
echo ✅ Ambiente moc-python pronto para uso!
echo.

:FIM
pause
