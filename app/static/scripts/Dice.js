import React from 'react';
import axios from 'axios';
import { Card, Button } from 'react-bootstrap';

class Dice extends React.Component {
    constructor(props) {
        super(props);
        this.rollDice = this.rollDice.bind(this);
        this.state = {};
    }

    rollDice() {
        axios.get(`/dice/roll`)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    this.props.refreshState();
                } else {
                    console.log("Dice roll failed 1");
                }
            })
            .catch( res => {
                console.log("Dice roll failed 2");
            });
    }

    render() {
        return (
            <Card>
                <Card.Header>Dice Roll ({this.props.lastRoll})</Card.Header>
//                <Card.Img variant="top" src={"/static/images/Dev card.png"}/>
                <Card.Body>
                    <Button variant="outline-secondary" onClick={this.rollDice}>Roll Dice</Button>
                </Card.Body>
            </Card>
        );
    }}
export default Dice;