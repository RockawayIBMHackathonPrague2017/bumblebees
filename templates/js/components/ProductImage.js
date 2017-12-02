import React from 'react';
import PropTypes from 'prop-types';

const ProductImage = ({ IMGURL }) =>
    <div className="product-image">
        <div className="statuses">
            <div className="status">Vyšší parametry</div>
        </div>
        <img src={IMGURL} />
    </div>;

ProductImage.propTypes = {
    IMGURL: PropTypes.string,
};

export default ProductImage;
