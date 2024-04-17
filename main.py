from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=contract_address, abi=abi)

print(f"адрес контракта: {contract_address}")
print(f"баланс смарт-контракта: {w3.eth.get_balance(contract_address)}")
print(f"баланс первого аккаунта: {w3.eth.get_balance('0x85E901f2015b1362AA995c3c9eD7385B1a32D8A5')}")
print(f"баланс второго аккаунта: {w3.eth.get_balance('0x46e51AF2514822dA044E2022FaFC79fffB49B0df')}")
print(f"баланс третьего аккаунта: {w3.eth.get_balance('0xa6c6D1C41Be295Cb4718D6AA343984Eb14268204')}")
print(f"баланс четвертого аккаунта: {w3.eth.get_balance('0x65a515693F12e7CCce061841EC6e451fA0a3bAfa')}")
print(f"баланс пятого аккаунта: {w3.eth.get_balance('0x1E3A4eb4D76e320F5ea54564F2Ea0a0F6ea159B5')}")
