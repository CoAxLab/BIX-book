# For local debuggging purposes
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Install files from Google Drive
!pip install --upgrade /content/drive/My\ Drive/Code/explorationlib
