import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
BIP0039_DIR = os.path.normpath(os.path.join(ROOT_DIR, 'bip39_word_list'))

MAX_AMOUNT = 2100000000000000
SIGHASH_ALL = 0x00000001
SIGHASH_NONE = 0x00000002
SIGHASH_SINGLE = 0x00000003
SIGHASH_ANYONECANPAY = 0x00000080
ECDSA_SEC256K1_ORDER = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

MAINNET_ADDRESS_BYTE_PREFIX = b'\x0a'
TESTNET_ADDRESS_BYTE_PREFIX = b'\x22'
MAINNET_SCRIPT_ADDRESS_BYTE_PREFIX = b'\x19'
TESTNET_SCRIPT_ADDRESS_BYTE_PREFIX = b'\x32'
MAINNET_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x03\x00\x02\x07\x0c'
TESTNET_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x03\x03\x00\x14\x02\x07\x0c'
REGTEST_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x03\x03\x00\x12\x02\x07\x0c'

MAINNET_ADDRESS_PREFIX = '5'
TESTNET_ADDRESS_PREFIX = 'E'
TESTNET_ADDRESS_PREFIX_2 = 'F'
MAINNET_SCRIPT_ADDRESS_PREFIX = 'B'
TESTNET_SCRIPT_ADDRESS_PREFIX = 'M'

MAINNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX = '5'
MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX = 'K'
MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX_2 = 'L'
TESTNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX = '9'
TESTNET_PRIVATE_KEY_COMPRESSED_PREFIX = 'c'

ADDRESS_PREFIX_LIST = (MAINNET_ADDRESS_PREFIX,
                       TESTNET_ADDRESS_PREFIX,
                       TESTNET_ADDRESS_PREFIX_2,
                       MAINNET_SCRIPT_ADDRESS_PREFIX,
                       TESTNET_SCRIPT_ADDRESS_PREFIX)

PRIVATE_KEY_PREFIX_LIST = (MAINNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX,
                           MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX,
                           MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX_2,
                           TESTNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX,
                           TESTNET_PRIVATE_KEY_COMPRESSED_PREFIX)

MAINNET_PRIVATE_KEY_BYTE_PREFIX = b'\x80'
TESTNET_PRIVATE_KEY_BYTE_PREFIX = b'\xef'

MAINNET_SEGWIT_ADDRESS_PREFIX = 'bgl'
TESTNET_SEGWIT_ADDRESS_PREFIX = 'tbgl'
REGTEST_SEGWIT_ADDRESS_PREFIX = 'rbgl'


SCRIPT_TYPES = {"P2PKH":        0,
                "P2SH":         1,
                "PUBKEY":       2,
                "NULL_DATA":    3,
                "MULTISIG":     4,
                "P2WPKH":       5,
                "P2WSH":        6,
                "NON_STANDARD": 7,
                "NULL_DATA_NON_STANDARD": 8
                }

SCRIPT_N_TYPES = {0: "P2PKH",
                  1: "P2SH",
                  2: "PUBKEY",
                  3: "NULL_DATA",
                  4: "MULTISIG",
                  5: "P2WPKH",
                  6: "P2WSH",
                  7: "NON_STANDARD",
                  8: "NULL_DATA_NON_STANDARD"
                }

# CONSTANTS hierarchical deterministic wallets (HD Wallets)
# m/44'/0' P2PKH
MAINNET_XPRIVATE_KEY_PREFIX = b'\x04\x88\xAD\xE4'
MAINNET_XPUBLIC_KEY_PREFIX = b'\x04\x88\xB2\x1E'

# m/44'/1' P2PKH
TESTNET_XPRIVATE_KEY_PREFIX = b'\x04\x35\x83\x94'
TESTNET_XPUBLIC_KEY_PREFIX = b'\x04\x35\x87\xCF'

# m/44'/0' P2PKH
MAINNET_M44_XPRIVATE_KEY_PREFIX = b'\x04\x88\xAD\xE4'
MAINNET_M44_XPUBLIC_KEY_PREFIX = b'\x04\x88\xB2\x1E'

# m/44'/1' P2PKH
TESTNET_M44_XPRIVATE_KEY_PREFIX = b'\x04\x35\x83\x94'
TESTNET_M44_XPUBLIC_KEY_PREFIX = b'\x04\x35\x87\xCF'



# m/49'/0' P2WPKH in P2SH
MAINNET_M49_XPRIVATE_KEY_PREFIX = b'\x04\x9d\x78\x78'
MAINNET_M49_XPUBLIC_KEY_PREFIX = b'\x04\x9d\x7c\xb2'

# m/49'/1' P2WPKH in P2SH
TESTNET_M49_XPRIVATE_KEY_PREFIX = b'\x04\x4a\x4e\x28'
TESTNET_M49_XPUBLIC_KEY_PREFIX = b'\x04\x4a\x52\x62'

# m/84'/0' P2WPKH
MAINNET_M84_XPRIVATE_KEY_PREFIX = b'\x04\xb2\x43\x0c'
MAINNET_M84_XPUBLIC_KEY_PREFIX = b'\x04\xb2\x47\x46'

# m/84'/1' P2WPKH
TESTNET_M84_XPRIVATE_KEY_PREFIX = b'\x04\x5f\x18\xbc'
TESTNET_M84_XPUBLIC_KEY_PREFIX = b'\x04\x5f\x1c\xf6'



HARDENED_KEY = 0x80000000
FIRST_HARDENED_CHILD = 0x80000000
PATH_LEVEL_BIP0044 = [0x8000002C, 0x80000000, 0x80000000, 0, 0]
TESTNET_PATH_LEVEL_BIP0044 = [0x8000002C, 0x80000001, 0x80000000, 0, 0]

MINER_COINBASE_TAG = {}

MINER_PAYOUT_TAG = {}



LN2SQUARED = 0.4804530139182014246671025263266649717305529515945455
LN2 = 0.6931471805599453094172321214581765680755001343602552
