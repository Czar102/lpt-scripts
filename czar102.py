from web3 import Web3
import binascii
from utils.livepeer.abi.bonding_manager import bonding_manager_contract_abi
from utils.eth import get_contract

nullAddress = "0x0000000000000000000000000000000000000000"

w3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc')) # https://arb1.arbitrum.io/rpc  https://rinkeby.arbitrum.io/rpc
print(w3.isConnected())
contract = "0x35Bcf3c30594191d53231E4FF333E8A770453e40" # 0xe42229d764F673EB3FB8B9a56016C2a4DA45ffd7
BondingManager = get_contract(w3, contract, bonding_manager_contract_abi)


def transferBondOwnership(sender, senderPrivate, recipient):
	ret = BondingManager.functions.getDelegator(sender).call()
	print(ret)
	amount = ret[0]

	tx = BondingManager.functions.transferBond(recipient, amount, nullAddress, nullAddress, nullAddress, nullAddress).buildTransaction(
		{
			"from": sender,
			"gasPrice": 1000000000,
			"nonce": w3.eth.get_transaction_count(sender)
		}
	)

	signedTx = w3.eth.account.sign_transaction(tx, senderPrivate)

	transactionHash = w3.eth.send_raw_transaction(signedTx.rawTransaction)

	receipt = w3.eth.wait_for_transaction_receipt(transactionHash)

	print("Bond ownership transfer:")
	print(receipt)


sender = input("Pass sender account: ")
senderPrivate = input("Input private key: ")
recipient = "0xd541B4316623Ed0Af28d029Bd447fD4c45472d68"

transferBondOwnership(sender, senderPrivate, recipient)