import React from 'react';
import axios from 'axios';
import StoreResourceCard from "./StoreResourceCard";
import StoreDevCard from "./StoreDevCard";
import PlayerInventory from "./PlayerInventory";
import OtherPlayers from "./OtherPlayers";
import { Alert, CardGroup, Container, Row, Col } from 'react-bootstrap';

class GameView extends React.Component {
    constructor(props) {
        super(props);
        this.refreshState = this.refreshState.bind(this);
        this.state = {};
    }

    componentDidMount() {
        this.refreshState();
        this.refreshTimer = setInterval(()=> this.refreshState(), 8000);
    }
    componentWillUnmount() {
        clearInterval(this.refreshTimer);
        this.refreshTimer = null; // here...
    }

    refreshState() {
        axios.get(`/state?player=${this.props.username}`)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    // set state appropriately
                    this.setState(res.data);
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

        const resourceTypes = ['Wood', 'Brick', 'Sheep', 'Ore', 'Wheat'];
        let resourceCards;
        let devCard;
        if (!!this.state.store) {
            resourceCards = resourceTypes.map(resourceType => {
                return (<StoreResourceCard
                            username={this.props.username}
                            resourceType={resourceType}
                            resourceStock={this.state.store.resource_cards[resourceType]}
                            refreshState={this.refreshState}
                            />);
            });

            devCard = <StoreDevCard
                        username={this.props.username}
                        resourceStock={this.state.store.dev_cards}
                        refreshState={this.refreshState}
                        />
        }

        let otherPlayerRender;
        let otherPlayerNames = [];
        if(this.state.other_players) {
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
            <Container>
                <Row>
                    <Col sm={9}>
                    <Container>
                        <Row>
                            <Col>
                                <CardGroup>
                                {resourceCards}
                                </CardGroup>
                            </Col>
                        </Row>
                    </Container>
                    </Col>
                    <Col sm={2}>
                        {devCard}
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