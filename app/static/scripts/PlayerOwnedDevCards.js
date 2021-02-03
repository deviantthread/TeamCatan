import React from 'react';
import axios from 'axios';
import { Form, Card, Button, Container, Row, Col, ListGroup } from 'react-bootstrap';

class PlayerOwnedDevCards extends React.Component {
    constructor(props) {
        super(props);
        this.useDevCardClick = this.useDevCardClick.bind(this);
        this.devSelectChange = this.devSelectChange.bind(this);
    }
    useDevCardClick() {
        axios.put(`/player/playDevCard?player=${this.props.username}&devCard=${this.selectedCard}`)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    this.selectedCard = null;
                    this.props.refreshState();
                } else {
                    console.log("spend resources failed 1");
                }
            })
            .catch( res => {
                console.log("spend resources failed 2");
            });
    }
    // using janky class variable to avoid rerender - cuz react unmount and rerender doesn't work properly and keeps checkbox checked
    devSelectChange(e) {
        this.selectedCard = e.target.nextElementSibling.textContent.trim();
    }

    render() {

        const unplayedDevSpreadRender = this.props.unplayedCards.map((devCard, i) => {
            const uniqueHash = Math.random().toString(36).slice(-6); // so react can properly rerender after unmount
            return (
                <ListGroup.Item>
                    <Form.Check
                      type='radio'
                      key={devCard+i+uniqueHash}
                      id={devCard+i}
                      label={devCard}
                      name='unplayedDevCards'
                      onChange={this.devSelectChange}
                    />
                </ListGroup.Item>
            );
        });

        const playedDevSpreadRender = this.props.playedCards.map((devCard) => {
            return (
                <ListGroup.Item>
                    {devCard}
                </ListGroup.Item>
            );
        });
        return (
                <Card.Body>
                    <Card.Title>Dev Cards</Card.Title>
                    <Container>
                        <Row>
                        <Col>
                            Unplayed
                            <div className="overflow-auto" style={{height:'220px', border: '1px solid lightgrey', 'border-radius': '5px'}}>
                            <ListGroup>
                                {unplayedDevSpreadRender}
                            </ListGroup>
                            </div>
                            <Button className="mt-3" variant="dark" onClick={this.useDevCardClick}>Use</Button>
                        </Col>
                        <Col>
                            Played
                            <div className="overflow-auto" style={{height:'220px', border: '1px solid lightgrey', 'border-radius': '5px'}}>
                            <ListGroup>
                                {playedDevSpreadRender}
                            </ListGroup>
                            </div>
                        </Col>
                        </Row>
                    </Container>
                </Card.Body>
        );
    }}
export default PlayerOwnedDevCards;