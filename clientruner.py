import asyncio
import subprocess

# Liste des fichiers à exécuter
files_to_execute = ["python1.py", "python2.py", "python3.py", "python4.py"]

async def execute_file(file):
    try:
        # Exécute le fichier en utilisant subprocess
        await asyncio.create_subprocess_exec("python", file)
        print(f"{file} exécuté avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {file}: {e}")

async def main():
    # Crée des tâches pour chaque fichier à exécuter
    tasks = [execute_file(file) for file in files_to_execute]
    # Lance les tâches en parallèle
    await asyncio.gather(*tasks)

# Lance le programme principal asyncio
asyncio.run(main())
