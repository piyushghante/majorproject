from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Infura provider URL (replace with your Infura URL)
infura_url = "https://polygon-amoy.infura.io/v3/41a8174eef734e4a9411c2e386bce358"
web3 = Web3(Web3.HTTPProvider(infura_url))

@app.route('/save_account', methods=['POST'])
def save_account():
    data = request.json
    account = data.get('account')

    if not account:
        return jsonify({'error': 'No account provided'}), 400

    # Here, you can perform operations like checking balance, interacting with smart contracts, etc.
    balance = web3.eth.get_balance(account)
    balance_in_ether = web3.fromWei(balance, 'ether')

    return jsonify({
        'account': account,
        'balance': str(balance_in_ether)
    })

if __name__ == '__main__':
    app.run(debug=True)
