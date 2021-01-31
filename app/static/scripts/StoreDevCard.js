import React from 'react';
import axios from 'axios';
import { Card, Button, InputGroup, FormControl } from 'react-bootstrap';

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
                    if(this.qtyInput) {
                        this.qtyInput.value = 0;
                    }
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
                    <InputGroup className="mb-3" size="sm">
                        <InputGroup.Prepend>
                            <InputGroup.Text id="resource-qty">Qty</InputGroup.Text>
                        </InputGroup.Prepend>
                        <FormControl
                                placeholder="0"
                                aria-label="resource-draw-qty"
                                aria-describedby="resource-draw-qty"
                                ref = {c => this.qtyInput = c}
                        />
                        <InputGroup.Append>
                            <Button variant="outline-secondary" onClick={this.buyDevCard}>Draw</Button>
                        </InputGroup.Append>
                    </InputGroup>

                </Card.Body>
            </Card>
        );
    }}
export default StoreDevCard;