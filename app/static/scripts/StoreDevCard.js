import React from 'react';
import axios from 'axios';
import { Card, Button } from 'react-bootstrap';

class StoreDevCard extends React.Component {
    constructor(props) {
        super(props);
        this.buyDevCard = this.buyDevCard.bind(this);
        this.state = {};
    }

    buyDevCard() {
        axios.put(`/store/buyDevCard?player=${this.props.username}`)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    this.props.refreshState();
                } else {
                    console.log("Buy dev card failed 1");
                }
            })
            .catch( res => {
                console.log("Buy dev card failed 2");
            });
    }

    render() {
        return (
            <Card>
                <Card.Header>Dev Cards ({this.props.resourceStock})</Card.Header>
                <Card.Img variant="top" src={"/static/images/Dev card.png"}/>
                <Card.Body>
                    <Button variant="outline-secondary" onClick={this.buyDevCard}>Draw</Button>
                </Card.Body>
            </Card>
        );
    }}
export default StoreDevCard;