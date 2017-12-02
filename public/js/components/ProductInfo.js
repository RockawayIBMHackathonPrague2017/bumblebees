import React from 'react';
import PropTypes from 'prop-types';
import { isNil } from 'ramda';
import ProductComparison from './ProductComparison';
import { formatPrice } from '../utils';

const ProductInfo = ({ URL, PRODUCTNAME, PRICE_VAT, DESCRIPTION, LABELS }) =>
    <div className="product-info">
        <div className="product-title"><a href={URL}>{PRODUCTNAME}</a></div>
        <div className="product-price">{formatPrice(PRICE_VAT)} Kč</div>
        <div className="product-description">{DESCRIPTION}</div>
        { !isNil(LABELS) && <ProductComparison LABELS={LABELS} /> }
        <button className="btn-primary">Přidat do košíku</button>
    </div>;

ProductInfo.propTypes = {
    DESCRIPTION: PropTypes.string,
    PRICE_VAT: PropTypes.string,
    PRODUCTNAME: PropTypes.string,
    URL: PropTypes.string,
};

export default ProductInfo;
