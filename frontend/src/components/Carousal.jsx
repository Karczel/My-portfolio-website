import React from 'react';
import Slider from 'react-slick';
import DisplayLinkContent from './DisplayLinkContent';

const Carousel = ({ item }) => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  return (
    <div style={{ width: '100%', maxWidth: '900px', margin: '0 auto' }}>
      <Slider {...settings}>
        <div>
          <DisplayLinkContent item={item} />
        </div>
      </Slider>
    </div>
  );
};

export default Carousel;
