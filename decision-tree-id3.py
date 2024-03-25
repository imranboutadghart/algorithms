
import six
import sys
sys.modules['sklearn.externals.six'] = six
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import id3

#using pandas to load data of playing tennis
data = pd.read_csv("PlayTennis.csv")

encoder = LabelEncoder()
# Separate features (X) and target class (y)
features = ["Outlook", "Temperature", "Humidity", "Wind"]  # List of feature names
X = data[features]  # Select features by column names
y = data["Play Tennis"]

# Create an ID3 Estimator object
estimator = id3.Id3Estimator()

# Train the ID3 model
estimator.fit(X, y)

# Make predictions on new data (optional)

#note	[sunny, hot, high, Weak] = 0
#		[overcast, Mild, Normal, Weak] = 1
#		[Rain, Cool] = 2
new_data = pd.DataFrame({'Outlook': ['1'], 'Temperature': ['0'], 'Humidity': ['1'], 'Wind': ['0']})
prediction = estimator.predict(new_data)
print("Predicted class for new data:", prediction[0])