import React from 'react';
import '@/theme/LinkedIcon.css'; // Import the CSS file

const LinkedIcon = ({ item }) => {
  return (
    <div className="icon-item">
      <a href={item.link} target="_blank" rel="noopener noreferrer" className="icon-link">
        <img src={item.icon} alt={`${item.platform} icon`} className="icon-image" />
        <span className="hover-label">{item.platform}</span>
      </a>
    </div>
  );
};

export default LinkedIcon;
