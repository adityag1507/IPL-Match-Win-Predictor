from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

pipe = pickle.load(open("pipe.pkl", "rb"))

team_logos = {
    "Chennai Super Kings": "logos/csk.png",
    "Delhi Capitals": "logos/dc.png",
    "Gujarat Titans": "logos/gt.png",
    "Kolkata Knight Riders": "logos/kkr.png",
    "Lucknow Super Giants": "logos/lsg.png",
    "Mumbai Indians": "logos/mi.png",
    "Punjab Kings": "logos/pbks.png",
    "Rajasthan Royals": "logos/rr.png",
    "Royal Challengers Bengaluru": "logos/rcb.png",
    "Sunrisers Hyderabad": "logos/srh.png"
}

teams = [
    'Chennai Super Kings',
    'Delhi Capitals',
    'Gujarat Titans',
    'Kolkata Knight Riders',
    'Lucknow Super Giants',
    'Mumbai Indians',
    'Punjab Kings',
    'Rajasthan Royals',
    'Royal Challengers Bengaluru',
    'Sunrisers Hyderabad'
]

cities = sorted([
    'Ahmedabad',
    'Bengaluru',
    'Chandigarh',
    'Chennai',
    'Delhi',
    'Dharamshala',
    'Hyderabad',
    'Jaipur',
    'Kolkata',
    'Lucknow',
    'Mohali',
    'Mumbai',
    'Pune',
    'Sharjah',
    'Visakhapatnam'
])


@app.route("/")
def home():
    return render_template(
        "index.html",
        teams=teams,
        cities=cities,
        team_logos=team_logos
    )

@app.route('/predict', methods=['POST'])
def predict():

    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    city = request.form['city']

    target = int(request.form['target'])
    score = int(request.form['score'])
    overs = float(request.form['overs'])
    wickets = int(request.form['wickets'])


    if overs <= 0 or overs > 20:
        return render_template(
            "index.html",
            teams=teams,
            cities=cities,
            team_logos=team_logos,
            error="Overs must be between 0.1 and 20."
        )

    if wickets < 0 or wickets > 10:
        return render_template(
            "index.html",
            teams=teams,
            cities=cities,
            team_logos=team_logos,
            error="Wickets must be between 0 and 10."
        )

    if score < 0:
        return render_template(
            "index.html",
            teams=teams,
            cities=cities,
            team_logos=team_logos,
            error="Score cannot be negative."
        )

    if target <= 0:
        return render_template(
            "index.html",
            teams=teams,
            cities=cities,
            team_logos=team_logos,
            error="Target must be greater than 0."
        )

    if batting_team == bowling_team:
        return render_template(
            "index.html",
            teams=teams,
            cities=cities,
            team_logos=team_logos,
            error="Batting Team and Bowling Team cannot be the same."
        )

    if score > target:
        return render_template(
            "index.html",
            teams=teams,
            cities=cities,
            team_logos=team_logos,
            error="Current score cannot be greater than the target."
        )

    over_part = int(overs)
    ball_part = round((overs - over_part) * 10)

    if ball_part > 5:
        return render_template(
            "index.html",
            teams=teams,
            cities=cities,
            team_logos=team_logos,
            error="Invalid over entered. Balls can only be between 0 and 5."
        )

    runs_left = target - score
    balls_left = 120 - int(overs * 6)
    wickets_left = 10 - wickets

    if overs == 0:
        crr = 0
    else:
        crr = score / overs

    if balls_left == 0:
        rrr = 0
    else:
        rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[city],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets':[wickets_left],
        'total_runs_x':[target],
        'crr':[crr],
        'rrr':[rrr]
    })

    result = pipe.predict_proba(input_df)

    loss = round(result[0][0] * 100, 2)
    win = round(result[0][1] * 100, 2)

    runs_left = target - score
    balls_left = 120 - int(overs * 6)
    wickets_left = 10 - wickets

    crr = round(score / overs, 2)

    if balls_left > 0:
        rrr = round((runs_left * 6) / balls_left, 2)
    else:
        rrr = 0

    return render_template(
        "index.html",
        teams=teams,
        cities=cities,
        batting_team=batting_team,
        bowling_team=bowling_team,
        city_selected=city,
        target=target,
        score=score,
        overs=overs,
        wickets=wickets,
        win=win,
        loss=loss,
        runs_left=runs_left,
        balls_left=balls_left,
        wickets_left=wickets_left,
        crr=crr,
        rrr=rrr,
        team_logos=team_logos
    )

if __name__ == "__main__":
    app.run(debug=True)