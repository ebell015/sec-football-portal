from flask import Flask, render_template, redirect, url_for, request
from models import db, connect_db, Team, Player
from forms import PlayerForm
from seed import seed_data

app = Flask(__name__)
app.config.from_object('config.Config')
connect_db(app)

# ✅ Create tables and seed data inside app context
with app.app_context():
    db.create_all()
    seed_data()

@app.route('/')
def home():
    teams = Team.query.all()
    return render_template('home.html', teams=teams)

@app.route('/team/<int:team_id>')
def team_detail(team_id):
    team = Team.query.get_or_404(team_id)
    from collections import defaultdict
    grouped = defaultdict(list)
    for player in sorted(team.players, key=lambda p: (p.position, p.depth)):
        grouped[player.position].append(player)
    return render_template("team_detail.html", team=team, grouped=grouped)

@app.route('/player/<int:player_id>')
def player_detail(player_id):
    player = Player.query.get_or_404(player_id)
    return render_template('player_detail.html', player=player)

@app.route('/player/new', methods=['GET', 'POST'])
def new_player():
    form = PlayerForm()
    if form.validate_on_submit():
        player = Player(
            name=form.name.data,
            position=form.position.data,
            nil_value=form.nil_value.data,
            team_id=form.team_id.data
        )
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('player_form.html', form=form)

@app.route('/player/<int:player_id>/edit', methods=['GET', 'POST'])
def edit_player(player_id):
    player = Player.query.get_or_404(player_id)
    form = PlayerForm(obj=player)
    if form.validate_on_submit():
        form.populate_obj(player)
        db.session.commit()
        return redirect(url_for('player_detail', player_id=player.id))
    return render_template('player_form.html', form=form)

@app.route('/player/<int:player_id>/transfer', methods=['GET', 'POST'])
def transfer_player(player_id):
    player = Player.query.get_or_404(player_id)
    teams = Team.query.filter(Team.id != player.team_id).all()

    if request.method == 'POST':
        new_team_id = request.form.get('team_id')
        if new_team_id:
            player.team_id = int(new_team_id)
            db.session.commit()
            return redirect(url_for('player_detail', player_id=player.id))

    return render_template('transfer.html', player=player, teams=teams)


@app.route('/player/<int:player_id>/delete', methods=['POST'])
def delete_player(player_id):
    player = Player.query.get_or_404(player_id)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('home'))

from forms import PlayerForm, TeamForm  # make sure TeamForm is imported

@app.route('/team/new', methods=['GET', 'POST'])
def new_team():
    form = TeamForm()
    if form.validate_on_submit():
        team = Team(name=form.name.data)
        db.session.add(team)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('team_form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
