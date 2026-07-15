⚽ FIFA World Cup ML Predictor

A machine learning web app that predicts the outcome of football matches (home win / away win / draw) based on historical international match data. Built as a personal project to learn end-to-end ML — from data preprocessing and model training to deploying a live, usable web app.

🔗 Live demo:** [fifa-worldcup-ml-predictor.vercel.app](https://fifa-worldcup-ml-predictor.vercel.app)

---

##📌 What it does
Given two teams, the tournament, and the match location, the model predicts the likely outcome of the match using patterns learned from historical results.

Example flow:
1. Enter home team, away team, tournament, city, country, and whether it's a neutral venue
2. Model encodes the inputs and runs them through a trained classifier
3. Returns a predicted outcome

---

## 🛠️ Tech Stack

**Backend / ML**
- Python
- scikit-learn (model training & evaluation)
- pandas (data preprocessing)
- Flask / API layer (see `api/`)

**Frontend**
- JavaScript, HTML, CSS
- Deployed on Vercel

**Backend hosting**
- Deployed on Render (see `render.yaml`)

---

## 📁 Project Structure

```
fifa-worldcup-ml-predictor/
├── api/              # Backend API routes
├── data/             # Match dataset(s) used for training
├── frontend/          # Frontend UI (Vercel-hosted)
├── models/           # Saved/trained model artifacts
├── src/
│   ├── preprocess.py  # Cleans and encodes raw match data
│   ├── train.py       # Trains the classification model
│   ├── evaluate.py    # Evaluates model accuracy
│   └── predict.py     # Loads model + runs predictions
├── main.py            # Entry point: trains model, then runs a CLI prediction
├── requirements.txt    # Python dependencies
├── package.json        # Frontend dependencies
└── render.yaml         # Render deployment config
```

> Note: the `frontend/` folder is currently named `fronted` in the repo — renaming is on the to-do list.

---

## 🚀 Running it locally

**Backend**
```bash
git clone https://github.com/shivasaireddy09/fifa-worldcup-ml-predictor.git
cd fifa-worldcup-ml-predictor
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
This will preprocess the data, train the model, and prompt you for match details in the terminal.

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

---

## 🧠 How the model works

- Raw historical match data is cleaned and encoded in `preprocess.py` (team names, tournament type, venue, etc. are converted to a format the model can learn from).
- `train.py` trains a classification model on this data to predict match outcome.
- `evaluate.py` reports the model's accuracy on a held-out test set.
- `predict.py` loads the trained model and encoders to make predictions on new, unseen matches.

**Current limitations:**
- The model relies only on historical categorical data (teams, venue, tournament) — it does not currently factor in things like current squad form, injuries, or head-to-head recency, which real-world prediction models typically weigh heavily.
- Accuracy is a work in progress — see [Roadmap](#-roadmap) below.

---

## 🤖 A note on how this was built

This project was built with AI tools (like Claude/ChatGPT/Copilot) as a coding partner — mainly to help scaffold the ML pipeline and speed up the frontend. The backend logic (preprocessing, training, evaluation) was built with AI assistance but reviewed and understood step-by-step; the frontend was built more quickly with AI generating most of the UI code. I'm being upfront about this because I think it's more useful (and honest) than pretending otherwise — and I'm actively working on deepening my own understanding of the ML side in particular.

---

## 🗺️ Roadmap

- [ ] Clean up repo (remove `node_modules` from version control, fix `.gitignore`)
- [ ] Rename `fronted` → `frontend`
- [ ] Add proper train/test split reporting and confusion matrix to README
- [ ] Add unit tests for `preprocess.py` and `predict.py`
- [ ] Handle unseen team names gracefully (currently may error if a team wasn't in training data)
- [ ] Separate `main.py` into a clean training script vs. a CLI prediction script
- [ ] Experiment with additional features (recent form, rankings) to improve accuracy

---

## 📄 License

Not currently licensed — feel free to open an issue if you'd like to use or build on this.
