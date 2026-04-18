section = input("Enter section name: ").strip()
coordinator = input("Enter sports coordinator's name: ").strip()

sports = {
    1: "Basketball",
    2: "Volleyball",
    3: "Badminton",
    4: "Chess",
    5: "Table Tennis"
}

print("\nAvailable sports:")
for num, name in sports.items():
    print(f" {num}. {name}")

games = []   
TOTAL_SLOTS = 4

for i in range(1, TOTAL_SLOTS + 1):
    print(f"\nGame {i}:")
    while True:
        s_input = input(" Enter sport number (0 to skip, 1-5 to choose): ").strip()
        if s_input.isdigit():
            s = int(s_input)
            if 0 <= s <= 5:
                break
            else:
                print("  Please enter 0 or a number from 1 to 5.")
        else:
            print("  Please enter a valid integer (0-5).")

    if s == 0:
        games.append({"slot": i, "skipped": True})
        print("  This game slot is skipped.")
        continue

    sport_name = sports[s]
    opponent = input(" Enter opposing section name: ").strip()

    while True:
        result = input(" Enter result (W for win, L for loss): ").strip().upper()
        if result in ("W", "L"):
            break
        else:
            print("  Invalid input. Please enter W or L.")

    points = 3 if result == "W" else 0
    games.append({
        "slot": i,
        "skipped": False,
        "sport_num": s,
        "sport_name": sport_name,
        "opponent": opponent,
        "result": result,
        "points": points
    })

total_points = sum(g.get("points", 0) for g in games if not g.get("skipped", False))

if total_points >= 9:
    standing = "GOLD CONTENDER"
elif total_points >= 6:
    standing = "SILVER PUSH"
else:
    standing = "KEEP FIGHTING!"

print("\n" + "="*50)
print("GAME RESULTS BOARD")
print("="*50)
print(f"Section    : {section}")
print(f"Coordinator: {coordinator}")
print("-"*50)
print("Logged Games:")
for g in games:
    if g.get("skipped", False):
        print(f" Game {g['slot']}: skipped (sport = 0)")
    else:
        print(f" Game {g['slot']}: sport {g['sport_num']} ({g['sport_name']}), vs {g['opponent']}, {g['result']}  ->  {g['points']} pts")
print("-"*50)
parts = []
for g in games:
    if g.get("skipped", False):
        parts.append("0")
    else:
        parts.append(str(g["points"]))
expr = " + ".join(parts)
print(f"Total: {expr} = {total_points}  ->  {standing}")
print("="*50)
