import React from 'react';
import axios from 'axios';
import PlayerOwnedResource from './PlayerOwnedResource';
import PlayerOwnedDevCards from './PlayerOwnedDevCards';
import { Card } from 'react-bootstrap';

class PlayerInventory extends React.Component {
    render() {
        let playerOwnedResourceCards;
        let playerOwnedDevCards;
        let otherPlayerNames = [];
        if (this.props.otherPlayerNames) {
            otherPlayerNames = this.props.otherPlayerNames;
        }

        if (this.props.playerInventory) {
            playerOwnedResourceCards = (
                <PlayerOwnedResource
                    otherPlayerNames={otherPlayerNames}
                    username={this.props.playerInventory.name}
                    resourceCards={this.props.playerInventory.resource_cards}
                    refreshState={this.props.refreshState} />
            );

            playerOwnedDevCards = (
                <PlayerOwnedDevCards
                    username={this.props.playerInventory.name}
                    playedCards={this.props.playerInventory.played_dev_cards}
                    unplayedCards={this.props.playerInventory.unplayed_dev_cards}
                    refreshState={this.props.refreshState} />
            );
        }
        return (
            <Card>
                <Card.Header>Player Inventory</Card.Header>
                    {playerOwnedResourceCards}
                    {playerOwnedDevCards}
            </Card>
        );
    }
}
export default PlayerInventory;