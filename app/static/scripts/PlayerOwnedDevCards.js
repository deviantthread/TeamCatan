import React from 'react';
import axios from 'axios';
import { Form, Card, Button, Container, Row, Col, ListGroup } from 'react-bootstrap';

class PlayerOwnedDevCards extends React.Component {
    constructor(props) {
        super(props);
        this.useDevCardClick = this.useDevCardClick.bind(this);
        this.devSelectChange = this.devSelectChange.bind(this);
        this.state = {};
    }
    useDevCardClick() {
        axios.put(`/player/playDevCard?player=${this.props.username}&devCard=${this.state.selectedCardType}`)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    this.setState({
                        selectedCardType : null,
                        selectedIndexOfType: null
                    });
                    this.props.refreshState();
                } else {
                    console.log("spend resources failed 1");
                }
            })
            .catch( res => {
                console.log("spend resources failed 2");
            });
    }

    devSelectChange(e) {
        const selectedCardType = e.target.dataset.devCardType;
        const index = e.target.dataset.devCardIndex;
        this.setState({
            selectedCardType : selectedCardType,
            selectedIndexOfType: index
        });
    }

    render() {

        const unplayedDevSpreadRender = this.props.unplayedCards.map((devCard, i) => {
            return (
                <ListGroup.Item>
                    <Form.Check
                      type='radio'
                      key={devCard+i}
                      id={devCard+i}
                      label={devCard}
                      data-dev-card-type={devCard}
                      data-dev-card-index={i}
                      name='unplayedDevCards'
                      onChange={this.devSelectChange}
                      checked={this.state.selectedCardType == devCard && this.state.selectedIndexOfType == i}
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