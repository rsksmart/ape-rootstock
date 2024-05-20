from typing import cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (30, 775),
    "testnet": (31, 8100),
}


class RootstockConfig(BaseEthereumConfig):
    mainnet: NetworkConfig = create_network_config(block_time=30, required_confirmations=1)
    testnet: NetworkConfig = create_network_config(block_time=30, required_confirmations=1)


class Rootstock(Ethereum):
    fee_token_symbol: str = "RBTC"

    @property
    def config(self) -> RootstockConfig:  # type: ignore
        return cast(RootstockConfig, self.config_manager.get_config("rootstock"))
