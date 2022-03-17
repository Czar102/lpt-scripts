from web3 import Web3
import binascii
from utils.livepeer.abi.bonding_manager import bonding_manager_contract_abi
from utils.eth import get_contract

nullAddress = "0x0000000000000000000000000000000000000000"

w3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc')) # https://arb1.arbitrum.io/rpc
print(w3.isConnected())
contract = "0x35Bcf3c30594191d53231E4FF333E8A770453e40"
BondingManager = get_contract(w3, contract, bonding_manager_contract_abi)


def transferBondOwnership(sender, senderPrivate, recipient):
	amount = BondingManager.functions.getDelegator(sender).call()[3]

	tx = BondingManager.functions.transferBond(recipient, amount, nullAddress, nullAddress, nullAddress, nullAddress).buildTransaction()

	signedTx = w3.eth.account.sign_transaction(tx, senderPrivate)

	transactionHash = w3.eth.send_raw_transaction(signedTx.rawTransaction)

	receipt = w3.eth.wait_for_transaction_receipt(transactionHash)

	print("Bond ownership transfer:")
	print(receipt)



# 0. for testing purposes only!

# 1. send funds from the funder to the first account
# needs approx 0.0032 eth


def getTxOverWith(txDict, senderPrivate):
	signed_txn = w3.eth.account.sign_transaction(txDict, senderPrivate)

	transactionHash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

	receipt = w3.eth.wait_for_transaction_receipt(transactionHash)

	print("Pure tx:")
	print(receipt)


txInfo = [
	{
		"from": "0x08f10D03A0CF7a9eADdc7EacD4cf135a07A0feff",
		"fromPrivate": "", # Paste private for 0x08f10D03A0CF7a9eADdc7EacD4cf135a07A0feff here
		"data": "062e98b800000000000000000000000052cAC9F2df3068107c95DB3Acf3f6B1256d75E4500000000000000000000000000000000000000000000000384e3368bea0d64aa0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
	},
	{
		"from": "0xb1D0Bac0abBdfa8D7Ca6fA0973cfE84F79262967",
		"fromPrivate": "", # Paste private for 0xb1D0Bac0abBdfa8D7Ca6fA0973cfE84F79262967 here
		"data": "0x062e98b800000000000000000000000052cac9f2df3068107c95db3acf3f6b1256d75e45000000000000000000000000000000000000000000000008724232c4e68c01b40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
	},
	{
		"from": "0x1D2A89755cA40B1226b4D7A52E8aDDa610D08d46",
		"fromPrivate": "", # Paste private for 0x1D2A89755cA40B1226b4D7A52E8aDDa610D08d46 here
		"data": "0x062e98b800000000000000000000000052cac9f2df3068107c95db3acf3f6b1256d75e45000000000000000000000000000000000000000000000008c2c9ad2738df559c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
	},
]


# 2. wait until funds are rebonded

# 2. rebond funds on 0x08f10d03a0cf7a9eaddc7eacd4cf135a07a0feff
