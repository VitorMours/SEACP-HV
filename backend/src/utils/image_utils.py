from pathlib import Path
import os
def build_file_structure() -> None:
    path = Path(__file__).resolve().parent.parent / "files" 
    if path.exists():
        print("Diretorio de Files existe")
    else:
        try:
            path.mkdir(parents=True, exist_ok=True)
            print(f"Diretório '{path}' criado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao criar o diretório: {e}")

def build_raw_image_folder() -> None:
    pass

    