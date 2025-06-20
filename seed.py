from models import db, Team, Player

def seed_data():
   if not Team.query.first():
        t1 = Team(name="Florida Gators", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/57.png")
        t2 = Team(name="Georgia Bulldogs", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/61.png")
        t3 = Team(name="LSU Tigers", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/99.png")
        t4 = Team(name="Alabama Crimson Tide", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/333.png")
        t5 = Team(name="Texas A&M Aggies", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/245.png")
        t6 = Team(name="Tennessee Volunteers", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/2633.png")
        t7 = Team(name="Ole Miss Rebels", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/145.png")
        t8 = Team(name="Mississippi State Bulldogs", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/344.png")
        t9 = Team(name="Arkansas Razorbacks", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/8.png")
        t10 = Team(name="South Carolina Gamecocks", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/2579.png")
        t11 = Team(name="Kentucky Wildcats", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/96.png")
        t12 = Team(name="Missouri Tigers", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/142.png")
        t13 = Team(name="Auburn Tigers", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/2.png")
        t14 = Team(name="Vanderbilt Commodores", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/238.png")
        t15 = Team(name="Texas Longhorns", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/251.png")
        t16 = Team(name="Oklahoma Sooners", logo_url="https://a.espncdn.com/i/teamlogos/ncaa/500/201.png")
        db.session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16])
        db.session.commit()
        db.session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16])
        db.session.commit()

        players = [
            Player(name="Player 10", position="OL", nil_value=0.13, depth=1, team_id=t1.id),
            Player(name="Player 11", position="S", nil_value=0.46, depth=3, team_id=t1.id),
            Player(name="Player 12", position="RB", nil_value=0.51, depth=1, team_id=t1.id),
            Player(name="Player 13", position="OL", nil_value=1.07, depth=2, team_id=t1.id),
            Player(name="Player 14", position="P", nil_value=0.23, depth=3, team_id=t1.id),
            Player(name="Player 15", position="RB", nil_value=1.77, depth=2, team_id=t1.id),
            Player(name="Player 16", position="OL", nil_value=1.15, depth=2, team_id=t1.id),
            Player(name="Player 17", position="TE", nil_value=2.45, depth=1, team_id=t1.id),
            Player(name="Player 18", position="DL", nil_value=0.91, depth=3, team_id=t1.id),
            Player(name="Player 19", position="QB", nil_value=2.22, depth=2, team_id=t1.id),
            Player(name="Player 110", position="CB", nil_value=1.74, depth=2, team_id=t1.id),
            Player(name="Player 111", position="DL", nil_value=0.58, depth=2, team_id=t1.id),
            Player(name="Player 20", position="LB", nil_value=0.86, depth=3, team_id=t2.id),
            Player(name="Player 21", position="WR", nil_value=1.17, depth=1, team_id=t2.id),
            Player(name="Player 22", position="RB", nil_value=1.8, depth=2, team_id=t2.id),
            Player(name="Player 23", position="DL", nil_value=0.65, depth=3, team_id=t2.id),
            Player(name="Player 24", position="OL", nil_value=0.54, depth=3, team_id=t2.id),
            Player(name="Player 25", position="CB", nil_value=0.36, depth=2, team_id=t2.id),
            Player(name="Player 26", position="K", nil_value=1.76, depth=1, team_id=t2.id),
            Player(name="Player 27", position="K", nil_value=0.68, depth=2, team_id=t2.id),
            Player(name="Player 28", position="RB", nil_value=0.6, depth=3, team_id=t2.id),
            Player(name="Player 29", position="OL", nil_value=1.43, depth=3, team_id=t2.id),
            Player(name="Player 210", position="S", nil_value=1.66, depth=1, team_id=t2.id),
            Player(name="Player 211", position="OL", nil_value=2.14, depth=2, team_id=t2.id),
            Player(name="Player 30", position="QB", nil_value=0.87, depth=3, team_id=t3.id),
            Player(name="Player 31", position="OL", nil_value=0.35, depth=1, team_id=t3.id),
            Player(name="Player 32", position="P", nil_value=1.88, depth=3, team_id=t3.id),
            Player(name="Player 33", position="QB", nil_value=0.83, depth=2, team_id=t3.id),
            Player(name="Player 34", position="TE", nil_value=2.38, depth=2, team_id=t3.id),
            Player(name="Player 35", position="TE", nil_value=0.63, depth=2, team_id=t3.id),
            Player(name="Player 36", position="WR", nil_value=0.39, depth=2, team_id=t3.id),
            Player(name="Player 37", position="K", nil_value=0.77, depth=1, team_id=t3.id),
            Player(name="Player 38", position="P", nil_value=1.5, depth=2, team_id=t3.id),
            Player(name="Player 39", position="S", nil_value=2.23, depth=1, team_id=t3.id),
            Player(name="Player 310", position="WR", nil_value=1.61, depth=1, team_id=t3.id),
            Player(name="Player 311", position="S", nil_value=1.8, depth=3, team_id=t3.id),
            Player(name="Player 40", position="CB", nil_value=1.82, depth=1, team_id=t4.id),
            Player(name="Player 41", position="WR", nil_value=1.39, depth=2, team_id=t4.id),
            Player(name="Player 42", position="DL", nil_value=1.54, depth=2, team_id=t4.id),
            Player(name="Player 43", position="K", nil_value=0.93, depth=3, team_id=t4.id),
            Player(name="Player 44", position="S", nil_value=2.49, depth=2, team_id=t4.id),
            Player(name="Player 45", position="CB", nil_value=1.41, depth=3, team_id=t4.id),
            Player(name="Player 46", position="S", nil_value=1.58, depth=3, team_id=t4.id),
            Player(name="Player 47", position="WR", nil_value=0.21, depth=3, team_id=t4.id),
            Player(name="Player 48", position="TE", nil_value=1.42, depth=3, team_id=t4.id),
            Player(name="Player 49", position="OL", nil_value=1.2, depth=2, team_id=t4.id),
            Player(name="Player 410", position="CB", nil_value=1.61, depth=3, team_id=t4.id),
            Player(name="Player 411", position="K", nil_value=1.88, depth=1, team_id=t4.id),
            Player(name="Player 50", position="RB", nil_value=0.44, depth=1, team_id=t5.id),
            Player(name="Player 51", position="DL", nil_value=0.3, depth=2, team_id=t5.id),
            Player(name="Player 52", position="P", nil_value=0.16, depth=2, team_id=t5.id),
            Player(name="Player 53", position="K", nil_value=0.36, depth=2, team_id=t5.id),
            Player(name="Player 54", position="WR", nil_value=2.04, depth=2, team_id=t5.id),
            Player(name="Player 55", position="WR", nil_value=0.94, depth=2, team_id=t5.id),
            Player(name="Player 56", position="WR", nil_value=0.3, depth=3, team_id=t5.id),
            Player(name="Player 57", position="OL", nil_value=1.19, depth=3, team_id=t5.id),
            Player(name="Player 58", position="RB", nil_value=2.13, depth=3, team_id=t5.id),
            Player(name="Player 59", position="TE", nil_value=2.19, depth=2, team_id=t5.id),
            Player(name="Player 510", position="K", nil_value=1.32, depth=2, team_id=t5.id),
            Player(name="Player 511", position="RB", nil_value=0.99, depth=1, team_id=t5.id),
            Player(name="Player 60", position="TE", nil_value=1.96, depth=2, team_id=t6.id),
            Player(name="Player 61", position="WR", nil_value=1.79, depth=3, team_id=t6.id),
            Player(name="Player 62", position="CB", nil_value=0.96, depth=3, team_id=t6.id),
            Player(name="Player 63", position="RB", nil_value=0.98, depth=2, team_id=t6.id),
            Player(name="Player 64", position="TE", nil_value=1.6, depth=2, team_id=t6.id),
            Player(name="Player 65", position="S", nil_value=0.34, depth=3, team_id=t6.id),
            Player(name="Player 66", position="LB", nil_value=1.26, depth=2, team_id=t6.id),
            Player(name="Player 67", position="QB", nil_value=0.88, depth=2, team_id=t6.id),
            Player(name="Player 68", position="K", nil_value=2.43, depth=2, team_id=t6.id),
            Player(name="Player 69", position="K", nil_value=1.03, depth=1, team_id=t6.id),
            Player(name="Player 610", position="CB", nil_value=1.07, depth=3, team_id=t6.id),
            Player(name="Player 611", position="P", nil_value=1.06, depth=1, team_id=t6.id),
            Player(name="Player 70", position="OL", nil_value=1.7, depth=3, team_id=t7.id),
            Player(name="Player 71", position="S", nil_value=0.38, depth=3, team_id=t7.id),
            Player(name="Player 72", position="QB", nil_value=1.86, depth=2, team_id=t7.id),
            Player(name="Player 73", position="K", nil_value=0.43, depth=2, team_id=t7.id),
            Player(name="Player 74", position="WR", nil_value=0.62, depth=2, team_id=t7.id),
            Player(name="Player 75", position="OL", nil_value=0.19, depth=1, team_id=t7.id),
            Player(name="Player 76", position="TE", nil_value=0.93, depth=2, team_id=t7.id),
            Player(name="Player 77", position="OL", nil_value=0.5, depth=3, team_id=t7.id),
            Player(name="Player 78", position="CB", nil_value=0.6, depth=2, team_id=t7.id),
            Player(name="Player 79", position="TE", nil_value=2.49, depth=2, team_id=t7.id),
            Player(name="Player 710", position="K", nil_value=0.43, depth=3, team_id=t7.id),
            Player(name="Player 711", position="TE", nil_value=1.36, depth=3, team_id=t7.id),
            Player(name="Player 80", position="DL", nil_value=0.62, depth=1, team_id=t8.id),
            Player(name="Player 81", position="CB", nil_value=2.0, depth=2, team_id=t8.id),
            Player(name="Player 82", position="LB", nil_value=1.19, depth=2, team_id=t8.id),
            Player(name="Player 83", position="QB", nil_value=2.5, depth=3, team_id=t8.id),
            Player(name="Player 84", position="DL", nil_value=0.5, depth=3, team_id=t8.id),
            Player(name="Player 85", position="TE", nil_value=2.18, depth=2, team_id=t8.id),
            Player(name="Player 86", position="S", nil_value=2.36, depth=3, team_id=t8.id),
            Player(name="Player 87", position="QB", nil_value=1.18, depth=1, team_id=t8.id),
            Player(name="Player 88", position="LB", nil_value=1.4, depth=3, team_id=t8.id),
            Player(name="Player 89", position="S", nil_value=1.14, depth=2, team_id=t8.id),
            Player(name="Player 810", position="K", nil_value=1.28, depth=2, team_id=t8.id),
            Player(name="Player 811", position="TE", nil_value=1.49, depth=2, team_id=t8.id),
            Player(name="Player 90", position="S", nil_value=1.18, depth=3, team_id=t9.id),
            Player(name="Player 91", position="S", nil_value=0.6, depth=3, team_id=t9.id),
            Player(name="Player 92", position="S", nil_value=0.32, depth=1, team_id=t9.id),
            Player(name="Player 93", position="S", nil_value=1.05, depth=1, team_id=t9.id),
            Player(name="Player 94", position="QB", nil_value=2.45, depth=1, team_id=t9.id),
            Player(name="Player 95", position="WR", nil_value=0.27, depth=1, team_id=t9.id),
            Player(name="Player 96", position="TE", nil_value=2.18, depth=1, team_id=t9.id),
            Player(name="Player 97", position="QB", nil_value=1.03, depth=1, team_id=t9.id),
            Player(name="Player 98", position="OL", nil_value=0.35, depth=1, team_id=t9.id),
            Player(name="Player 99", position="RB", nil_value=2.08, depth=2, team_id=t9.id),
            Player(name="Player 910", position="OL", nil_value=0.34, depth=3, team_id=t9.id),
            Player(name="Player 911", position="CB", nil_value=0.19, depth=3, team_id=t9.id),
            Player(name="Player 100", position="DL", nil_value=0.99, depth=3, team_id=t10.id),
            Player(name="Player 101", position="TE", nil_value=1.33, depth=2, team_id=t10.id),
            Player(name="Player 102", position="TE", nil_value=0.18, depth=3, team_id=t10.id),
            Player(name="Player 103", position="S", nil_value=2.44, depth=3, team_id=t10.id),
            Player(name="Player 104", position="K", nil_value=1.55, depth=3, team_id=t10.id),
            Player(name="Player 105", position="QB", nil_value=2.46, depth=1, team_id=t10.id),
            Player(name="Player 106", position="S", nil_value=0.75, depth=3, team_id=t10.id),
            Player(name="Player 107", position="LB", nil_value=1.71, depth=2, team_id=t10.id),
            Player(name="Player 108", position="S", nil_value=0.4, depth=1, team_id=t10.id),
            Player(name="Player 109", position="CB", nil_value=0.29, depth=1, team_id=t10.id),
            Player(name="Player 1010", position="DL", nil_value=1.97, depth=2, team_id=t10.id),
            Player(name="Player 1011", position="S", nil_value=1.75, depth=1, team_id=t10.id),
            Player(name="Player 110", position="OL", nil_value=2.41, depth=1, team_id=t11.id),
            Player(name="Player 111", position="TE", nil_value=1.88, depth=2, team_id=t11.id),
            Player(name="Player 112", position="CB", nil_value=0.76, depth=2, team_id=t11.id),
            Player(name="Player 113", position="S", nil_value=2.25, depth=2, team_id=t11.id),
            Player(name="Player 114", position="TE", nil_value=2.18, depth=1, team_id=t11.id),
            Player(name="Player 115", position="QB", nil_value=2.25, depth=2, team_id=t11.id),
            Player(name="Player 116", position="RB", nil_value=0.76, depth=2, team_id=t11.id),
            Player(name="Player 117", position="TE", nil_value=2.11, depth=3, team_id=t11.id),
            Player(name="Player 118", position="LB", nil_value=1.04, depth=1, team_id=t11.id),
            Player(name="Player 119", position="RB", nil_value=2.43, depth=3, team_id=t11.id),
            Player(name="Player 1110", position="CB", nil_value=1.53, depth=2, team_id=t11.id),
            Player(name="Player 1111", position="DL", nil_value=1.08, depth=3, team_id=t11.id),
            Player(name="Player 120", position="CB", nil_value=1.06, depth=2, team_id=t12.id),
            Player(name="Player 121", position="DL", nil_value=0.39, depth=1, team_id=t12.id),
            Player(name="Player 122", position="OL", nil_value=0.71, depth=3, team_id=t12.id),
            Player(name="Player 123", position="QB", nil_value=0.28, depth=1, team_id=t12.id),
            Player(name="Player 124", position="P", nil_value=1.97, depth=1, team_id=t12.id),
            Player(name="Player 125", position="LB", nil_value=0.21, depth=2, team_id=t12.id),
            Player(name="Player 126", position="P", nil_value=0.11, depth=3, team_id=t12.id),
            Player(name="Player 127", position="WR", nil_value=0.75, depth=3, team_id=t12.id),
            Player(name="Player 128", position="QB", nil_value=2.25, depth=3, team_id=t12.id),
            Player(name="Player 129", position="TE", nil_value=1.32, depth=3, team_id=t12.id),
            Player(name="Player 1210", position="QB", nil_value=0.17, depth=3, team_id=t12.id),
            Player(name="Player 1211", position="CB", nil_value=2.12, depth=2, team_id=t12.id),
            Player(name="Player 130", position="CB", nil_value=2.09, depth=2, team_id=t13.id),
            Player(name="Player 131", position="OL", nil_value=1.45, depth=3, team_id=t13.id),
            Player(name="Player 132", position="OL", nil_value=1.56, depth=1, team_id=t13.id),
            Player(name="Player 133", position="RB", nil_value=1.95, depth=1, team_id=t13.id),
            Player(name="Player 134", position="WR", nil_value=0.87, depth=3, team_id=t13.id),
            Player(name="Player 135", position="S", nil_value=1.79, depth=1, team_id=t13.id),
            Player(name="Player 136", position="QB", nil_value=0.98, depth=1, team_id=t13.id),
            Player(name="Player 137", position="QB", nil_value=0.2, depth=1, team_id=t13.id),
            Player(name="Player 138", position="DL", nil_value=2.37, depth=1, team_id=t13.id),
            Player(name="Player 139", position="TE", nil_value=1.11, depth=2, team_id=t13.id),
            Player(name="Player 1310", position="CB", nil_value=1.09, depth=3, team_id=t13.id),
            Player(name="Player 1311", position="LB", nil_value=1.5, depth=3, team_id=t13.id),
            Player(name="Player 140", position="WR", nil_value=1.64, depth=2, team_id=t14.id),
            Player(name="Player 141", position="CB", nil_value=1.22, depth=3, team_id=t14.id),
            Player(name="Player 142", position="K", nil_value=1.74, depth=1, team_id=t14.id),
            Player(name="Player 143", position="LB", nil_value=1.29, depth=3, team_id=t14.id),
            Player(name="Player 144", position="OL", nil_value=1.21, depth=2, team_id=t14.id),
            Player(name="Player 145", position="WR", nil_value=0.22, depth=1, team_id=t14.id),
            Player(name="Player 146", position="WR", nil_value=1.63, depth=2, team_id=t14.id),
            Player(name="Player 147", position="K", nil_value=0.55, depth=1, team_id=t14.id),
            Player(name="Player 148", position="TE", nil_value=2.31, depth=3, team_id=t14.id),
            Player(name="Player 149", position="WR", nil_value=2.13, depth=2, team_id=t14.id),
            Player(name="Player 1410", position="DL", nil_value=0.32, depth=2, team_id=t14.id),
            Player(name="Player 1411", position="K", nil_value=1.15, depth=1, team_id=t14.id),
            Player(name="Player 150", position="OL", nil_value=2.31, depth=3, team_id=t15.id),
            Player(name="Player 151", position="WR", nil_value=1.43, depth=3, team_id=t15.id),
            Player(name="Player 152", position="P", nil_value=0.16, depth=1, team_id=t15.id),
            Player(name="Player 153", position="S", nil_value=2.08, depth=2, team_id=t15.id),
            Player(name="Player 154", position="DL", nil_value=2.19, depth=2, team_id=t15.id),
            Player(name="Player 155", position="WR", nil_value=0.41, depth=2, team_id=t15.id),
            Player(name="Player 156", position="TE", nil_value=2.2, depth=2, team_id=t15.id),
            Player(name="Player 157", position="S", nil_value=1.94, depth=2, team_id=t15.id),
            Player(name="Player 158", position="LB", nil_value=0.15, depth=3, team_id=t15.id),
            Player(name="Player 159", position="P", nil_value=1.76, depth=1, team_id=t15.id),
            Player(name="Player 1510", position="OL", nil_value=0.19, depth=2, team_id=t15.id),
            Player(name="Player 1511", position="WR", nil_value=0.78, depth=1, team_id=t15.id),
            Player(name="Player 160", position="CB", nil_value=1.5, depth=1, team_id=t16.id),
            Player(name="Player 161", position="OL", nil_value=2.42, depth=2, team_id=t16.id),
            Player(name="Player 162", position="S", nil_value=0.22, depth=3, team_id=t16.id),
            Player(name="Player 163", position="WR", nil_value=2.4, depth=2, team_id=t16.id),
            Player(name="Player 164", position="LB", nil_value=1.41, depth=3, team_id=t16.id),
            Player(name="Player 165", position="P", nil_value=1.44, depth=3, team_id=t16.id),
            Player(name="Player 166", position="RB", nil_value=2.15, depth=3, team_id=t16.id),
            Player(name="Player 167", position="TE", nil_value=0.38, depth=3, team_id=t16.id),
            Player(name="Player 168", position="LB", nil_value=0.64, depth=1, team_id=t16.id),
            Player(name="Player 169", position="P", nil_value=2.22, depth=2, team_id=t16.id),
            Player(name="Player 1610", position="DL", nil_value=0.83, depth=3, team_id=t16.id),
            Player(name="Player 1611", position="DL", nil_value=0.5, depth=1, team_id=t16.id),
        ]
        db.session.add_all(players)
        db.session.commit()