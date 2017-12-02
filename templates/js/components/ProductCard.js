import React from 'react';
import PropTypes from 'prop-types';
import ProductImage from './ProductImage';
import ProductInfo from './ProductInfo';

const ProductCard = ({ IMGURL, URL, PRODUCTNAME, PRICE_VAT, DESCRIPTION }) =>
    <div className="product-card">
        <ProductImage
            IMGURL={IMGURL}
        />
        <ProductInfo
            URL={URL}
            PRODUCTNAME={PRODUCTNAME}
            PRICE_VAT={PRICE_VAT}
            DESCRIPTION={DESCRIPTION}
        />
    </div>;

ProductCard.propTypes = {
    DESCRIPTION: PropTypes.string,
    IMGURL: PropTypes.string,
    PRICE_VAT: PropTypes.string,
    PRODUCTNAME: PropTypes.string,
    URL: PropTypes.string,
};

export default ProductCard;
