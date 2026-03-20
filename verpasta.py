from pathlib import Path
import subprocess

diretorio_atual = Path.cwd()

if (diretorio_atual / '.git').is_dir():
    print("pasta já está no git")
else:
    print("subindo pasta para o git")
    subprocess.run(['git', 'init'], check=True)

resposta = input("Deseja subir os arquivos para o git? (s/n): ")

if resposta.lower() == 's':
    print("Subindo")
    subprocess.run(['git', 'add', '.'])
    commit = input("Deseja escrever seu commit? (Enter = auto commit): ")
    if commit.strip() == "":
        print("Commit automatico")
        subprocess.run(['git', 'commit', '-m', 'auto commit'])
    else:
        print("Sua mensagem de commit:", commit)
        subprocess.run(['git', 'commit', '-m', commit])
    url = input("Cole a URL do repositorio aqui: ")
    subprocess.run(['git', 'remote', 'set-url', 'origin', url])
    branch = input("Deseja subir para outra branch? (Enter = main): ")
    if branch.strip() == "":
        print("Subindo para branch main")
        subprocess.run(['git', 'branch', '-M', 'main'])
        print("dando Push para main")
        subprocess.run(['git', 'push', '-u', 'origin', 'main'])
    else:
        print("subindo para branch ", branch)
        subprocess.run(['git', 'branch', '-M', branch])
        print("dando push para ", branch)
        subprocess.run(['git', 'push', '-u', 'origin', branch])



#isso acima vê qual a pasta atual
