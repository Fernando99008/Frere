import sys
from PySide6.QtWidgets import QApplication
from database.connection import engine
from database.schema import Base
from models import Rol, Usuario
from database.seed import seed_database
from views.login_view import LoginView 

def main():
    Base.metadata.create_all(engine)
    seed_database()
    app = QApplication(sys.argv)
    ventana=LoginView()
    ventana.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()