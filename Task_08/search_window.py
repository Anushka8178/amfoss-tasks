import requests
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QListWidget, QListWidgetItem
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.w = None

    def initUI(self):
        self.setWindowTitle("Pokedex")
        self.setFixedSize(850, 500)

   

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setFixedSize(850, 500)

        # Create a layout
        layout = QVBoxLayout()

        # Load and set the background image
        background_path = "/home/anushka/Poke-Search/assets/landing.jpg"
        background = QPixmap(background_path)
        background_label = QLabel(self)
        background_label.setPixmap(background)
        background_label.setGeometry(0, 0, 850, 500)
        layout.addWidget(background_label)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)
        layout.addWidget(self.textbox)

        label1 = QLabel("Enter the name", self)
        layout.addWidget(label1)

        self.enter_button = QPushButton("Search", self)
        self.enter_button.clicked.connect(self.fetch_pokemon_data)
        layout.addWidget(self.enter_button)

        self.capture_button = QPushButton("Capture", self)
        self.capture_button.clicked.connect(self.capture_pokemon)
        layout.addWidget(self.capture_button)

        self.display_button = QPushButton("Display", self)
        self.display_button.clicked.connect(self.display_captured_pokemon)
        layout.addWidget(self.display_button)

        self.setLayout(layout)

        #Displaying Pokemon data
        self.name_label = QLabel(self)
        layout.addWidget(self.name_label)

        self.abilities_label = QLabel(self)
        layout.addWidget(self.abilities_label)

        self.types_label = QLabel(self)
        layout.addWidget(self.types_label)

        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)
        self.captured_pokemon_data = []

    def fetch_pokemon_data(self):
        # Get the user input,Pokemon name
        pokemon_name = self.textbox.text()

        #Request for Pokemon API
        api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
        response = requests.get(api_url)

        if response.status_code == 200:
            pokemon_data = response.json()
            name = pokemon_data['name']
            abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
            types = [type_data['type']['name'] for type_data in pokemon_data['types']]
            stats = [(stat['stat']['name'], stat['base_stat']) for stat in pokemon_data['stats']]

            # Display the information
            self.name_label.setText(f"Name: {name}")
            self.abilities_label.setText(f"Abilities: {', '.join(abilities)}")
            self.types_label.setText(f"Types: {', '.join(types)}")

            # Load and display the official artwork image
            image_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(image_url).content)
            self.image_label.setPixmap(pixmap)

        else:
            error_message = "Pokemon not found. Please enter a valid Pokemon name."
            QMessageBox.warning(self, "Error", error_message)

    def capture_pokemon(self):
        # Get the user input (Pokemon name)
        pokemon_name = self.textbox.text()
        api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
        response = requests.get(api_url)

        if response.status_code == 200:
            pokemon_data = response.json()
            image_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
            capture_dir = 'captured_pokemon_images'
            os.makedirs(capture_dir, exist_ok=True)

            # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                image_filename = f"{pokemon_name.lower()}.png"
                image_path = os.path.join(capture_dir, image_filename)

                with open(image_path, 'wb') as image_file:
                    image_file.write(response.content)

                # Display a message to indicate successful capture
                QMessageBox.information(self, "Capture Success", f"You captured {pokemon_name}!")

                # Add the captured Pokemon data to the list
                self.captured_pokemon_data.append((pokemon_name, image_path))

            else:
                error_message = "Failed to download Pokemon image."
                QMessageBox.warning(self, "Error", error_message)

        else:
            # Error
            error_message = "Pokemon not found. Please enter a valid Pokemon name."
            QMessageBox.warning(self, "Error", error_message)

    def display_captured_pokemon(self):
        # Display captured Pokemon
        captured_pokemon_window = CapturedPokemonWindow(self.captured_pokemon_data)
        captured_pokemon_window.exec()

class CapturedPokemonWindow(QDialog):
    def __init__(self, captured_pokemon_data):
        super().__init__()

        self.setWindowTitle("Captured Pokemon")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout()

        # Create a list to display captured Pokemon names and images
        self.pokemon_list_widget = QListWidget(self)
        layout.addWidget(self.pokemon_list_widget)

        # Set up the list of captured Pokemon names and images
        self.captured_pokemon_data = captured_pokemon_data
        for pokemon_name, image_path in self.captured_pokemon_data:
            item = QListWidgetItem(pokemon_name, self.pokemon_list_widget)
            pixmap = QPixmap(image_path)
            item.setIcon(QIcon(pixmap))

        # Connect the item selection display the image
        self.pokemon_list_widget.itemSelectionChanged.connect(self.display_selected_pokemon)

        self.setLayout(layout)

    def display_selected_pokemon(self):
        # Get the selected item from the list
        selected_item = self.pokemon_list_widget.currentItem()

        if selected_item:
            selected_pokemon_name = selected_item.text()
            # Find the image path for the Pokemon
            selected_pokemon_image_path = None
            for pokemon_name, image_path in self.captured_pokemon_data:
                if pokemon_name == selected_pokemon_name:
                    selected_pokemon_image_path = image_path
                    break

            # Display the Pokemon's image
            if selected_pokemon_image_path:
                pixmap = QPixmap(selected_pokemon_image_path)
                self.image_label.setPixmap(pixmap)
            else:
                self.image_label.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = SearchWindow()
    window.show()
    app.exec()

