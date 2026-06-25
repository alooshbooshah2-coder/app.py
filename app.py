from flask import Flask, request

import json
import os

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)

    return {
        "player1":"",
        "player2":"",
        "ali_score": 0,
        "mahdi_score": 0, 
        "ali_kills":0,
        "mahdi_kills":0
    }
    



def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    data = load_data()

    if data["player1"] != "":
       names = f"""
    <h3>{data["player1"]} VS {data["player2"]}</h3>
    """
    else:
       names = """
    <label>player 1:</label><br>
    <input type="text" name="player1" required><br><br>

    <label>player 2:</label><br>
    <input type="text" name="player2" required><br><br>
    """

    return f"""" 
       <h2>point calculat</h2>

       <form action="/result" method="POST">

       {names}

        <label>player 1 score:</label><br>
        <input type="number" name="score1" required><br><br>

        <label>player 2 score:</label><br>
        <input type="number" name="score2" required><br><br>

        <label style = color:blue>player 1 help:</label><br>
        <input type="number" name="help1" required><br><br>

        <label style = color:blue>how many player 2 have no kill:</label><br>
        <input type="number" name="no_kill" required><br><br>

        <label style = color:red>how many player 2 assist:</label><br>
        <input type="number" name="assist" required><br><br>

        <label style = color:red>how many player 1 die:</label><br>
        <input type="number" name="p1_d" required><br><br>

        <button type="submit">ok</button>

    </form>
    """

@app.route("/result", methods=["POST"])
def result():
    player1 = request.form["player1"]
    player2 = request.form["player2"]

    data = load_data()
    if data["player1"] == "":
       data["player1"] = player1 

    if data["player2"] == "":
       data["player2"] = player2
   
    save_data(data)

    alis = int(request.form["score1"])
    mahdis = int(request.form["score2"])

    player1_kills = int(request.form["score1"])
    player2_kills = int(request.form["score2"])
    
    help1 = int(request.form["help1"])
    
    no_kill = int(request.form["no_kill"])

    assist = int(request.form["assist"])

    p1_d = int(request.form["p1_d"])
   
    scoreali = 0
    scorema = 0

    if alis == mahdis:
         scorema,scoreali = scorema,scoreali

    if alis > mahdis:
         scoreali += 1

    elif mahdis > alis:
         scorema += 1

    #player1_kills += alis
    #player2_kills += mahdis    

    if player1_kills >= 50:
       player1_kills = 0

    if player2_kills >= 50:
        player2_kills = 0

    if player1_kills == 0:
          player2_kills = 0

    if player2_kills == 0 :
         player1_kills = 0

    if alis >= mahdis + 4:
       scoreali += 1

    elif mahdis >= alis + 4:
         scorema += 1

    if alis >= mahdis + 8:
       scoreali += 1

    elif mahdis >= alis + 8:
         scorema += 1

    if alis >= mahdis + 12:
       scoreali += 1

    elif mahdis >= alis + 12:
         scorema += 1

   #  #rule ali
   #  #rule 1
    if no_kill == 0:
        scorema = scorema

    elif no_kill != 0 :
          scorema -= no_kill

   #  #rule 2
    if alis == 2:
       scoreali += 1

    if alis == 4:
       scoreali += 1

    if alis == 5:
       scoreali += 2

    if alis == 6:
       scoreali += 2

    if alis == 7:
       scoreali += 3

    if alis == 8:
       scoreali += 3              

    if alis == 9:
       scoreali += 4   

    if alis == 10:
       scoreali += 4

    if alis == 11:
       scoreali += 5

    if alis == 12:
       scoreali += 5

    if alis == 13:
       scoreali += 6

    if alis == 14:
       scoreali += 6       

    if alis == 15:
       scoreali += 7      

    if alis == 16:
       scoreali += 7    

    if alis == 17:
       scoreali += 8    

   #  #rule 3
    if help1 == 0:
        scoreali = scoreali

    else :
      scoreali += help1 
        


   #  #mahdi rule
   #  #1 rule
    if assist == 0:
        scorema = scorema

    else:
        scorema += assist 

   #  #2 rule
    if p1_d == 0:
        scoreali = scoreali

    else :
     scoreali -= p1_d   

    data = load_data()

    data["ali_score"] += scoreali
    data["mahdi_score"] += scorema

    data["ali_kills"] += player1_kills
    data["mahdi_kills"] += player2_kills


    save_data(data)

    total_ali = data["ali_score"]
    total_mahdi = data["mahdi_score"]

    return f"""
    <h2>score</h2>

    <p>{player1}: {total_ali} score</p>

    <p>{player2}: {total_mahdi} score</p>

    <p>{player1}: {player1_kills} kills</p>

    <p>{player2}: {player2_kills} kills</p>

    <a href="/">next</a>
    """
    
    


if __name__ == "__main__":
    app.run(debug=True)
