import React from 'react';
import axios from 'axios';
import { Card, Button, Image } from 'react-bootstrap';

class Dice extends React.Component {
    constructor(props) {
        super(props);
        this.rollDice = this.rollDice.bind(this);
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
        let lastRollRender;
        if(this.props.lastRoll.length > 0) {
            lastRollRender = (
            <div>
                <div className="d-flex justify-content-center mb-3">
                    <Image className="mr-1" src={"/static/images/dice"+this.props.lastRoll[0]+".png"}
                        style={{height:'40%', width:'40%', opacity:0.5}} />
                    <Image src={"/static/images/dice"+this.props.lastRoll[1]+".png"}
                        style={{height:'40%', width:'40%', opacity:0.5}} />
                </div>
                <p>Dice total: {this.props.lastRoll[0] + this.props.lastRoll[1]}</p>
            </div>
            );
        }
        return (
            <Card>
                <Card.Header>Dice Roll</Card.Header>
                <Card.Body className="text-center">
                    {lastRollRender}
                    <Button variant="outline-success" onClick={this.rollDice}>Roll Dice</Button>
                </Card.Body>
            </Card>
        );
    }}
export default Dice;