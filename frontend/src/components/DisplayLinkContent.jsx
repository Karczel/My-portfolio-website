import React from 'react';

const DisplayLinkContent = ({ item }) => {
  const content = [];

  // Check if the item has an image to display
  if (item.image) {
    content.push(
      <div key="image">
        <img src={item.image} alt="Content" style={{ width: '100%', height: 'auto' }} />
        {item.desc && <p>{item.desc}</p>} {/* Show description if available */}
      </div>
    );
  }

  // Check if the item has a link (like repository)
  if (item.link) {
    content.push(
      <div key="link">
        <a href={item.link} target="_blank" rel="noopener noreferrer">
          <button>Visit Repository</button>
        </a>
        {item.desc && <p>{item.desc}</p>} {/* Show description if available */}
      </div>
    );
  }

  // Check if the item has a product field (either link or image)
  if (item.product) {
    // If the product is a URL to an image, display it as an image
    if (item.product.match(/\.(jpeg|jpg|gif|png)$/)) {
      content.push(
        <div key="product-image">
          <img src={item.product} alt="Product" style={{ width: '100%', height: 'auto' }} />
          {item.desc && <p>{item.desc}</p>}
        </div>
      );
    } else {
      // If the product is a link (web application), display it as a clickable link
      content.push(
        <div key="product-link">
          <a href={item.product} target="_blank" rel="noopener noreferrer">
            <button>Visit Product</button>
          </a>
          {item.desc && <p>{item.desc}</p>}
        </div>
      );
    }
  }

  return <>{content}</>;
};

export default DisplayLinkContent;
