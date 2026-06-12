import random

class Match:
    def __init__(self):
        self.minute = 0
        self.home_goals = 0
        self.away_goals = 0

    def advance_minute(self):
        self.minute += 1

    def pass_ball(self, passer, receiver):
        return f"{self.minute}' Ball passed from {passer} to {receiver}"

    def dribble_ball(self, dribbler):
        return f"{self.minute}' {dribbler} dribbles the ball forward"

    def shoot_ball(self, shooter):
        return f"{self.minute}' {shooter} takes a shot"

    def goal_scored(self, scorer, home):
        if home:
            self.home_goals += 1
        else:
            self.away_goals += 1

        return (
            f"{self.minute}' GOAL! {scorer} scores!\n"
            f"Score: Home {self.home_goals} - {self.away_goals} Away"
        )

    def save_shot(self, keeper, shooter):
        return f"{self.minute}' {keeper} saves a shot from {shooter}"

    def half_time(self):
        return (
            f"{self.minute}' Half Time\n"
            f"Score: Home {self.home_goals} - {self.away_goals} Away"
        )

    def full_time(self):
        return (
            f"{self.minute}' Full Time\n"
            f"Final Score: Home {self.home_goals} - {self.away_goals} Away"
        )


match = Match()

for minute in range(1, 91):
    if minute==45:
        print("\n==HALF TIME==\n")
        continue

    match.minute = minute

    event = random.choice([
        "pass",
        "dribble",
        "shot"
    ])

    if event == "pass":
        print(match.pass_ball("a", "b"))

    elif event == "dribble":
        print(match.dribble_ball("a"))

    elif event == "shot":
        print(match.shoot_ball("a"))

        if random.random()<0.15:
            print(match.goal_scored("a",True))
        else:
            print(match.save_shot("c","a"))

print("\n==FINAL SCORE==\n")
print(f"Final Score: Home{match.home_goals} - Away{match.away_goals}")