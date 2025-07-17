# ╭────────────────────────────────────────────────────────────╮
# │                                                            │
# │     moc-python — Instalação Automatizada via PowerShell   │
# │                                                            │
# ╰────────────────────────────────────────────────────────────╯

Write-Host "`n🚀 Iniciando instalação do moc-python...`n"

# 🐍 Verifica versão do Python
$pythonVersion = python --version
Write-Host "📦 Python detectado: $pythonVersion"

# 🔍 Verifica presença do Poetry
$poetryPath = Get-Command poetry -ErrorAction SilentlyContinue

if (-not $poetryPath) {
    Write-Host "`n⚠️ Poetry não encontrado. Instalando automaticamente..."
    Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing | python
    Write-Host "`n✅ Poetry instalado. Reinicie o terminal se necessário."
} else {
    Write-Host "`n✅ Poetry já está disponível em: $($poetryPath.Source)"
}

# 🔁 Executa instalador principal em Python
Write-Host "`n🛠️ Executando instalar_moc.py..."
python instalar_moc.py
