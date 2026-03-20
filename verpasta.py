from pathlib import Path
import subprocess

diretorio_atual = Path.cwd()

if (diretorio_atual / '.git').is_dir():
    print("pasta já está no git")
else:
    print("subindo pasta para o git")
    subprocess.run(['git', 'init'], check=True)

resposta = input("Deseja subir os arquivos para o git? (s/n)")

if resposta.lower() == 's':
    print("Subindo")
    subprocess.run(['git', 'add', '.'])
    commit = input("Deseja escrever seu commit? (Enter = auto commit)")
    if commit.strip() == "":
        print("Commit automatico")
        subprocess.run(['git', 'commit', '-m', 'auto commit'])
    else:
        print("Sua mensagem de commit:", commit)
        subprocess.run(['git', 'commit', '-m', commit])




#isso acima vê qual a pasta atual
