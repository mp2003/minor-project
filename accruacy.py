from sklearn.model_selection import train_test_split

# Modify the train_model function
def train_model():
    # ... your existing code to get faces and labels

    # Split data into training and testing sets
    faces_train, faces_test, labels_train, labels_test = train_test_split(faces, labels, test_size=0.2, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(faces_train, labels_train)

    # Now, use faces_test and labels_test for evaluation

    # ... your existing code to save the model


    from sklearn.metrics import accuracy_score

def evaluate_model():
    faces_test, labels_test = load_testing_data()  # You need to implement a function to load your testing data

    # Assuming model is already trained and loaded
    model = joblib.load('static/face_recognition_model.pkl')

    # Get predictions for the test set
    predictions = model.predict(faces_test)

    # Calculate accuracy
    accuracy = accuracy_score(labels_test, predictions)
    print(f'Test Accuracy: {accuracy * 100:.2f}%')


    if __name__ == '__main__':
        train_model()
        evaluate_model()
    