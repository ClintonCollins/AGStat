from flask import Flask, request, render_template
import query
import socket
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    print request.method
    if request.method == 'POST':
        ip = request.form['ip']
        port = request.form['port']
        game = request.form['game']
        print ip
        print port
        print game
        try:
            socket.inet_aton(ip)
        except socket.error:
            ip = socket.gethostbyname(ip)
        print 'Using IP: %s' % ip
        if game == 'starbound':
            lookup = query.SourceQuery(ip, int(port))
            data = lookup.main()
            players = data['players']
            player_list = data['player_list']
        else:
            return render_template('index.html')
        return render_template('data.html', players=players, player_list=player_list)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
