import React from 'react';
import { Card, Container, Form, Button, Row, Col } from 'react-bootstrap';

class Welcome extends React.Component {
    constructor(props) {
        super(props);
        this.usernameChange = this.usernameChange.bind(this);
        this.joinGameClick = this.joinGameClick.bind(this);
        this.keyPressed = this.keyPressed.bind(this);
        this.state = {};
    }

    joinGameClick() {
        this.props.usernameHandler(this.state.username);
    }

    usernameChange(e) {
        this.setState({username: e.target.value});
    }

    keyPressed(e) {
        if (event.key === "Enter") {
            this.joinGameClick();
        }
    }
    render() {
        return (
        <Container style={{"margin-top":"5em"}}>
            <Row>
                <Col>
                    <Card>
                        <Card.Body>
                            <Card.Title>Welcome to Team Catan</Card.Title>
                            <Form>
                                <Form.Group controlId="formPlayerName">
                                    <Form.Control type="text" placeholder="Name" onChange={this.usernameChange} onKeyPress={this.keyPressed}/>
                                    <Form.Text className="text-muted">
                                        If you have a game in progress, make sure to use the same name as before!! (CAPS and all)
                                    </Form.Text>
                                </Form.Group>
                                <Button variant="primary" onClick={this.joinGameClick}>Join Game</Button>
                            </Form>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
        );
    }}
export default Welcome;