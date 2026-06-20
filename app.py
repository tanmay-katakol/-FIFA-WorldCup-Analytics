import streamlit as st
import pickle
import pandas as pd

# Load model and encoder
model = pickle.load(open("model.pkl", "rb"))
result_encoder = pickle.load(open("result_encoder.pkl", "rb"))

st.set_page_config(page_title="FIFA World Cup Predictor")

st.title("⚽ FIFA World Cup Match Predictor")

teams = [
    "Argentina",
    "Brazil",
    "France",
    "Germany",
    "England",
    "Spain",
    "Italy",
    "Portugal",
    "Netherlands",
    "Belgium",
    "Croatia",
    "Morocco"
]

# FIFA rankings from your ranking dataset
rankings = {
    "Brazil": 1,
    "Belgium": 2,
    "Argentina": 3,
    "France": 4,
    "England": 5,
    "Spain": 7,
    "Netherlands": 8,
    "Portugal": 9,
    "Germany": 11,
    "Croatia": 12,
    "Italy": 6,
    "Morocco": 22
}

team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", teams)

if st.button("Predict Match"):

    st.write("Button clicked!")

    home_rank = rankings[team1]
    away_rank = rankings[team2]
    rank_difference = away_rank - home_rank

    input_data = pd.DataFrame({
        "home_rank": [home_rank],
        "away_rank": [away_rank],
        "rank_difference": [rank_difference]
    })

    st.write(f"{team1} Rank: #{home_rank}")
    st.write(f"{team2} Rank: #{away_rank}")

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    st.write("Prediction Confidence:")
    st.write(f"Away Win: {probabilities[0]*100:.1f}%")
    st.write(f"Draw: {probabilities[1]*100:.1f}%")
    st.write(f"Home Win: {probabilities[2]*100:.1f}%")
    result = result_encoder.inverse_transform([prediction])[0]

    if result == "Home Win":
        st.success(f"🏆 Predicted Winner: {team1}")

    elif result == "Away Win":
        st.success(f"🏆 Predicted Winner: {team2}")

    else:
        st.success("🤝 Predicted Result: Draw")