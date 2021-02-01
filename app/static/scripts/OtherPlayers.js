import React from 'react';
import axios from 'axios';

import { Card, Container, Row, Col, ListGroup, Button } from 'react-bootstrap';

class OtherPlayers extends React.Component {
    constructor(props) {
        super(props);
        this.stealClick = this.stealClick.bind(this);
    }
    stealClick(e) {
        const reqHeader = { headers: {'Content-Type': 'application/json'} };
        const reqData = {
            thief: this.props.username,
            victim: e.target.dataset.victim
        };
        axios.post(`/player/stealFromPlayer`, reqData, reqHeader)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    this.props.refreshState();
                } else {
                    console.log("spend resources failed 1");
                }
            })
            .catch( res => {
                console.log("spend resources failed 2");
            });
    }

    render() {
        let otherPlayersSpreadRender;
        if (!!this.props.otherPlayers) {
            otherPlayersSpreadRender = this.props.otherPlayers.map((otherPlayer) => {
                return (
                    <Row>
                        <Col>
                        <Card>
                            <Card.Body>
                                <Card.Title>{otherPlayer.name}</Card.Title>
                                <ListGroup variant="flush">
                                    <ListGroup.Item>
                                    <span className='mr-3'>resource cards: {otherPlayer.resource_cards}</span>
                                    <Button variant="danger" onClick={this.stealClick} data-victim={otherPlayer.name}>Steal</Button>
                                    </ListGroup.Item>
                                    <ListGroup.Item>unplayed dev cards: {otherPlayer.unplayed_dev_cards} </ListGroup.Item>
                                    <ListGroup.Item>
                                    <p>
                                    played dev cards: {otherPlayer.played_dev_cards.join(", ")}
                                    </p>
                                    </ListGroup.Item>
                                </ListGroup>
                            </Card.Body>
                        </Card>
                        </Col>
                    </Row>
                );
            });
        }
        return (
        <Card>
            <Card.Header>Other Players</Card.Header>
            <Card.Body>
                <Container>
                    {otherPlayersSpreadRender}
                </Container>
            </Card.Body>
            </Card>
        );
    }}
export default OtherPlayers;