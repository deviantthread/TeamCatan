import React from 'react';
import axios from 'axios';
import StoreResourceCard from "./StoreResourceCard";
import StoreDevCard from "./StoreDevCard";
import PlayerInventory from "./PlayerInventory";
import OtherPlayers from "./OtherPlayers";
import Dice from "./Dice";
import { Alert, CardGroup, Container, Row, Col } from 'react-bootstrap';

class GameView extends React.Component {
    constructor(props) {
        super(props);
        this.refreshState = this.refreshState.bind(this);
        this.state = {};
    }

    componentDidMount() {
        this.refreshState();
        this.refreshTimer = setInterval(()=> this.refreshState(), 2000);
    }
    componentWillUnmount() {
        clearInterval(this.refreshTimer);
        this.refreshTimer = null;
    }

    refreshState() {
        axios.get(`/state?player=${this.props.username}`)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    if (!this.state.time || res.data.time > this.state.time) {
                        this.setState(res.data);
                    }
                } else {
                    this.props.usernameUnsetHandler();
                }
            })
            .catch( res => {
                console.log("catch");
                this.props.usernameUnsetHandler();
            });
    }

    render() {
        console.log(this.state.current_player);
        let playerName;
        if (!!this.state.current_player) {
            playerName = (
                <Alert variant="dark">
                    Hello {this.props.username}!
                </Alert>
                );
        }

        const resourceTypes = ['Wood', 'Brick', 'Sheep', 'Wheat', 'Ore'];
        let resourceCards = [];
        let devCard;
        if (!!this.state.store) {
            Object.keys(this.state.store.resource_cards).forEach(key => {
                resourceCards.push(
                    <StoreResourceCard
                        username={this.props.username}
                        resourceType={key}
                        resourceStock={this.state.store.resource_cards[key]}
                        refreshState={this.refreshState}
                        />
                );
            });

            devCard = <StoreDevCard
                        username={this.props.username}
                        resourceStock={this.state.store.dev_cards}
                        refreshState={this.refreshState}
                        />

        }

        let dice = <Dice
                        lastRoll={this.state.last_roll || []}
                        refreshState={this.refreshState}
                        />

        let otherPlayerRender;
        let otherPlayerNames = [];
        if (this.state.other_players) {
            otherPlayerNames = this.state.other_players.map(function (otherPlayer) { return otherPlayer.name; });
        }

        if (!!this.state.current_player) {
            otherPlayerRender = (
                <OtherPlayers
                    username={this.state.current_player.name}
                    otherPlayers={this.state.other_players}
                    refreshState={this.refreshState} />
            )
        }

        return (
        <div>
            {playerName}
            <Container fluid>
                <Row>
                    <Col>
                        <CardGroup>
                        {resourceCards}
                        {devCard}
                        {dice}
                        </CardGroup>
                    </Col>
                </Row>
                <Row style={{height: '30px'}}>
                </Row>
                <Row>
                    <Col sm>
                        <PlayerInventory
                            playerInventory={this.state.current_player}
                            refreshState={this.refreshState}
                            otherPlayerNames={otherPlayerNames}
                        />
                    </Col>
                    <Col sm>
                        {otherPlayerRender}
                    </Col>
                </Row>
            </Container>
        </div>
        );
    }}
export default GameView;