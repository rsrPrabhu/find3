from flask import Flask, request, jsonify
import pandas as pd

# Load the dataset
df = pd.read_csv('../../datasets/countries.csv')

# Initialize Flask app
app = Flask(__name__)


# Define the function to process the query
def process_query(query):
    print(f"Received query: {query}")  # Debugging: Show the received query

    query = query.lower()

    # Check if the question is asking about the capital
    if "capital" in query:
        print("Identified question about capital")  # Debugging: Confirming question type
        country = extract_country(query)
        print(f"Extracted country: {country}")  # Debugging: Show extracted country
        if country:
            capital = df[df['Country'].str.lower() == country]['Capital'].values
            print(f"Capital found: {capital}")  # Debugging: Show found capital
            if capital:
                return capital[0]
            else:
                return "Country not found."
        return "Please specify a valid country."

    # Check if the question is asking about the population
    elif "population" in query:
        print("Identified question about population")  # Debugging: Confirming question type
        country = extract_country(query)
        print(f"Extracted country: {country}")  # Debugging: Show extracted country
        if country:
            population = df[df['Country'].str.lower() == country]['Population'].values
            print(f"Population found: {population}")  # Debugging: Show found population
            if population:
                return int(population[0])
            else:
                return "Country not found."
        return "Please specify a valid country."

    # Default response if no matching question pattern
    return "Sorry, I didn't understand the question."


# Helper function to extract country name from the query
def extract_country(query):
    # Extract country by checking if it's in the dataset (naive approach)
    countries = df['Country'].str.lower()
    for country in countries:
        if country in query:
            return country
    return None


# Define the route for handling questions
@app.route('/query', methods=['GET'])
def query():
    # Get the user query
    user_query = request.args.get('question')

    if not user_query:
        return jsonify({"error": "No question provided!"}), 400

    # Process the question
    result = process_query(user_query)

    return jsonify({"answer": result})


# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
