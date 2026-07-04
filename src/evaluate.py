from sklearn.metrics import accuracy_score


def evaluate_model(model, x_test, y_test):
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    print("accuracy:", accuracy)
    return accuracy
