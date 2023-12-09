//This part includes the backend of the website which integrates the python method used during bidding

from bidding_system import BiddingSystem
from time import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

class BiddingSystem:
    def _init_(self):
        self.products = {}

    def add_product(self, product_id, min_price, max_price, auction_duration):
        self.products[product_id] = {
            'min_price': min_price,
            'max_price': max_price,
            'auction_duration': auction_duration,
            'start_time': time(),
            'end_time': time() + auction_duration,
            'bids': {}
        }

    # Implement the rest of the BiddingSystem class methods here (start_auction, place_bid, check_for_ties, get_current_bid, get_winning_bid)

# Initialize the bidding system
bidding_system = BiddingSystem()
bidding_system.add_product(1, 100, 500, auction_duration=60)  # Example product

@app.route('/')
def index():
    return render_template('index.html')  # Your HTML file renamed as index.html

@socketio.on('place_bid')
def place_bid(data):
    product_id = data['product_id']
    user_id = data['user_id']
    bid_amount = data['bid_amount']

    # Place bid in the bidding system
    bidding_system.place_bid(product_id, user_id, bid_amount)

    # Emit an event to update all clients with the new highest bid
    highest_bid = bidding_system.get_current_bid(product_id)
    emit('bid_update', {'product_id': product_id, 'highest_bid': highest_bid}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

