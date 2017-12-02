import React from 'react';
import PropTypes from 'prop-types';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { find, map, propEq } from 'ramda';
import { selectedProductActions, tipsActions } from '../actions';
import { demoProductsSelectors } from '../selectors';

class SelectBox extends React.Component {

    constructor(props) {
        super(props);
    }

    _handleSelectedProduct = (event) => {
        const selectedProduct = find(propEq('_id', event.target.value))(this.props.demoProducts);
        this.props._handleSelectedProduct(selectedProduct);
        this.props.getTips(selectedProduct._id);
    };

    renderSelectOptions = ({ _id, PRODUCTNAME }) => <option key={_id} value={_id}>{PRODUCTNAME}</option>;

    render() {
        return(
            <select onChange={this._handleSelectedProduct}>
                {map(this.renderSelectOptions, this.props.demoProducts)}
            </select>
        );
    }

}

const mapStateToProps = (state) => ({
    demoProducts: demoProductsSelectors.getDemoProducts(state),
});

const mapDispatchToProps = (dispatch) => ({
    _handleSelectedProduct: bindActionCreators(selectedProductActions.storeSelectedProduct, dispatch),
    getTips: bindActionCreators(tipsActions.getTips, dispatch),
});

SelectBox.propTypes = {
    _handleSelectedProduct: PropTypes.func,
    demoProducts: PropTypes.array,
    getTips: PropTypes.func,
};

export default connect(mapStateToProps, mapDispatchToProps)(SelectBox);
