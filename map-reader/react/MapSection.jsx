import React from 'react'

import { LeftCymbal, Hihat, LeftPedal, Snare, BassPedal, HighTom, LowTom, FloorTom, Cymbal } from "./Notes.jsx"

const notes = [ LeftCymbal, Hihat, LeftPedal, Snare, HighTom, BassPedal, LowTom, FloorTom, Cymbal]
export default class MapSection extends React.Component {
  render() {
    console.log('this.props.sectionData', this.props.sectionData);
    const noteArray = [[], [], [], [], [], [], [], [], []]
    this.props.sectionData.contents.forEach((content) => {
      console.log("content.note", content.note);
      for (let i = 0; i < 9; i++) {
        if (content.note.charAt(i) === "1") {
          noteArray[i].push(content.position);
        }
      }
    });

    console.log("noteArray", noteArray);

    let scale = 2.5;
    return (
      <table style={styles.section}>
        <tbody>
          <tr>
            {
              noteArray.map((foo, noteTypeIndex) =>
                <td style={{
                  position: "relative",
                  padding: 0,
                  height: 96 * scale,
                  width: 20,
                }} key={noteTypeIndex}>
                  <div style={{ position: "absolute", bottom: 0, background: "white", width: "100%", height: 1 }} />
                  <div style={{ position: "absolute", bottom: "50%", background: "white", width: "100%", height: 0.5 }} />
                  { foo &&
                    foo.map((bar, index) => (
                      <div
                        style={{
                          position: "absolute",
                          bottom: bar * scale - 1
                        }}
                        key={index}
                      >
                        { notes[noteTypeIndex] // temporary soluation
                          &&
                          React.createElement(notes[noteTypeIndex], null)
                        }
                      </div>
                    ))
                  }
                </td>
              )
            }
          </tr>
        </tbody>
      </table>
    );
  }
}

const styles = {
  section: {
    background: "black",
    borderSpacing: 0,
  }
}