import json
from typing import List

class Task:
    """
    Luokka, joka edustaa yksittäistä tehtävää.
    """
    def __init__(self, title: str, description: str):
        self.__title = title  # Kapseloitu attribuutti
        self.__description = description
        self.__completed = False

    def mark_completed(self):
        """Merkitsee tehtävän suoritetuksi."""
        self.__completed = True

    def to_dict(self) -> dict:
        """Muuntaa tehtävän sanakirjamuotoon tiedostoon tallennusta varten."""
        return {
            "title": self.__title,
            "description": self.__description,
            "completed": self.__completed
        }

    @staticmethod
    def from_dict(data: dict):
        """Luo Task-olion sanakirjasta."""
        task = Task(data["title"], data["description"])
        if data["completed"]:
            task.mark_completed()
        return task

    def __str__(self):
        """Palauttaa tehtävän tekstimuodossa."""
        status = "[X]" if self.__completed else "[ ]"
        return f"{status} {self.__title}: {self.__description}"

class TaskManager:
    """
    Luokka, joka hallitsee tehtävälistaa ja sen tiedostokäsittelyä.
    """
    def __init__(self, filename: str = "tasks.json"):
        self.__filename = filename
        self.__tasks: List[Task] = self.__load_tasks()

    def add_task(self, title: str, description: str):
        """Lisää uuden tehtävän listaan."""
        task = Task(title, description)
        self.__tasks.append(task)
        self.__save_tasks()

    def complete_task(self, index: int):
        """Merkitsee annetun indeksin mukaisen tehtävän suoritetuksi."""
        if 0 <= index < len(self.__tasks):
            self.__tasks[index].mark_completed()
            self.__save_tasks()

    def list_tasks(self):
        """Listaa kaikki tehtävät."""
        for i, task in enumerate(self.__tasks):
            print(f"{i}: {task}")

    def __save_tasks(self):
        """Tallentaa tehtävät tiedostoon JSON-muodossa."""
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.__tasks], file, indent=4)

    def __load_tasks(self) -> List[Task]:
        """Lataa tehtävät tiedostosta, jos se on olemassa."""
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

# Ohjelman päälogiikka
def main():
    manager = TaskManager()
    while True:
        print("\n1. Lisää tehtävä\n2. Listaa tehtävät\n3. Merkitse tehtävä suoritetuksi\n4. Poistu")
        choice = input("Valitse toiminto: ")

        if choice == "1":
            title = input("Anna tehtävän otsikko: ")
            description = input("Anna tehtävän kuvaus: ")
            manager.add_task(title, description)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            try:
                index = int(input("Anna suoritettavan tehtävän numero: "))
                manager.complete_task(index)
            except ValueError:
                print("Virheellinen syöte.")
        elif choice == "4":
            break
        else:
            print("Virheellinen valinta.")

if __name__ == "__main__":
    main()
