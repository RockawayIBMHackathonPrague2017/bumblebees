import React from 'react';
import PropTypes from 'prop-types';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { tipsActions } from '../actions';

class SelectBox extends React.Component {

    _handleChange = (event) => this.props._handleChange(event.target.value);

    render() {
        return (
            <select onChange={this._handleChange}>
                <option>Vyber produkt</option>
                <option value="product-id-1">product-id-1</option>
                <option value="product-id-2">product-id-2</option>
                <option value="product-id-3">product-id-3</option>
                <option value="product-id-4">product-id-4</option>
            </select>
        )
    }
}

const mapDispatchToProps = (dispatch) => ({
    _handleChange: bindActionCreators(tipsActions.getTips, dispatch),
});

SelectBox.propTypes = {
    _handleChange: PropTypes.func,
};

export default connect(null, mapDispatchToProps)(SelectBox);
