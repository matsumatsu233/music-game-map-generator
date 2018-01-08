import React from 'react'

import MapSection from './MapSection.jsx';

const data = [{
  bpm: 180,
  contents: [{
    position: 0,
    note: '100001000',
  }, {
    position: 12,
    note: '010000000',
  }, {
    position: 24,
    note: '010100000',
  }, {
    position: 36,
    note: '010000000',
  }, {
    position: 42,
    note: '000100000',
  }, {
    position: 48,
    note: '010001000',
  }, {
    position: 60,
    note: '010001000',
  }, {
    position: 72,
    note: '010100000',
  }, {
    position: 84,
    note: '010000000',
  }]
}, {
  bpm: 180,
  contents: [{
    position: 0,
    note: '010001000',
  }, {
    position: 12,
    note: '010001000',
  }, {
    position: 24,
    note: '010100000',
  }, {
    position: 36,
    note: '010000000',
  }, {
    position: 42,
    note: '000100000',
  }, {
    position: 48,
    note: '010001000',
  }, {
    position: 60,
    note: '010001000',
  }, {
    position: 72,
    note: '010100000',
  }, {
    position: 84,
    note: '010000000',
  }]
}, {
  bpm: 180,
  contents: [{
    position: 0,
    note: '111111111',
  }]
}];

export default class MapReader extends React.Component {
  render() {
    return (
      <div>
        { data.reverse().map((sectionData, index) =>
          <MapSection
            sectionData={sectionData}
            key={index}
          />
        )}
      </div>
    );
  }
}
