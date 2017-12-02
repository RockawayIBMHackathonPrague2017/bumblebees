import React from 'react';
import PropTypes from 'prop-types';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { demoProductsActions, tipsActions } from '../actions';

class RequestForm extends React.Component {

    constructor() {
        super();
        this.state = {
            input: '',
        };
    }

    _handleOnChange = (event) => this.setState({ input: event.target.value });

    _handleOnClick = (event) => {
        this.props.getDemoProduct(this.state.input);
        this.props.getTips(this.state.input);
    };

    render() {
        return (
            <form>
                <input type="text" placeholder="Enter product id..." onChange={this._handleOnChange} />
                <button type="submit" onClick={this._handleOnClick}>Submit</button>
            </form>
        );
    }
}

const mapDispatchToProps = (dispatch) => ({
    getDemoProduct: bindActionCreators(demoProductsActions.getDemoProduct, dispatch),
    getTips: bindActionCreators(tipsActions.getTips, dispatch),
});

RequestForm.propTypes = {
    _handleOnClick: PropTypes.func,
};

export default connect(null, mapDispatchToProps)(RequestForm);
