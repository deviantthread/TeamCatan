import React from 'react';
import axios from 'axios';
import { Card, Button, InputGroup, FormControl } from 'react-bootstrap';

class StoreResourceCard extends React.Component {
    constructor(props) {
        super(props);
        this.resourceDrawClick = this.resourceDrawClick.bind(this);
        this.state = {};
    }

    resourceDrawClick() {
        const reqHeader = { headers: {'Content-Type': 'application/json'} };
        const reqData = {
            player: this.props.username,
            resources: {}
        }
        reqData.resources[this.props.resourceType] = parseInt(this.qtyInput.value);

        axios.post(`/store/withdraw`, reqData, reqHeader)
            .then(res => {
                if (res.status >= 200 && res.status < 300) {
                    if(this.qtyInput) {
                        this.qtyInput.value = 0;
                    }
                    this.props.refreshState();
                } else {
                    console.log("withdraw failed 1");
                }
            })
            .catch( res => {
                console.log("withdraw failed 2");
            });
    }

    render() {
        return (
            <Card>
                <Card.Header>{this.props.resourceType} ({this.props.resourceStock})</Card.Header>
                <Card.Img variant="top" src={"/static/images/" + this.props.resourceType + ".png"}/>
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
                            <Button variant="outline-secondary" onClick={this.resourceDrawClick}>Draw</Button>
                        </InputGroup.Append>
                    </InputGroup>

                </Card.Body>
            </Card>
        );
    }}
export default StoreResourceCard;