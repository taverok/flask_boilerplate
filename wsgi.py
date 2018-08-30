# Set the path
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sample_app.src import create_app
app = create_app()

if __name__ == "__main__":
    app.run()
