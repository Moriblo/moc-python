# ╭────────────────────────────────────────────────────────────╮
# │                                                            │
# │       moc-python — Script de Instalação Inicial            │
# │                                                            │
# │ Valida pré-requisitos (Python, Poetry), instala o ambiente │
# │ virtual via Poetry e verifica estrutura técnica mínima     │
# │                                                            │
# │ Autor: MOACYR & Copilot • Versão: 0.1.0 • Data: 2025-07-17 │
# ╰────────────────────────────────────────────────────────────╯

import subprocess
import sys
import os
import shutil

def verificar_python():
    print("🐍 Verificando versão do Python...")
    versao = sys.version_info
    print(f"📍 Versão atual detectada: {versao.major}.{versao.minor}.{versao.micro}")
    if versao.major == 3 and versao.minor >= 9:
        print(f"✅ Python {versao.major}.{versao.minor}+ OK")
    else:
        print(f"❌ Python {versao.major}.{versao.minor} não compatível (requer >= 3.9)")
        sys.exit(1)

def verificar_poetry():
    print("\n🔍 Verificando presença do Poetry...")
    caminho = shutil.which("poetry")
    if caminho:
        print(f"✅ Poetry localizado em: {caminho}")
        return True
    else:
        print("⚠️ Poetry não encontrado no PATH.")
        return False

def instrucoes_instalacao_poetry():
    print("\n📦 Para instalar o Poetry manualmente, execute no PowerShell:")
    print("(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -")
    print("\n💡 Após instalar, reinicie o terminal para que o PATH seja reconhecido.")
    print("❌ Instalação abortada até que o Poetry esteja disponível.")
    sys.exit(1)

def instalar_dependencias():
    print("\n📦 Instalando dependências via Poetry...")
    try:
        subprocess.run(["poetry", "install"], check=True)
        subprocess.run(["poetry", "check"], check=True)
        print("✅ Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError:
        print("❌ Erro ao executar 'poetry install' ou 'poetry check'")
        sys.exit(1)

def validar_estrutura():
    print("\n📁 Verificando estrutura de diretórios essenciais...")
    pastas = ["moc", "tests", "docs"]
    faltando = [p for p in pastas if not os.path.exists(p)]
    if faltando:
        print(f"⚠️ Pastas ausentes: {', '.join(faltando)}")
    else:
        print("✅ Estrutura técnica básica encontrada.")

def instrucoes_uso():
    print("\n🧠 Dica: para rodar auditoria técnica, use o comando:")
    print("poetry run python moc/verificar_certidao.py")

def main():
    print("\n🚀 Iniciando instalação do moc-python...\n")
    verificar_python()
    if not verificar_poetry():
        instrucoes_instalacao_poetry()
    instalar_dependencias()
    validar_estrutura()
    instrucoes_uso()
    print("\n✅ Ambiente moc-python pronto para uso.\n")

if __name__ == "__main__":
    main()

