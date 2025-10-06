import subprocess
import sys
import os

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def setup_database():
    os.chdir("api")
    subprocess.check_call([sys.executable, "init_db.py"])
    os.chdir("..")

if __name__ == "__main__":
    print("Instalando dependências...")
    install_requirements()
    
    print("Configurando banco de dados...")
    setup_database()
    
    print("Setup concluído! Execute: cd api && python main.py")