import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { selectedProductSelectors } from '../selectors';
import { formatPrice } from '../utils';
import ProductComparison from './ProductComparison';
import { isNil } from 'ramda';

const ProductDetail = ({ selectedProduct: { IMGURL, PRODUCTNAME, DESCRIPTION, PRICE_VAT, LABELS } }) =>
    <div className="detail">
        <div className="left-column">
            <div className="image">
                <div className="statuses">
                    <span className="status">Doprava zdarma</span>
                </div>
                <img src={IMGURL} alt="Product photo" />
            </div>
        </div>
        <div className="right-column">
            <div className="info">
                <div><h1>{PRODUCTNAME}</h1></div>
                <div className="description">
                    {DESCRIPTION}
                </div>
                <div className="price">{formatPrice(PRICE_VAT)} Kč</div>
            <button className="btn-primary">Přidat do košíku</button>
            </div>
        </div>
    </div>;

const mapStateToProps = (state) => ({
    selectedProduct: selectedProductSelectors.getSelectedProduct(state),
});

ProductDetail.propTypes = {
    selectedProduct: PropTypes.object,
};

export default connect(mapStateToProps)(ProductDetail);
